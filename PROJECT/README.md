# Schrödinger Equation Solver – PHYS 4840 Final Project

## Overview

This project implements a command-line software tool that numerically solves the one-dimensional time-independent Schrödinger equation using **finite difference methods**. The program is written primarily in **Fortran**, with Python used for visualization. It is designed to be modular, efficient, and self-contained, without relying on external numerical libraries for matrix diagonalization.

## Features

- Solves the 1D time-independent Schrödinger equation
- User-defined potential options:
  - Harmonic oscillator
  - Infinite square well
  - (Others can be added numerically)
- Finite difference approximation for the second derivative
- Jacobi diagonalization (implemented from scratch, not imported)
- Outputs:
  - Normalized eigenfunctions $\psi(x)$
  - Corresponding energy eigenvalues
  - All results saved to plain text files
- Python script to plot:
  - Real-valued wavefunctions $\psi(x)$
  - Probability densities $|\psi(x)|^2$
  - Input potential $V(x)$
- Command-line interface with customizable input file
- Fully modular and documented Fortran codebase
- Includes `Makefile`, test case, and plotting script

## Methods

We numerically solve the time-independent Schrödinger equation:

$$
\left[ -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V(x) \right] \psi(x) = E \psi(x)
$$

Discretization is performed using the second-order central finite difference approximation:

$$
\frac{d^2 \psi}{dx^2} \approx \frac{\psi_{i+1} - 2\psi_i + \psi_{i-1}}{\Delta x^2}
$$

This leads to a matrix eigenvalue problem:

$$
H \psi = E \psi
$$

Where $H$ is the Hamiltonian matrix, assembled from the kinetic energy (Laplacian) and the user-defined potential.

## Numerical Techniques

- **Finite Difference Method (FDM)**: for discretizing the Laplacian
- **Jacobi Method**: for symmetric matrix diagonalization
- **Rectangular approximation**: for normalizing eigenfunctions

## Languages Used

- **Fortran**: all numerical computation and simulation
- **Python**: for reading output and plotting results

## Output

The solver generates:

- `xgrid.txt`: spatial grid
- `eigenvalues.txt`: energy levels
- `wavefunctions.txt`: eigenfunctions
- Plots of $\psi(x)$, $|\psi(x)|^2$, and $V(x)$ saved to the `plots/` directory

## Running the Code

1. Clone the repository
2. Edit `input.txt` to set parameters (grid, potential, number of states, etc.)
3. Run `make` to compile
4. Execute `make run` to run the solver and generate plots
5. Executre 'make clean' to clean the directory for a new run

## Future Goals

- Upload the package to PyPI (time permitting)
- Add more potential options (e.g., double-well)
- Optimize diagonalization for larger systems

