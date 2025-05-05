import numpy as np
import matplotlib.pyplot as plt
import os

# === Load data ===
x = np.loadtxt("xgrid.txt")
eigenvalues = np.loadtxt("eigenvalues.txt")
wavefunctions = np.loadtxt("wavefunctions.txt")  # No transpose
neigs = wavefunctions.shape[0]
Nx = len(x)
assert wavefunctions.shape[1] == Nx

# === Guess potential type from wavefunction boundary behavior
def infer_potential_type():
    if np.all(np.abs(wavefunctions[:, 0]) < 1e-3) and np.all(np.abs(wavefunctions[:, -1]) < 1e-3):
        return "Infinite Square Well", lambda x: np.zeros_like(x)
    else:
        k = 0.01
        return "Harmonic Oscillator", lambda x: k * x**2

potential_name, V = infer_potential_type()
Vx = V(x)
Vx_scaled = (Vx - Vx.min()) / (Vx.max() - Vx.min()) * np.max(wavefunctions**2)

# === Create output directory ===
os.makedirs("plots", exist_ok=True)

# === Plot wavefunctions ===
plt.figure(figsize=(10, 5))
for n in range(neigs):
    plt.plot(x, wavefunctions[n], label=fr"$\psi_{{{n+1}}}$ (E = {eigenvalues[n]:.2f})")
plt.plot(x, Vx_scaled, 'k--', label=f"Rescaled V(x) [{potential_name}]", alpha=0.6)
plt.title(r"Wavefunctions $\psi_n(x)$")
plt.xlabel("x")
plt.ylabel(r"$\psi(x)$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots/wavefunctions_all.png")
plt.close()

# === Plot probability densities ===
plt.figure(figsize=(10, 5))
for n in range(neigs):
    prob_density = wavefunctions[n]**2
    plt.plot(x, prob_density, label=fr"$|\psi_{{{n+1}}}|^2$ (E = {eigenvalues[n]:.2f})")
plt.plot(x, Vx_scaled, 'k--', label=f"Rescaled V(x) [{potential_name}]", alpha=0.6)
plt.title(r"Probability Densities $|\psi_n(x)|^2$")
plt.xlabel("x")
plt.ylabel(r"$|\psi(x)|^2$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots/prob_densities_all.png")
plt.close()

print("Plots saved to 'plots/'")


