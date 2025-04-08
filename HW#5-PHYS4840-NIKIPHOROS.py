#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             Homework #5
###				Nikiphoros Vlastos
###             
#				April 3, 2025
###########################################



# My code for FORTRAN RUNGE KUTA can be found in RK2.f90 and RK4.f90 (this is for the In Class Assignments --Question 0).
# My timing code for Fortran (the bash file) Can be found in time_fortran.sh
# My code for FORTRAN RUNGE KUTA for Problems 2,3,4 can be found in RK2_x^3-sin.f90 and RK4_x^3-sin.f90


################## IN CLASS WORK (QUESTION 0) #############################
############# IN CLASS EXCERCISE #1 ###################

import numpy as np
import matplotlib.pyplot as plt
import time  

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
t_end = 1000
dt_values = [0.1]  # Trying with multiple dt values woul look like: dt_values = [0.1, 0.05, 0.01, 0.005]

# Start timing
start_time = time.time()

plt.figure(figsize=(8, 5))

for dt in dt_values:
    t_values, x_values = rk2_method(differential_eq, x0, t0, t_end, dt)
    plt.plot(t_values, x_values, label=f"dt = {dt}")

# End timing
end_time = time.time()
# Calculate the total time it took
execution_time = end_time - start_time

# Makeing the plot settings
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("QUESTION 0: Second-Order Runge-Kutta Method for dx/dt = x² - x")
plt.grid(True)
plt.legend()
plt.show()

# Print the total execution time
print(f"Execution time SECOND ORDER PYTHON N = 10000: {execution_time:.6f} seconds")


############# IN CLASS EXCERCISE #2 ###################


#This is the RK4 method
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
t_end = 10000
dt_values = [0.1]  # Trying with multiple dt values Would look like: dt_values = [0.1, 0.05, 0.01, 0.005]

plt.figure(figsize=(8, 5))

# Start timing
start_time1 = time.time()

for dt in dt_values:
    t_values, x_values = rk4_method(differential_eq, x0, t0, t_end, dt)
    plt.plot(t_values, x_values, label=f"dt = {dt}")

# End timing
end_time1 = time.time()
#Calc time it took
execution_time1 = end_time1 - start_time1

plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("QUESTION 0: Fourth-Order Runge-Kutta Method for dx/dt = x² - x")
plt.grid(True)
plt.legend()
plt.show()

#Print total time
print(f"Execution time RK4 PYTHON N=10000: {execution_time1:.6f} seconds")

############# IN CLASS EXCERCISE #3 ###################

# This loads in the rk2 results
filename1 = 'rk2_results_function.dat'
filename2 = 'rk2_results_10000.dat'

## # Col.  1: t
## # Col. 2: x

t1, x1 = np.loadtxt(filename1, usecols=(0, 1), unpack=True, skiprows=1)
t2, x2 = np.loadtxt(filename2, usecols=(0, 1), unpack=True, skiprows=1)


fig, axes = plt.subplots(2, 1, figsize=(10, 12))


# Plot the 'function' verson
axes[0].plot(t1, x1, color="blue", alpha=0.6, linestyle='--')
axes[0].set_title("QUESTION 0: RK2 FORTRAN N =  int((t_end - t) / dt)")


# plot the '10000' version
axes[1].plot(t2, x2, color="green", alpha=0.6)
axes[1].set_title("QUESTION 0: RK2 FORTRAN N =  10000")


plt.tight_layout() 
plt.show()

############# IN CLASS EXCERCISE #4 ###################


# Correct filename
filename3 = 'rk4_results10000.dat'
filename4 = 'rk4_resultsFUNCTION.dat'

# Read the data
t3, x3 = np.loadtxt(filename3, usecols=(0, 1), unpack=True, skiprows=1)
t4, x4 = np.loadtxt(filename4, usecols=(0, 1), unpack=True, skiprows=1)

# Create a single plot
fig, axes = plt.subplots(2, 1, figsize=(10, 12))

# Plot the RK4 results
axes[0].plot(t3, x3, color="blue", alpha=0.6, label="10000 Approximation")
axes[0].set_title("QUESTION 0: RK4 FORTRAN: N =  10000")
axes[1].plot(t4, x4, color="blue", alpha=0.6, label="Function Approximation")
axes[1].set_title("QUESTION 0: RK4 FORTRAN: N =  int((t_end - t) / dt)")

#ax.grid(True)


# Show the plot
plt.tight_layout()
plt.show()

############# IN CLASS EXCERCISE #5 ###################

#TIMING RESULTS:

# Execution time SECOND ORDER PYTHON N = 10000: 0.208382 seconds
# Execution time RK4 PYTHON N=10000: 0.370754 seconds

#FOR RK2 FORTRAN:
#Execution time (seconds):   2.7930000000000000E-002
#Compilation time: 1.0 seconds
#Execution time: 0 seconds


#FOR RK4 FORTRAN:
#Compilation time: 0 seconds
#Execution time: 0 seconds




################## QUESTION 1 ######################################################################################################################################################


def square_wave(t):
    """Generates a square wave with frequency 1 and amplitude 1."""
    return 1 if int(2 * t) % 2 == 0 else -1

def low_pass_filter(V_out, t, RC):
    """Defines the diff equation"""
    V_in = square_wave(t)
    return (V_in - V_out) / RC

def rk4_method(f, x0, t0, t_end, dt, RC):
    """Fourth-order Runge-Kutta"""
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
x0 = 0  # Initial condition Vout(0) = 0
dt = 0.001  # Small step size for accuracy
RC_values = [0.01, 0.1, 1]  # Different RC values

plt.figure(figsize=(10, 6))

for RC in RC_values:
    t_values, V_out_values = rk4_method(low_pass_filter, x0, t0, t_end, dt, RC)
    plt.plot(t_values, V_out_values, label=f"RC = {RC}")

plt.xlabel("Time (t)")
plt.ylabel("V_out(t)")
plt.title("QUESTION 1: Low-pass Filter Response for Different RC Values")
plt.legend()
plt.grid()
plt.show()


#PART B
#The output Vout(t) varies significantly based on the RC time constant, demonstrating how the 
#low-pass filter affects the input square wave. For RC=0.01 (blue curve), the output closely follows 
#the input signal, with only minor smoothing at the transitions. The capacitor charges and discharges 
#quickly, allowing the output to nearly replicate the square wave with slightly softened edges.

#For RC=0.1 (orange curve), the smoothing effect is more pronounced. The transitions between high 
#and low values are rounded, as the capacitor takes longer to charge and discharge. This attenuates 
#the high-frequency components of the input signal, causing the output to take on a more gradual, curved shape.

#For RC=1 (green curve), the output waveform changes significantly. Instead of smoothly transitioning 
#between values, the output forms a sharp, triangular-like pattern. This suggests that the circuit 
#is no longer just smoothing the square wave but is instead producing a response characteristic of 
#a different type. The capacitor is charging and discharging at a rate that prevents 
#it from fully reaching the input voltage before the signal switches. As a result, the waveform becomes 
#more linear, resembling a sawtooth or triangular wave.
#Overall, the circuit acts as a low-pass filter, but the effect depends strongly on RC. 
#For small RC, the output retains the shape of the input signal with minor smoothing. As RC increases, 
#the circuit increasingly suppresses high-frequency components, transitioning from rounded 
#smoothing to a more linearbehavior.







################## QUESTION 2 ######################################################################################################################################################


#######THIS IS RK2 ################
def rk2_method(f, x0, t0, t_end, dt):
    t_values_1 = np.arange(t0, t_end + dt, dt)
    x_values_1 = np.zeros(len(t_values_1))
    x_values_1[0] = x0

    for i in range(1, len(t_values_1)):
        k1 = dt * f(x_values_1[i - 1], t_values_1[i - 1])
        k2 = dt * f(x_values_1[i - 1] + 0.5 * k1, t_values_1[i - 1] + 0.5 * dt)
        x_values_1[i] = x_values_1[i - 1] + k2

    return t_values_1, x_values_1

def differential_eq(x, t):
    return -x**3 + np.sin(t)  # differential equation: dx/dt = -x^3 + sin(t)

x0 = 1.0  # Given initial condition x = 1 at t = 0
t0 = 0
t_end_values = [10]  # Intervals [0, 10] and [0, 10000] BUT I TOOK OUT THE 10000 SO I COULD PLOT JUST THE 10 FOR QUESTION 3 OTHERWISE IT WOULD LOOK LIKE: t_end_values = [10, 10000]
dt = 0.1  # Single dt value

# Start timing
start_time = time.time()

plt.figure(figsize=(10, 6))

for t_end in t_end_values:
    t_values_1, x_values_1 = rk2_method(differential_eq, x0, t0, t_end, dt)
    plt.plot(t_values_1, x_values_1, label=f"t_end = {t_end}")

# End timing
end_time = time.time()
execution_time = end_time - start_time

# Plot settings
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("QUESTION 2: Second-Order Runge-Kutta  PYTHON Method for dx/dt = -x^3 + sin(t)")
plt.grid(True)
plt.legend()
plt.show()

# Print execution time
print(f"Execution time Second-Order Runge-Kutta PYTHON Method for dx/dt = -x^3 + sin(t): {execution_time:.6f} seconds")

#######THIS IS RK4 (QUESTION 3) ################################################################################################

def rk4_method(f, x0, t0, t_end, dt):
    t_values_2 = np.arange(t0, t_end + dt, dt)
    x_values_2 = np.zeros(len(t_values_2))
    x_values_2[0] = x0

    for i in range(1, len(t_values_2)):
        t = t_values_2[i - 1]
        x = x_values_2[i - 1]
        
        k1 = dt * f(x, t)
        k2 = dt * f(x + 0.5 * k1, t + 0.5 * dt)
        k3 = dt * f(x + 0.5 * k2, t + 0.5 * dt)
        k4 = dt * f(x + k3, t + dt)
        
        x_values_2[i] = x + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

    return t_values_2, x_values_2

def differential_eq(x, t):
    return -x**3 + np.sin(t)  # differential equation: dx/dt = -x^3 + sin(t)

# Initial conditions
x0 = 1.0  # Initial condition is supposed to be x = 1 at t = 0
t0 = 0
t_end_values = [10]  # Intervals [0, 10] and [0, 10000] BUT I TOOK OUT THE 10000 SO I COULD PLOT JUST THE 10 FOR QUESTION 3 OTHERWISE IT WOULD LOOK LIKE: t_end_values = [10, 10000]
dt = 0.1  # Single dt value

plt.figure(figsize=(10, 6))

# Start timing
start_time1 = time.time()

for t_end in t_end_values:
    t_values_2, x_values_2 = rk4_method(differential_eq, x0, t0, t_end, dt)
    plt.plot(t_values_2, x_values_2, label=f"t_end = {t_end}")

# End timing
end_time1 = time.time()
execution_time1 = end_time1 - start_time1

plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("QUESTION 3 Fourth-Order Runge-Kutta PYTHON Method for dx/dt = -x^3 + sin(t)")
plt.grid(True)
plt.legend()
plt.show()

print(f"Execution time Fourth-Order Runge-Kutta PYTHON Method for dx/dt = -x^3 + sin(t): {execution_time1:.6f} seconds")



# PLOTTING ALL TOGETHER


# Load the data from the Fortran output files

rk2_data = np.loadtxt('rk2_resultsHW.dat', skiprows=1)  # Skip the first line (headers)
rk4_data = np.loadtxt('rk4_resultsHW.dat', skiprows=1)

# Extract t and x values for RK2 and RK4
t_rk2, x_rk2 = rk2_data[:, 0], rk2_data[:, 1]
t_rk4, x_rk4 = rk4_data[:, 0], rk4_data[:, 1]

# Create the plot
plt.figure(figsize=(8, 5))

# Plot RK2 and RK4 results
plt.plot(t_rk2, x_rk2, label="RK2 Method (Fortran)", color='b', linestyle='--')  # Blue line for RK2 ( in Python)
plt.plot(t_rk4, x_rk4, label="RK4 Method (Fortran)", color='r', linestyle='--')  # Red line for RK4 (in Python)


plt.plot(t_values_1, x_values_1, label="RK2 Method (python)", color='g', linestyle='--')  # Green dashed line for RK2 ( in Fortran)
plt.plot(t_values_2, x_values_1, label="RK4 Method (Python)", color='orange', linestyle='--')  # Orange dashed line for RK4 (inFortran)

# Add labels and title
plt.xlim(0, 10)
plt.xlabel("Time (t)")
plt.ylabel("Solution x(t)")
plt.title("QUESTION 3: Comparison of RK2 and RK4 Methods 0-10")

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

#### ALL 4 PLOTS THE EXACT SAME SO THEY OVERLAP, IF YOU HASHTAG THEM OUT AND LOOK AT EACH INDIVIDUALLY YOU WILL SEE THIS

####### Question 4 ################################################################################################

#My timing code is in time_fortran.sh


#TIMING PYTHON 10,000 RK2
def rk2_method(f, x0, t0, t_end, dt):
    t_values_1 = np.arange(t0, t_end + dt, dt)
    x_values_1 = np.zeros(len(t_values_1))
    x_values_1[0] = x0

    for i in range(1, len(t_values_1)):
        k1 = dt * f(x_values_1[i - 1], t_values_1[i - 1])
        k2 = dt * f(x_values_1[i - 1] + 0.5 * k1, t_values_1[i - 1] + 0.5 * dt)
        x_values_1[i] = x_values_1[i - 1] + k2

    return t_values_1, x_values_1

def differential_eq(x, t):
    return -x**3 + np.sin(t)  #  differential equation: dx/dt = -x^3 + sin(t)

# Initial conditions
x0 = 1.0  # Given initial condition x = 1 at t = 0
t0 = 0
t_end_values = [100]  
dt = 0.1  # Single dt value

# Start timing
start_time = time.time()

plt.figure(figsize=(10, 6))

for t_end in t_end_values:
    t_values_1, x_values_1 = rk2_method(differential_eq, x0, t0, t_end, dt)
    plt.plot(t_values_1, x_values_1, label=f"t_end = {t_end}")

# End timing
end_time = time.time()
execution_time = end_time - start_time

# Print execution time
print(f"Execution time Second-Order Runge-Kutta PYTHON Method N= 10,000 for dx/dt = -x^3 + sin(t): {execution_time:.6f} seconds")


# Execution time Second-Order Runge-Kutta PYTHON Method N= 10,000 for dx/dt = -x^3 + sin(t): 0.337190 seconds

#TIMING PYTHON 10,000 RK4
def rk4_method(f, x0, t0, t_end, dt):
    t_values_2 = np.arange(t0, t_end + dt, dt)
    x_values_2 = np.zeros(len(t_values_2))
    x_values_2[0] = x0

    for i in range(1, len(t_values_2)):
        t = t_values_2[i - 1]
        x = x_values_2[i - 1]
        
        k1 = dt * f(x, t)
        k2 = dt * f(x + 0.5 * k1, t + 0.5 * dt)
        k3 = dt * f(x + 0.5 * k2, t + 0.5 * dt)
        k4 = dt * f(x + k3, t + dt)
        
        x_values_2[i] = x + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

    return t_values_2, x_values_2

def differential_eq(x, t):
    return -x**3 + np.sin(t)  # differential equation: dx/dt = -x^3 + sin(t)

# Initial conditions
x0 = 1.0  # Initial condition is supposed to be x = 1 at t = 0
t0 = 0
t_end_values = [100]
dt = 0.1  # Single dt value

plt.figure(figsize=(10, 6))

# Start timing
start_time1 = time.time()

for t_end in t_end_values:
    t_values_2, x_values_2 = rk4_method(differential_eq, x0, t0, t_end, dt)
    #plt.plot(t_values_2, x_values_2, label=f"t_end = {t_end}")

# End timing
end_time1 = time.time()
execution_time1 = end_time1 - start_time1

print(f"Execution time Fourth-Order Runge-Kutta PYTHON Method N= 10,000 for dx/dt = -x^3 + sin(t): {execution_time1:.6f} seconds")


# THESE ARE THE VALUES I GOT

#10000

# Execution time Second-Order Runge-Kutta PYTHON Method N= 10,000 for dx/dt = -x^3 + sin(t): 0.337190 seconds

# Execution time Fourth-Order Runge-Kutta PYTHON Method N= 10,000 for dx/dt = -x^3 + sin(t): 0.540335 seconds

#Runge Kuta 2 N=10000 FORTRAN Compilation time: .788077000 seconds
#Runge Kuta 2 N=10000 FORTRAN Execution time: .328761000 seconds

#Runge Kuta 4 N=10000 FORTRAN Compilation time: .460092000 seconds
#Runge Kuta 4 N=10000 FORTRAN Execution time: .325523000 seconds



# Execution time Second-Order Runge-Kutta PYTHON Method N= 100 for dx/dt = -x^3 + sin(t): 0.032223 seconds
# Execution time Fourth-Order Runge-Kutta PYTHON Method N= 100 for dx/dt = -x^3 + sin(t): 0.005672 seconds


####### Question 5 ################################################################################################



# The command 'chmod +x myfile.py' changes the file permissions of myfile.py 
# to make it executable. This allows the Python script to be run directly 
# from the terminal using ./myfile.py, rather than calling it with the Python 
# interpreter explicitly. For this to work properly, the script typically needs 
# a hashbang or shebang or whatever it is called line at the top (such as #!/usr/bin/env python3) 
# that tells the system which interpreter to use. In contrast, we don’t need to do this for Fortran 
# because Fortran code is compiled into a separate executable file (like RK4.exe) 
# using a compiler such as gfortran. Once compiled, the resulting executable can be 
# run directly, and it's the compiled file—not the original .f90 source code—that needs 
# to be executed. Therefore, there’s no need to change the permissions of the Fortran source file.

