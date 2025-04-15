#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
g = 9.81
l = 0.4
m = 1.0

# Time parameters
dt = 0.001
t_max = 10
t = np.arange(0, t_max, dt)

# Equations of Motion
def equations(r):
    theta1, theta2, omega1, omega2 = r
    delta = theta2 - theta1
    denom = (2 - np.cos(2 * delta))
    if np.abs(denom) < 1e-6:
        denom = 1e-6
    domega1 = (
        -g * (2 * np.sin(theta1) + np.sin(theta1 - 2 * theta2))
        - 2 * np.sin(delta) * (omega2 ** 2 * l + omega1 ** 2 * l * np.cos(delta))
    ) / (l * denom)
    domega2 = (
        2 * np.sin(delta) * (
            omega1 ** 2 * l + g * np.cos(theta1) + omega2 ** 2 * l * np.cos(delta)
        )
    ) / (l * denom)
    return np.array([omega1, omega2, domega1, domega2])

# RK4 Integrator
def rk4_step(r, dt):
    k1 = dt * equations(r)
    k2 = dt * equations(r + 0.5 * k1)
    k3 = dt * equations(r + 0.5 * k2)
    k4 = dt * equations(r + k3)
    return r + (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Simulate given initial conditions
def simulate(theta1_deg, theta2_deg, omega1, omega2):
    r0 = np.radians([theta1_deg, theta2_deg])  # Convert angles to radians
    r = np.array([r0[0], r0[1], omega1, omega2])
    R = np.zeros((len(t), 4))
    R[0] = r
    for i in range(1, len(t)):
        R[i] = rk4_step(R[i - 1], dt)
    theta1_vals, theta2_vals, omega1_vals, omega2_vals = R.T
    x1 = l * np.sin(theta1_vals)
    y1 = -l * np.cos(theta1_vals)
    x2 = x1 + l * np.sin(theta2_vals)
    y2 = y1 - l * np.cos(theta2_vals)
    return x1, y1, x2, y2

# Simulate three runs with small perturbations
run1 = simulate(90, 90, 0, 0)
run2 = simulate(90.5, 90, 0, 0)
run3 = simulate(90, 90.5, 0, 0)

# Calculate separation between Run 1 and others
dist12 = np.sqrt((run1[2] - run2[2])**2 + (run1[3] - run2[3])**2)
dist13 = np.sqrt((run1[2] - run3[2])**2 + (run1[3] - run3[3])**2)

# Plot divergence (chaos indicator)
plt.figure(figsize=(8, 5))
plt.plot(t, np.log(dist12 + 1e-12), label='Run 1 vs Run 2')
plt.plot(t, np.log(dist13 + 1e-12), label='Run 1 vs Run 3')
plt.xlabel("Time (s)")
plt.ylabel("log(Distance)")
plt.title("Divergence Between Slightly Perturbed Double Pendulums")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("chaos_divergence.png")
plt.show()

# --------------------------------
# Animation Setup
# --------------------------------
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
titles = ["Run 1: (90°, 90°)", "Run 2: (90.5°, 90°)", "Run 3: (90°, 90.5°)"]
runs = [run1, run2, run3]
lines = []

for ax, title in zip(axes, titles):
    ax.set_xlim(-2 * l, 2 * l)
    ax.set_ylim(-2 * l, 2 * l)
    ax.set_aspect('equal')
    ax.set_title(title)
    ax.grid(True)
    line, = ax.plot([], [], 'o-', lw=2, markersize=6)
    lines.append(line)

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def update(frame):
    for line, run in zip(lines, runs):
        x1, y1, x2, y2 = run
        thisx = [0, x1[frame], x2[frame]]
        thisy = [0, y1[frame], y2[frame]]
        line.set_data(thisx, thisy)
    return lines

ani = animation.FuncAnimation(
    fig, update, frames=range(0, len(t), 10),
    init_func=init, blit=True, interval=10
)

plt.tight_layout()
plt.show()

# Optional: Save animation
#ani.save("double_pendulum_comparison.gif", writer="pillow", fps=60)

