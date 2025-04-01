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

def euler_method(f, x0, t0, t_end, dt):
    t_values = np.arange(t0, t_end + dt, dt)
    x_values = np.zeros(len(t_values))
    x_values[0] = x0  # THIS et initial condition

    for i in range(1, len(t_values)):
        x_values[i] = x_values[i - 1] + dt * f(x_values[i - 1], t_values[i - 1])

    return t_values, x_values

def differential_eq(x, t):
    expression = x**2 - x  # dx/dt = x^2 - x
    return expression

# Initial conditions
x0 = 1
t0 = 0
t_end = 10
dt_values = [1, 0.1, 0.5, 0.2]  # try two other step sizes

# Solve and plot for different dt values
#for dt in dt_values:
#    t_values, x_values = euler_method(differential_eq, x0, t0, t_end, dt)
#    plt.plot(t_values, x_values, label=f"dt = {dt}")

# Plotting the solution
plt.figure(figsize=(8, 5))
plt.plot(t_values, x_values, label="Euler Approximation", color="b")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Euler Method Solution for dx/dt = x² - x")
plt.grid(True)
plt.legend()
plt.show()


############# IN CLASS EXCERCISE #2 ###################


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

############# IN CLASS EXCERCISE #5 ###################



