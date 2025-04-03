#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             Class Work
###				Nikiphoros Vlastos
###             
#				April 3, 2025
###########################################


######### starting with double_pendulum_template.py (from Dr. Joyce) ##################
## Excercise 8.15 from the book


import numpy as np

# Constants
g = 9.81  # Gravity (m/s^2)
l = 0.40   # Length of pendulum arms (m)
m = 1   # Mass of pendulums (kg)

# Initial conditions
theta1 = np.radians(90)
theta2 = np.radians(90)
omega1 = 0.0
omega2 = 0.0
# State vector r = [theta1, theta2, omega1, omega2]
r0 = np.array([theta1, theta2, omega1, omega2])  

# Time parameters
dt = 0.01  # Time step
t_max = 5  # Simulation duration: sets number of TIME STEPS
t = np.arange(0, t_max, dt)

# Equations of motion for the double pendulum
def equations(r):
    ## assign the four variables we need to evolve to ONE vector r 
    ## that holds them all
    theta1, theta2, omega1, omega2 = r
    delta_theta = theta2 - theta1

    # Define the four equations for the system
    ftheta1 = omega1
    ftheta2 = omega2

    ## HINT: the expressions for fomega1, fomega2 are quite long,
    ## so create smaller expressions to hold the denominators
    denom1 = 3-np.cos(2*theta1-2*theta2) #ASK DR. JOYCE
    denom2 = 3-np.cos(2*theta1-2*theta2) #ASK DR. JOYCE

    fomega1 = (-(omega1**2)*np.sin(2*theta1 - 2*theta2) + 2*(omega2**2)*np.sin(theta1-theta2) + (g/l) *(np.sin(theta1-2*theta2)+3*np.sin(theta1))) / denom1

    fomega2 = (4*(omega1**2)*np.sin(theta1 - theta2) + 2*(omega2**2)*np.sin(2*theta1-2*theta2) + 2*(g/l) *(np.sin(2*theta1-theta2)-np.sin(theta2))) / denom2

    return np.array([ftheta1, ftheta2, fomega1, fomega2])

# Runge-Kutta 4th order method
def rk4_step(r, dt):
    k1 = dt * equations(r)
    k2 = dt * equations(r + 0.5 * k1) #equations(r + 0.5 * dt * k1)
    k3 = dt * equations(r + 0.5 * k2) #equations(r + 0.5 * dt * k2)
    k4 = dt * equations(r + k3) #equations(r + dt * k3)
    return r + (k1 + 2 * k2 + 2 * k3 + k4) / 6

## this is a CLEVER way to hold all of your data in one object
## R is a vector of lenght t (time steps) that will hold the evolution
## of all FOUR of your variables
## r0 is a VECTOR initialized to r0 = [0,0,0,0]
R = np.zeros((len(t), 4))
R[0] = r0

# Integrate equations and save data
## remember: numerical integration --> for loop
for i in range(1, len(t)):
    R[i] = rk4_step(R[i - 1], dt)

# Extract angles and angular velocities
theta1_vals, theta2_vals, omega1_vals, omega2_vals = R.T

# Convert to Cartesian coordinates for visualization
x1 = l * np.sin(theta1_vals)
y1 = -l * np.cos(theta1_vals)
x2 = x1 + l * np.sin(theta2_vals)
y2 = y1 - l * np.cos(theta2_vals)

# Save data
np.savetxt("double_pendulum_data.txt", np.column_stack([t, x1, y1, x2, y2]),
           header="time x1 y1 x2 y2", comments="")