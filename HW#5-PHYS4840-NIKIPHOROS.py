#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             Homework #5
###				Nikiphoros Vlastos
###             
#				April 3, 2025
###########################################


################## IN CLASS WORK (QUESTION 0) ##############################

# My code for FORTRAN RUNGE KUTA can be found in RK2.f90 and RK4.f90

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

#TIMING RESULTS:






################## QUESTION 1 ######################################################################################################################################################

import numpy as np
import matplotlib.pyplot as plt

def square_wave(t):
    """Generates a square wave with frequency 1 and amplitude 1."""
    return 1 if int(2 * t) % 2 == 0 else -1

def low_pass_filter(V_out, t, RC):
    """Defines the differential equation for the low-pass filter."""
    V_in = square_wave(t)
    return (V_in - V_out) / RC

def rk4_method(f, x0, t0, t_end, dt, RC):
    """Fourth-order Runge-Kutta method for solving ODEs."""
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
#a different type of filtering effect. The capacitor is charging and discharging at a rate that prevents 
#it from fully reaching the input voltage before the signal switches. As a result, the waveform becomes 
#more linear, resembling a sawtooth or triangular wave.
#Overall, the circuit acts as a low-pass filter, but the effect depends strongly on RC. 
#For small RC, the output retains the shape of the input signal with minor smoothing. As RC increases, 
#the circuit increasingly suppresses high-frequency components, transitioning from rounded 
#smoothing to a more linear, ramp-like behavior.







################## QUESTION 2 ######################################################################################################################################################






import numpy as np
import matplotlib.pyplot as plt
import time

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
    return -x**3 + np.sin(t)  # Updated differential equation: dx/dt = -x^3 + sin(t)

# Initial conditions
x0 = 1.0  # Given initial condition x = 1 at t = 0
t0 = 0
t_end_values = [10, 10000]  # Intervals [0, 10] and [0, 10000]
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
plt.title("Second-Order Runge-Kutta PYTHON Method for dx/dt = -x^3 + sin(t)")
plt.grid(True)
plt.legend()
plt.show()

# Print execution time
print(f"Execution time: {execution_time:.6f} seconds")

#######THIS IS RK4 ################

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
    return -x**3 + np.sin(t)  # Updated differential equation: dx/dt = -x^3 + sin(t)

# Initial conditions
x0 = 1.0  # Initial condition x = 1 at t = 0
t0 = 0
t_end_values = [10, 10000]  # Intervals [0, 10] and [0, 10000]
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
plt.title("Fourth-Order Runge-Kutta PYTHON Method for dx/dt = -x^3 + sin(t)")
plt.grid(True)
plt.legend()
plt.show()

print(f"Execution time: {execution_time1:.6f} seconds")



# PLOTTING ALL

import numpy as np
import matplotlib.pyplot as plt

# Load the data from the Fortran output files
# Ensure that the file paths are correct (adjust if needed)
rk2_data = np.loadtxt('rk2_resultsHW.dat', skiprows=1)  # Skip the first line (headers)
rk4_data = np.loadtxt('rk4_resultsHW.dat', skiprows=1)

# Extract t and x values for RK2 and RK4
t_rk2, x_rk2 = rk2_data[:, 0], rk2_data[:, 1]
t_rk4, x_rk4 = rk4_data[:, 0], rk4_data[:, 1]

# Create the plot
plt.figure(figsize=(8, 5))

# Plot RK2 and RK4 results
plt.plot(t_rk2, x_rk2, label="RK2 Method (Fortran)", color='b')  # Blue line for RK2 (Python)
plt.plot(t_rk4, x_rk4, label="RK4 Method (Fortran)", color='r', linestyle='--')  # Red line for RK4 (Python)




#plt.plot(t_values_1, x_values_1, label="RK2 Method (python)", color='g', linestyle='--')  # Green dashed line for RK2 (Fortran)
#plt.plot(t_values_2, x_values_1, label="RK4 Method (Python)", color='orange', linestyle='--')  # Orange dashed line for RK4 (Fortran)

# Add labels and title
plt.xlim(0, 10)
plt.xlabel("Time (t)")
plt.ylabel("Solution x(t)")
plt.title("Comparison of RK2 and RK4 Methods")

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

