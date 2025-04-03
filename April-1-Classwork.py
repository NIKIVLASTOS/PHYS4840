#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             Class Work
###				Nikiphoros Vlastos
###             
#				April 1, 2025
###########################################
# ODEs: Runge-Kutta and friends (and a top secret topic)



# Second-order vs. fourth order Runge Kutta

#RK$ is three orders of h more accurate than second order RK


# >$ which gcc
# /usr/bin/gcc

# >$ gcc --version
# Apple clang version 15.0.0 (clang-1500.0.40.1)
# Target: x86_64-apple-darwin23.0.0
# Thread model: posix
# InstalledDir: /Library/Developer/CommandLineTools/usr/bin



############I still have gfortran now (on mac)##########

# >$ which gfortran
# /usr/local/bin/gfortran


# >$ gfortran --version
# GNU Fortran (Homebrew GCC 14.2.0_1) 14.2.0
# Copyright (C) 2024 Free Software Foundation, Inc.
# This is free software; see the source for copying conditions.  There is NO
# warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#HOW TO COMPILE THE CODE
# gfortran hello_world.f90 -o hello.exe

# 'gfortran' is calling fortran
# 'hello_world.f90' is telling it which file to compile
# '-o' is telling it you are specifying the output file name
# 'hello.exe' is the name of the file that is now an executable



# Now I

# >$ ./hello.exe
# Hello, Fortran!

# MODIFY THE FILE NOW, THEN RECOMPILE

# >$ ./hello.exe
# Hello, Fortran! I have rewritten this and recompiled, if you get this it is working!




###### COMPILING RUNGA KUTA FORTRAN

# >$ gfortran RK2.f90 -o RungaKuta.exe

# >$ ./RungaKuta.exe
# Integration complete. Results saved to rk2_results.dat

#NOW I HAVE A RESULTS FILE: rk2_results.dat



############# IN CLASS EXCERCISE #1 ###################

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
import time  # Import time module for timing

def rk2_method(f, x0, t0, t_end, dt):
    t_values = np.arange(t0, t_end + dt, dt)
    x_values = np.zeros(len(t_values))
    x_values[0] = x0

    for i in range(1, len(t_values)):
        k1 = dt * f(x_values[i - 1], t_values[i - 1])
        k2 = dt * f(x_values[i - 1] + 0.5 * k1, t_values[i - 1] + 0.5 * dt)
        x_values[i] = x_values[i - 1] + k2

    return t_values, x_values

def differential_eq(x, t):
    return x**2 - x  # dx/dt = x^2 - x

# Initial conditions
x0 = 0.5  # Only works when it is 0.5?
t0 = 0
t_end = 10
dt_values = [0.1, 0.05, 0.01, 0.005]  # Trying with multiple dt values

# Start timing
start_time = time.time()

plt.figure(figsize=(8, 5))

for dt in dt_values:
    t_values, x_values = rk2_method(differential_eq, x0, t0, t_end, dt)
    plt.plot(t_values, x_values, label=f"dt = {dt}")

# End timing
end_time = time.time()
execution_time = end_time - start_time

# Plot settings
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Second-Order Runge-Kutta Method for dx/dt = x² - x")
plt.grid(True)
plt.legend()
plt.show()

# Print execution time
print(f"Execution time: {execution_time:.6f} seconds")


############# IN CLASS EXCERCISE #2 ###################

import numpy as np
import matplotlib.pyplot as plt

def rk4_method(f, x0, t0, t_end, dt):
    t_values = np.arange(t0, t_end + dt, dt)
    x_values = np.zeros(len(t_values))
    x_values[0] = x0

    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        x = x_values[i - 1]
        
        k1 = dt * f(x, t)
        k2 = dt * f(x + 0.5 * k1, t + 0.5 * dt)
        k3 = dt * f(x + 0.5 * k2, t + 0.5 * dt)
        k4 = dt * f(x + k3, t + dt)
        
        x_values[i] = x + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

    return t_values, x_values

def differential_eq(x, t):
    return x**2 - x  # dx/dt = x^2 - x

# Initial conditions
x0 = 0.5
t0 = 0
t_end = 10
dt_values = [0.1, 0.05, 0.01, 0.005]  # Trying with multiple dt values

plt.figure(figsize=(8, 5))

# Start timing
start_time1 = time.time()

for dt in dt_values:
    t_values, x_values = rk4_method(differential_eq, x0, t0, t_end, dt)
    plt.plot(t_values, x_values, label=f"dt = {dt}")

# End timing
end_time1 = time.time()
execution_time1 = end_time1 - start_time1

plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Fourth-Order Runge-Kutta Method for dx/dt = x² - x")
plt.grid(True)
plt.legend()
plt.show()

print(f"Execution time: {execution_time1:.6f} seconds")

############# IN CLASS EXCERCISE #3 ###################


filename1 = 'rk2_results_function.dat'
filename2 = 'rk2_results_10000.dat'

## # Col.  1: t
## # Col. 2: x

t1, x1 = np.loadtxt(filename1, usecols=(0, 1), unpack=True, skiprows=1)
t2, x2 = np.loadtxt(filename2, usecols=(0, 1), unpack=True, skiprows=1)


fig, axes = plt.subplots(2, 1, figsize=(10, 12))


# Plot the 'function' verson
axes[0].plot(t1, x1, color="blue", alpha=0.6)
axes[0].set_title("N =  int((t_end - t) / dt)")


# plot the '10000' verion
axes[1].plot(t2, x2, color="green", alpha=0.6)
axes[1].set_title("N =  10000")


plt.tight_layout() 
plt.show()

############# IN CLASS EXCERCISE #4 ###################


# Correct filename
filename3 = 'rk4_results.dat'

# Read the data
t3, x3 = np.loadtxt(filename3, usecols=(0, 1), unpack=True, skiprows=1)

# Create a single plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the RK4 results
ax.plot(t3, x3, color="blue", alpha=0.6, label="RK4 Approximation")
ax.set_title("Fourth-Order Runge-Kutta Method")
ax.set_xlabel("t")
ax.set_ylabel("x(t)")
ax.grid(True)
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()

############# IN CLASS EXCERCISE #5 ###################



