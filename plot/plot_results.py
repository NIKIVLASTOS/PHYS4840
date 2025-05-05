#==========================
# File: plot_results.py
#==========================
import numpy as np
import matplotlib.pyplot as plt
import os

# === Load data ===
x = np.loadtxt("output/xgrid.txt")
eigenvalues = np.loadtxt("output/eigenvalues.txt")
wavefunctions = np.loadtxt("output/wavefunctions.txt")

# Sanity check shape
neigs = wavefunctions.shape[0]
Nx = len(x)
assert wavefunctions.shape[1] == Nx

# === Define potential function (same as used in Fortran) ===
def V(x):
    return x**2

Vx = V(x)

# === Create output directory for plots ===
os.makedirs("plots", exist_ok=True)

# === Plotting ===
for n in range(neigs):
    psi = wavefunctions[n, :]
    prob_density = psi**2

    # Plot wavefunction
    plt.figure(figsize=(8, 4))
    plt.plot(x, psi, label=f"Wavefunction $\\psi_{{{n+1}}}(x)$")
    plt.plot(x, Vx, 'k--', label="Potential $V(x)$", alpha=0.6)
    plt.title(f"Wavefunction ψ_{n+1}(x), Energy = {eigenvalues[n]:.2f}")
    plt.xlabel("x")
    plt.ylabel("ψ(x)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"plots/wavefunction_{n+1}.png")
    plt.close()

    # Plot probability density
    plt.figure(figsize=(8, 4))
    plt.plot(x, prob_density, label=f"$|\\psi_{{{n+1}}}(x)|^2$")
    plt.plot(x, Vx, 'k--', label="Potential $V(x)$", alpha=0.6)
    plt.title(f"Probability Density |ψ_{n+1}(x)|², Energy = {eigenvalues[n]:.2f}")
    plt.xlabel("x")
    plt.ylabel("$|ψ(x)|^2$")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"plots/prob_density_{n+1}.png")
    plt.close()

print("Plots saved to 'plots/' directory.")
