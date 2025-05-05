#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import celerite
from celerite import terms
import corner

def generate_sinusoidal_data(n, amp, freq, noise_std, phase=0.0):
    t = np.linspace(0, 10, n)
    y_true = amp * np.sin(2 * np.pi * freq * t + phase)
    y_obs = y_true + np.random.normal(0, noise_std, size=n)
    y_err = np.full(n, noise_std)
    return t, y_obs, y_err

def build_gp(params, t, yerr):
    log_S0, log_Q, log_omega0 = params
    kernel = terms.SHOTerm(log_S0=log_S0, log_Q=log_Q, log_omega0=log_omega0)
    gp = celerite.GP(kernel, mean=0.0)
    gp.compute(t, yerr)
    return gp

def neg_log_likelihood(params, t, y, yerr):
    try:
        gp = build_gp(params, t, yerr)
        return -gp.log_likelihood(y)
    except:
        return 1e25

def main(
    n_points=100,
    amp=2.0,
    period = 5.42069,
    noise_std=0.1,
    phase=np.pi/4,
    normalize=True
):

    freq = 1/period

    t, y, yerr = generate_sinusoidal_data(n_points, amp, freq, noise_std, phase)
    idx = np.argsort(t)
    t, y, yerr = t[idx], y[idx], yerr[idx]

    if normalize:
        y = (y - np.mean(y)) / np.std(y)

    init = [np.log(np.var(y)), np.log(1.0), np.log(2 * np.pi * freq)]
    bounds = [
        (np.log(1e-5), np.log(10.0)),
        (np.log(0.5), np.log(100.0)),
        (np.log(0.1), np.log(100.0))
    ]

    result = minimize(neg_log_likelihood, init, args=(t, y, yerr), bounds=bounds, method="L-BFGS-B")
    gp = build_gp(result.x, t, yerr)

    log_S0, log_Q, log_omega0 = result.x
    S0 = np.exp(log_S0)
    Q = np.exp(log_Q)
    omega0 = np.exp(log_omega0)
    period = 2 * np.pi / omega0
    tau = Q / omega0

    print("\nOptimized GP Parameters:")
    print(f"Amplitude (S0)       = {S0:.4f}")
    print(f"Quality factor (Q)   = {Q:.4f}")
    print(f"ω₀ (rad/s)           = {omega0:.4f}")
    print(f"Period (s)           = {period:.4f}")
    print(f"Characteristic time  = {tau:.4f}")

    # Forward prediction range
    t_pred = np.linspace(t.min(), t.max() + period, 1200)
    mu, var = gp.predict(y, t_pred, return_var=True)

    plt.errorbar(t, y, yerr=yerr, fmt=".k", label="Data")
    plt.plot(t_pred, mu, label="GP Prediction")
    plt.fill_between(t_pred, mu - np.sqrt(var), mu + np.sqrt(var), alpha=0.3)
    plt.xlabel("Time")
    plt.ylabel("Flux (normalized)" if normalize else "Flux")
    plt.title(f"GP Fit + Prediction (forward by 1 period ≈ {period:.2f})")
    plt.legend()
    plt.tight_layout()
    plt.show()

    samples = np.random.multivariate_normal(result.x, np.eye(3)*0.01, size=1000)
    corner.corner(samples, labels=["log_S0", "log_Q", "log_omega0"], truths=result.x)
    plt.show()

if __name__ == "__main__":
    main()