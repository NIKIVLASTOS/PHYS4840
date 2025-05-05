#==========================                                             
# File: plot_results.py                                                # Python to visualize 1D Schrödinger results
#==========================
import numpy as np                                                     
import matplotlib.pyplot as plt                                        
import os                                                              

# === Read input.txt ===
def read_clean_input(path):                                            # This Function to rea and clean input.txt
    with open(path, "r") as f:                                         # Open file for reading
        return [line.strip() for line in f if line.strip() and not line.strip().startswith("!")]  # Return non-empty, non-comment lines

lines = read_clean_input("input.txt")                                  # read  lines
xmin, xmax, Nx_check = map(float, lines[0].split())                    # Parse first line: grid limits and Nx
potential_type = int(lines[1])                                         # Parse second line: potential type
nstates = int(lines[2])                                                # Parse third line: number of eigenstates
V0 = float(lines[3]) if potential_type == 3 else 0.0                   # Parse V0 if potential type is 3 (finite square well)

# === Load data ===
x = np.loadtxt("xgrid.txt")                                            # Load spatial grid
eigenvalues = np.loadtxt("eigenvalues.txt")                            # Load computed eigenvalues
wavefunctions = np.loadtxt("wavefunctions.txt", ndmin=2)               # Load wavefunctions (2D array forced)

# === Ensure wavefunctions are shape (nstates, Nx) ===
if wavefunctions.shape[0] != nstates:                                  # If shape is (Nx, nstates), transpose
    wavefunctions = wavefunctions.T                                    # Transpose to get (nstates, Nx)

neigs, Nx = wavefunctions.shape                                        # Get dimensions of wavefunction array
assert len(x) == Nx                                                    # Make sure x-grid length matches Nx

# === Define potential ===
def V(x, potential_type, xmin, xmax, V0):                              # Function to evaluate potential at x
    if potential_type == 1:                                            # Harmonic oscillator
        return 0.5 * 5500 * x**2                                       # Scaled harmonic oscillator (match scaling to Fortran laid out scaling facotr)
    elif potential_type == 2:                                          # Infinite square well
        return np.where((x >= xmin) & (x <= xmax), 0, 1e6)             # 0 inside, very large outside
    elif potential_type == 3:                                          # Finite square well
        return np.where((x >= xmin) & (x <= xmax), 0, V0)              # 0 inside, V0 outside
    else:
        raise ValueError("Invalid potential type.")                    # Error for invalid potential code

Vx = V(x, potential_type, xmin, xmax, V0)                              # Evaluate full potential array

# === Create output directory ===
os.makedirs("plots", exist_ok=True)                                    # make directory to store plots (no error if exists)

# === Diagnostic plot: raw wavefunctions over grid ===
plt.figure(figsize=(10, 6))                                            # Create figure for raw wavefunctions
for n in range(nstates):                                               # Loop over states
    plt.plot(x, wavefunctions[n], label=f"$\\psi_{n}(x)$")             # Plot each raw wavefunction
plt.title("Raw wavefunctions (no energy offset or scaling)")           # Title
plt.xlabel("x")                                                        # X-axis label
plt.grid(True)                                                         # Add grid
plt.legend()                                                           # Add legend
plt.tight_layout()                                                     # Tight layout
plt.savefig("plots/raw_wavefunctions.png")                             # Save raw wavefunction plot

# === Plot settings ===
wf_scale = 10.0                                                        # Vertical scaling for visibility
ymin = -5                                                              # Lower y-limit
ymax = max(eigenvalues[:nstates]) + 25                                 # Upper y-limit based on max eigenvalue
xlim_range = (x[0], x[-1])                                             # X-axis limits from grid

# === Plot wavefunctions overlapping with energy lines ===
plt.figure(figsize=(10, 6))                                            # Create figure
plt.plot(x, Vx, 'r--', label="V(x)")                                   # Plot potential
for n in range(nstates):                                               # Plot wavefunctions shifted by energy
    plt.plot(x, eigenvalues[n] + wf_scale * wavefunctions[n], label=rf"$\psi_{{{n}}}(x)$")
for n in range(nstates):                                               # Draw horizontal lines at each eigenvalue
    plt.axhline(eigenvalues[n], color='gray', linestyle='-', linewidth=0.5)
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)           # Line at E = 0

plt.title(r"Wavefunctions $\psi_n(x)$ in Harmonic Potential")          # Title with LaTeX
plt.xlabel("x")                                                        # X-axis label
plt.ylabel("Amplitude (shifted to $E_n$)")                             # Y-axis label
plt.ylim(ymin, ymax)                                                   # Set y-axis limits
plt.xlim(*xlim_range)                                                  # Set x-axis limits
plt.grid(True)                                                         # Add grid
plt.legend()                                                           # Add legend
plt.tight_layout()                                                     # Apply tight layout
plt.savefig("plots/wavefunctions.png")                                 # Save wavefunctions plot

# === Plot probability densities with vertical offset ===
plt.figure(figsize=(10, 6))                                            # figure for probability densities
plt.plot(x, Vx, 'r--', label="V(x)")                                   # Plot potential
for n in range(nstates):                                               # Plot shifted probability densities
    plt.plot(x, eigenvalues[n] + wf_scale * wavefunctions[n]**2, label=rf"$|\psi_{{{n}}}(x)|^2$")
for n in range(nstates):                                               # Energy level lines
    plt.axhline(eigenvalues[n], color='gray', linestyle='-', linewidth=0.5)
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)           # Line at E = 0

plt.title(r"Probability Densities $|\psi_n(x)|^2$ in Harmonic Potential")  # Title
plt.xlabel("x")                                                        # X-axis label
plt.ylabel("Probability (shifted to $E_n$)")                           # Y-axis label
plt.ylim(ymin, ymax)                                                   # Y-axis range
plt.xlim(*xlim_range)                                                  # X-axis range
plt.grid(True)                                                         # Grid
plt.legend()                                                           # Legend
plt.tight_layout()                                                     # Layout
plt.savefig("plots/probability_densities.png")                         # Save plot

print("Plots saved in 'plots/' directory.")                            # Print completion message

