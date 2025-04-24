#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             HOMEWORK #7
###             Nikiphoros Vlastos
###             
#               
###########################################

##### Question 0  ############################################################################################################################


##### IN CLASS EXCERCISE #1 (Answering Questions ############################################################################


# A) We have made it three dimensional so we are moving to +/- h in the x, y and z directions therefore 
# we have x +/- h, y +/- h, and z +/- h each one of these when being done the two others will be being 
# held constant, such x and y are constand and then we have z + h and then x and y are held constand and we have z - h

# B) When I set the grid size back to 100, there were many more points, and so the calculation takes 
# exponentially longer, for just 30 iterations it took my computer over 30 seconds then I cancelled 
# the run, where as when it was only 30 points, the whole thing ran to below the convergence set criteria 
# in roughy 60 seconds (and this was over 1350 iterations, so clearly it would take serious time with n = 100)


# C) When the convergence criteria is made larger, it converges in less iterations (usually saving time) but 
# this will make it less accurate. When the converance criteria is made smaller it converges in more 
# iterations (usually taking more time) but it will be more accurate to a 'true' value

# D) When the boundary conditions are being preserved in each of the 2D and 3D cases:
# In the 2D case, boundary conditions are enforced on the four edges of the grid (top, bottom, left, right) 
# by fixing the corresponding rows and columns. In the 3D case, boundary conditions must be applied 
# to all six faces of the cube. In this code, the top face (z = 0) is set to a fixed voltage V
# while the other five faces (z = N, x = 0, x = N, y = 0, y = N) are grounded (set to zero). 
# This is enforced after each iteration to prevent the update step from modifying the boundaries.

##### IN CLASS EXCERCISE #2 (Answering Questions ###################################################################

# A) The function np.roll(array, shift, axis) shifts the elements of a NumPy array by a given number of 
# positions along a specified axis. The key feature of np.roll() is that it wraps around the elements 
# that go past the edge, reintroducing them at the other end.

# B) Code is below to solve -- the np.roll function can be found in my nikiphoros_functions_lib.py script

import numpy as np
import matplotlib.pyplot as plt
from nikiphoros_functions_lib import laplacian_operator

# Constants
N = 30              # Grid size (NxNxN cube)
h = 1.0             # Grid spacing
V = 1.0             # Voltage on top face (z = 0)
target = 1e-6       # Convergence criterion
max_iters = 10000   # Optional safety limit

# Initialize potential arrays
phi = np.zeros((N+1, N+1, N+1))
phinew = np.empty_like(phi)

# Apply boundary condition: top face at V
phi[:,:,0] = V

# Iterative solver (Jacobi-style using np.roll)
delta = 1.0
iteration = 0

while delta > target and iteration < max_iters:
    iteration += 1

    # Use np.roll to compute the average of neighbors
    phinew = (np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0) +
              np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1) +
              np.roll(phi, 1, axis=2) + np.roll(phi, -1, axis=2)) / 6.0

    # Reapply boundary conditions after update
    phinew[:,:,0] = V
    phinew[:,:,N] = 0
    phinew[:,0,:] = 0
    phinew[:,N,:] = 0
    phinew[0,:,:] = 0
    phinew[N,:,:] = 0

    # Compute convergence
    delta = np.max(np.abs(phinew - phi))
    phi = phinew

    if iteration % 10 == 0:
        print(f"Iteration {iteration}, max delta = {delta:.2e}")

print(f"Converged in {iteration} iterations (Δ = {delta:.2e})")

# Visualize middle slice in z-direction
mid_z = N // 2
plt.figure(figsize=(6,5))
plt.imshow(phi[:,:,mid_z], origin='lower', cmap='inferno')
plt.colorbar(label='Potential φ')
plt.title(f"Midplane slice at z = {mid_z}")
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.show()


##### IN CLASS EXCERCISE #3 (Excercise 9.3 from the book) ###################################################################



# ----------------------------
# Constants and Parameters
# ----------------------------
L = 0.01           # Thickness in meters (1 cm)
D = 4.25e-6        # Thermal diffusivity (m^2/s)
N = 100            # Number of intervals
a = L / N          # Grid spacing
h = 1e-4           # Time step
epsilon = h / 1000 # Tolerance for float-time comparison

T_lo = 0.0         # Boundary temperature on cold side (°C)
T_hi = 50.0        # Boundary temperature on hot side (°C)
T_mid = 20.0       # Initial interior temperature (°C)

# Times at which to plot
plot_times = [0.01, 0.1, 0.4, 1.0, 10.0]
t_end = max(plot_times) + epsilon

# ----------------------------
# Initialization
# ----------------------------
T = np.empty(N + 1)
T[0] = T_hi
T[N] = T_lo
T[1:N] = T_mid

Tp = np.empty_like(T)
Tp[0] = T_hi
Tp[N] = T_lo

c = h * D / (a * a)
t = 0.0

# Store profiles to plot later
profiles = []
times_recorded = []

# ----------------------------
# Time Evolution (FTCS method)
# ----------------------------
while t < t_end:
    Tp[1:N] = T[1:N] + c * (T[0:N-1] + T[2:N+1] - 2 * T[1:N])
    T, Tp = Tp, T
    t += h

    for pt in plot_times:
        if abs(t - pt) < epsilon and pt not in times_recorded:
            profiles.append(T.copy())
            times_recorded.append(pt)

# ----------------------------
# Plotting Results
# ----------------------------
x = np.linspace(0, L, N+1)
for T_profile, time in zip(profiles, times_recorded):
    plt.plot(np.arange(N+1), T_profile, label=f"t = {time:.2f} s")

plt.xlabel("x (grid index)")
plt.ylabel("Temperature (°C)")
plt.title("Heat Conduction in Steel (Example 9.3)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

##### Question 1 (Excercies 9.4)  ############################################################################################################################

import numpy as np
import matplotlib.pyplot as plt

# ------------------------
# Parameters and Constants
# ------------------------
depth = 20.0            # in meters
D = 0.1                 # thermal diffusivity (m^2/day)
days_per_year = 365
years = 10
total_time = years * days_per_year

N = 100                 # grid divisions
dz = depth / N          # spatial step
h = 0.1                 # time step in days
epsilon = h / 1000      # float comparison tolerance

# Surface temperature oscillation
A = 10.0                # mean surface temp (°C)
B = 12.0                # seasonal variation amplitude (°C)
tau = days_per_year     # period of oscillation

# Initial temperature (entire column at 10°C)
T = np.full(N + 1, 10.0)
Tp = np.empty_like(T)

# Boundary condition at bottom: constant 11°C
T[-1] = 11.0
Tp[-1] = 11.0

# FTCS coefficient
c = h * D / dz**2

# Storage for profiles during final year
profiles = []
target_days = [9.0 * days_per_year + d for d in [0, 91.25, 182.5, 273.75]]

# ------------------------
# Time Evolution
# ------------------------
t = 0.0
while t < total_time + epsilon:
    # Update surface boundary (depth = 0)
    T[0] = A + B * np.sin(2 * np.pi * t / tau)
    Tp[0] = T[0]

    # FTCS update for interior points
    Tp[1:N] = T[1:N] + c * (T[0:N-1] + T[2:N+1] - 2 * T[1:N])

    # Update time and arrays
    T, Tp = Tp, T
    t += h

    # Save snapshot if within epsilon of target days
    for d in target_days:
        if abs(t - d) < epsilon:
            profiles.append(T.copy())

# ------------------------
# Plotting
# ------------------------
z = np.linspace(0, depth, N + 1)

plt.figure(figsize=(6,5))
for i, prof in enumerate(profiles):
    label = f"{['Jan', 'Apr', 'Jul', 'Oct'][i]}"
    plt.plot(prof, z, label=label)

plt.gca().invert_yaxis()
plt.xlabel("Temperature (°C)")
plt.ylabel("Depth (m)")
plt.title("Temperature vs. Depth (Final Year)")
plt.legend(title="Month")
plt.grid(True)
plt.tight_layout()
plt.show()


