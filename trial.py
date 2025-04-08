#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def square_wave(t):
    """Generates a square wave with frequency 1 and amplitude 1."""
    return 1 if int(2 * t) % 2 == 0 else -1

def low_pass_filter(V_out, t, RC):
    """Defines the differential equation for the low-pass filter."""
    V_in = square_wave(t)
    # The derivative of V_out based on the equation: dV_out/dt = (V_in - V_out) / RC
    return (V_in - V_out) / RC

def rk4_method(f, x0, t0, t_end, dt, RC):
    """Fourth-order Runge-Kutta method to solve the differential equation."""
    t_values = np.arange(t0, t_end + dt, dt)
    x_values = np.zeros(len(t_values))
    x_values[0] = x0

    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        x = x_values[i - 1]
        
        k1 = dt * f(x, t, RC)
        k2 = dt * f(x + 0.5 * k1, t + 0.5 * dt, RC)
        k3 = dt * f(x + 0.5 * k2, t + 0.5 * dt, RC)
        k4 = dt * f(x + k3, t + dt, RC)
        
        x_values[i] = x + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

    return t_values, x_values

# Parameters
t0, t_end = 0, 10
x0 = 0  # Initial condition V_out(0) = 0
dt = 0.001  # Small step size for accuracy
RC_values = [0.01, 0.1, 1]  # Different RC values

plt.figure(figsize=(10, 6))

for RC in RC_values:
    t_values, V_out_values = rk4_method(low_pass_filter, x0, t0, t_end, dt, RC)
    plt.plot(t_values, V_out_values, label=f"RC = {RC}")

plt.xlabel("Time (t)")
plt.ylabel("V_out(t)")
plt.title("Low-pass Filter Response for Different RC Values")
plt.legend()
plt.grid()
plt.show()
