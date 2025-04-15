#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             HOMEWORK #6
###				Nikiphoros Vlastos
###             
#				
###########################################

# I usually write the code in seperate files and then once it is running copy it into 
# this file for the HW submission, so sometimes I am re importing certain things multipl times like numpy as 
# np I think I removed all duplicates but who knows

# Also, as you requested I uploaded all my code to here but originial code is found in: ft_demo.py, ft_timing.py and fourier_transform.py

################################# Question 0 #######################################################################

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

# RK4 Integration
def rk4_step(r, dt):
    k1 = dt * equations(r)
    k2 = dt * equations(r + 0.5 * k1)
    k3 = dt * equations(r + 0.5 * k2)
    k4 = dt * equations(r + k3)
    return r + (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Simulate given initial conditions
def simulate(theta1_deg, theta2_deg, omega1, omega2):
    r0 = np.radians([theta1_deg, theta2_deg])  # Convert the angles to radians
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

# Simulate three runs with small perturbations (I changed the starting angles here)
run1 = simulate(90, 90, 0, 0) # Both start at 90 deg
run2 = simulate(90.5, 90, 0, 0) #change the first angle to start at 90.5
run3 = simulate(90, 90.5, 0, 0) #change the second angle to start at 90.5

# Calculate separation between Run 1 and others, I didnt really know 
# how to show chaos so I decided to try and plot the difference between the three runs
# e.g. like difference between 1 and 2 and then 1 and 3
dist12 = np.sqrt((run1[2] - run2[2])**2 + (run1[3] - run2[3])**2)
dist13 = np.sqrt((run1[2] - run3[2])**2 + (run1[3] - run3[3])**2)

# Plot, again I am assuming this can be used as what Dr. Joyce meant by showing a 'chaos indicator'
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


# Animation make: This makes the three animations and puts them next to eachother so the 'chaos' of them compared to one another can be observed.
# Hopefully one of these two ways is suffecient to show the 'chaos'
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
titles = ["Run 1: (90°, 90°)", "Run 2: (90.5°, 90°)", "Run 3: (90°, 90.5°)"] # obviously this is labels for the three plots
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

def update(frame): #update the frame so there can be movement (e.g. actual animation of it)
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

# This will save  the animation if I want, I have it hashtagged out at the moment
# ani.save("double_pendulum_comparison.gif", writer="pillow", fps=60)



################################# Question 1 #######################################################################

# My April 8th Code can be foud in: APRIL8-CLASSWORK.py but I have uploaded it below as well

# This is the Code from Dr. Miller 'fs_demo.py'

"""
Simple Fourier Series Demonstration
----------------------------------
This script demonstrates Fourier series approximation with a fixed number of terms,
generating four key visualizations:
1. Series plot with terms set
2. PSD with only terms set
3. Convergence and error up to the terms set
4. Animation showing only terms set

PHYS 4840 - Mathematical and Computational Methods II
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import fourier_series as fs


def do_fourier(TERMS, wave):


    # Create x values for plotting
    x_range = (-2*np.pi, 2*np.pi)
    num_points = 10000
    x = np.linspace(x_range[0], x_range[1], num_points)
    y_exact = wave(x)
    


    # Compute Fourier series coefficients
    a0 , an , bn  = fs.compute_coefficients(wave, TERMS) 
 	  

    # Calculate the Fourier approximation
    y_approx = fs.fourier_series_approximation(x, a0, an, bn)
	

    # Calculate partial approximations
    partial_approx = fs.compute_partial_approximations(x, a0, an, bn)

    errors = []
    times = []
    cumulative_times = []

    term_counts = range(1, TERMS + 1)
    total_time = 0

    for i, approx in enumerate(partial_approx):
        start = time.perf_counter()
        error = np.sqrt(np.mean((y_exact - approx)**2))
        end = time.perf_counter()

        change_time = end - start
        total_time += change_time

        errors.append(error)
        times.append(change_time)
        cumulative_times.append(total_time)


	


    # 1. Plot the series with TERMS set
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_exact, 'k-', label='Exact')
    plt.plot(x, y_approx, 'r-', label=f'Fourier ({TERMS} terms)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()#plt.savefig('fourier_approximation.png')
    plt.close()
    




    # 2. Plot the power spectral density (PSD) / coefficient spectrum
    plt.figure(figsize=(10, 6))
    
    # Compute magnitude of coefficients
    n_values = np.arange(1, TERMS + 1)
    
    # Plot coefficient magnitudes
    plt.stem(n_values, an, 'g-', markerfmt='g^', label='an', basefmt=" ", linefmt='g--')
    plt.stem(n_values, bn, 'r-', markerfmt='rs', label='bn', basefmt=" ", linefmt='r--')
    
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xlabel('Harmonic (n)')
    plt.ylabel('Coefficient Magnitude')
    plt.yscale('log')
    plt.show()#plt.savefig('coefficient_spectrum.png')
    plt.close()
    




    # 3. Convergence and error analysis
    # Calculate error for each partial approximation
    errors = []
    term_counts = range(1, TERMS + 1)
    
    for i, approx in enumerate(partial_approx):
        error = np.sqrt(np.mean((y_exact - approx)**2))
        errors.append(error)
    
    plt.figure(figsize=(10, 6))
    plt.plot(term_counts, errors, 'bo-')
    plt.grid(True, alpha=0.3)
    plt.xlabel('Number of Terms')
    plt.ylabel('RMS Error')
    plt.show()#plt.savefig('convergence_rate_linear.png')
    plt.close()
    
    # Log-log plot to better visualize error scaling
    plt.figure(figsize=(10, 6))
    plt.loglog(term_counts, errors, 'bo-')
    plt.grid(True, alpha=0.3, which='both')
    plt.xlabel('Number of Terms')
    plt.ylabel('RMS Error')
    plt.show()#plt.savefig('convergence_rate_log.png')
    plt.close()
    




    # 4. Create an animation showing how the approximation improves with terms
    fig, ax = plt.subplots(figsize=(10, 6))
    
    exact_line, = ax.plot(x, y_exact, 'k-', label='Exact')
    approx_line, = ax.plot([], [], 'r-', label='Fourier Approximation')
    
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    # Set axis limits
    margin = 0.1
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlim(x_range)
    
    # Text to display current number of terms
    terms_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    
    def init():
        """Initialize animation"""
        approx_line.set_data([], [])
        terms_text.set_text('')
        return approx_line, terms_text
    
    def update(frame):
        """Update animation for each frame"""
        n_terms = frame + 1
        # Use pre-computed partial approximation
        y_approx = partial_approx[n_terms - 1]
        
        approx_line.set_data(x, y_approx)
        terms_text.set_text(f'Terms: {n_terms}')
        return approx_line, terms_text
    
    ani = FuncAnimation(fig, update, frames=TERMS,
                       init_func=init, blit=True, interval=200)
    
    plt.show()
    ani.save('fourier_animation.gif', writer='pillow', fps=5)
    plt.close()

    # Plot time per term vs RMS error
    plt.figure(figsize=(10, 6))
    plt.plot(term_counts, times, 'r-', label='Time per term')
    plt.xlabel('Number of Terms')
    plt.ylabel('Time per Term (seconds)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    plt.close()


    # Error vs Cumulative Time
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_times, errors, 'ms-', label='RMS Error vs Time')
    plt.grid(True, alpha=0.3)
    plt.xlabel('Cumulative Time (seconds)')
    plt.ylabel('RMS Error')
    plt.title('Fourier Approximation Error vs. Time')
    plt.legend()
    plt.show()
    plt.close()

    #Log-log version
    plt.figure(figsize=(10, 6))
    plt.loglog(cumulative_times, errors, 'ms-')
    plt.grid(True, alpha=0.3, which='both')
    plt.xlabel('Cumulative Time (seconds)')
    plt.ylabel('RMS Error')
    plt.title('Log-Log: Error vs. Cumulative Time')
    plt.show()
    plt.close()

    # Error vs. Number of Terms
    plt.figure(figsize=(10, 6))
    plt.plot(term_counts, errors, 'ms-')
    plt.grid(True, alpha=0.3, which='both')
    plt.xlabel('Cumulative Time (seconds)')
    plt.ylabel('RMS Error')
    plt.title('Error vs. Number of Terms')
    plt.show()
    plt.close()


    




#some example wave forms, I encourage you to make your own :)

def square_wave(x):
    """Square wave: 1 for 0 <= x < pi, -1 for pi <= x < 2pi"""
    return np.where((x % (2*np.pi)) < np.pi, 1.0, -1.0)


def sawtooth_wave(x):
    """Sawtooth wave: from -1 to 1 over 2pi period"""
    return (x % (2*np.pi)) / np.pi - 1


def triangle_wave(x):
    """Triangle wave with period 2pi"""
    # Normalize to [0, 2pi]
    x_norm = x % (2*np.pi)
    # For 0 to pi, goes from 0 to 1
    # For pi to 2pi, goes from 1 to 0
    return np.where(x_norm < np.pi, 
                   x_norm / np.pi, 
                   2 - x_norm / np.pi)


def pulse_train(x):
    """Pulse train: 1 for small interval, 0 elsewhere"""
    x_norm = x % (2*np.pi)
    pulse_width = np.pi / 8  # Very narrow pulse
    return np.where(x_norm < pulse_width, 1.0, 0.0)


def half_rectified_sine(x):
    """Half-rectified sine wave: max(0, sin(x))"""
    return np.maximum(0, np.sin(x))


def ecg_like_signal(x):

    def r(val, variation=0.1):
        return val * np.random.uniform(1 - variation, 1 + variation)

    # Normalize x to [0, 2pi]
    x_norm = x % (2 * np.pi)
    # P-wave with randomized amplitude, center, and width
    p_wave = r(0.25, 0.2) * np.exp(-((x_norm - r(0.7 * np.pi, 0.05))**2) / (r(0.1 * np.pi, 0.05)**2))
    # QRS complex: one positive peak and two negative deflections
    qrs1 = r(1.0, 0.2) * np.exp(-((x_norm - r(np.pi, 0.05))**2) / (r(0.05 * np.pi, 0.05)**2))
    qrs2 = r(-0.3, 0.2) * np.exp(-((x_norm - r(0.9 * np.pi, 0.05))**2) / (r(0.04 * np.pi, 0.05)**2))
    qrs3 = r(-0.2, 0.2) * np.exp(-((x_norm - r(1.1 * np.pi, 0.05))**2) / (r(0.04 * np.pi, 0.05)**2))
    # T-wave with random parameters
    t_wave = r(0.5, 0.2) * np.exp(-((x_norm - r(1.4 * np.pi, 0.05))**2) / (r(0.1 * np.pi, 0.05)**2))
    
    return p_wave + qrs1 + qrs2 + qrs3 + t_wave

def my_signal(x):
    return half_rectified_sine(np.sin(x) * np.cos(np.sin(10 * x)))

def Niki_waveform1(x):
    return (x % (30*np.pi)) / np.pi - 1

def Niki_waveform2(x):
    return (x % (3*np.pi)) / np.pi


import time

def main():
    TERMS = 100
    wave = my_signal

    start_time = time.perf_counter()
    do_fourier(TERMS, wave)
    end_time = time.perf_counter()

    total_time = end_time - start_time
    print(f"\nTotal time for Fourier processing with {TERMS} terms: {total_time:.6f} seconds\n")




if __name__ == "__main__":
    main()



# My April 10th Code can be foud in: APRIL10-CLASSWORK.py Which in turn the most of the code is in 
# ft_demo.py (this is primarily the Code Dr. Miller gave us with some of my edits) and ft_timing.py (This is the timing of different methods and my plot comparing them)
# you can run each of the codes invdividually to get the plots that Dr. Miller had us work on. I went into his office to check I had the plots done in a way in that at least his quick glance over looked good
# The ft-demo.py is primarily in the above code, the ft_timing is for this code below as well as fourier_transform.py



################################################### taken from ft_timing.py I have obviously made changes to the code but some is what Dr. Miller gave us ###################################################
import numpy as np
import time
import matplotlib.pyplot as plt
import fourier_transform as ft

def compare_speeds():
    sizes = [2,4,6,8,16, 32, 64, 128, 256, 512, 1024]
    times_dft = []
    times_radix2 = []
    times_bluestein = []
    times_zeropad = []
    times_numpy = []


    for N in sizes:
        x = np.random.rand(N)

        # Naive DFT
        try:
            start = time.time()
            ft.dft(x)
            end = time.time()
            times_dft.append(end - start)
        except Exception as e:
            times_dft.append(np.nan)

        # Radix-2 FFT (only works for powers of 2)
        try:
            start = time.time()
            ft.fft_radix2(x)
            end = time.time()
            times_radix2.append(end - start)
        except Exception:
            times_radix2.append(np.nan)

        # Bluestein FFT (for any size)
        try:
            start = time.time()
            ft.fft_bluestein(x)
            end = time.time()
            times_bluestein.append(end - start)
        except Exception:
            times_bluestein.append(np.nan)

        # Zero-padded FFT (next power of 2)
        try:
            start = time.time()
            ft.fft_zeropad(x)
            end = time.time()
            times_zeropad.append(end - start)
        except Exception:
            times_zeropad.append(np.nan)

        # Numpy FFT
        try:
            start = time.time()
            np.fft.fft(x)
            end = time.time()
            times_numpy.append(end - start)
        except Exception:
            times_numpy.append(np.nan)

    # Plot the timing results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_dft, label="Naive DFT", marker='o')
    plt.plot(sizes, times_radix2, label="Radix-2 FFT", marker='o')
    plt.plot(sizes, times_bluestein, label="Bluestein FFT", marker='o')
    plt.plot(sizes, times_zeropad, label="Zero-padded FFT", marker='o')
    plt.plot(sizes, times_numpy, label="NumPy FFT", marker='o')

    plt.xlabel("Signal size (N)")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time of Fourier Transform Methods")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    compare_speeds()

################################################### taken from fourier_transform.py (this is also used in question #3 but imported as seen in the code) I have obviously made changes to the code but some is what Dr. Miller gave us ###################################################



################################# Question 2 #######################################################################

# Constants again
g = 9.81  # it is always in m/s^2 or atleast on earth we use that value
l = 0.4   # in m as the question said
m = 1     # in kg here

# Initial conditions agan
theta1_0 = np.radians(90)
theta2_0 = np.radians(90)
omega1_0 = 0
omega2_0 = 0

# Time parameters
t_final = 10  # 10 seconds
dt = 0.1
dt_min = 0.00001
tolerance = 1e-5

# Equations of motion
def theta1_dot(omega1): return omega1
def theta2_dot(omega2): return omega2

def omega1_dot(theta1, theta2, omega1, omega2, g, l):
    num = (omega1**2 * np.sin(2*theta1 - 2*theta2) + 
           2 * omega2**2 * np.sin(theta1 - theta2) + 
           (g/l) * (np.sin(theta1 - 2*theta2) + 3*np.sin(theta1)))
    den = 3 - np.cos(2*theta1 - 2*theta2)
    return -num / den

def omega2_dot(theta1, theta2, omega1, omega2, g, l):
    num = (4 * omega1**2 * np.sin(theta1 - theta2) + 
           omega2**2 * np.sin(2*theta1 - 2*theta2) + 
           2 * (g/l) * (np.sin(2*theta1 - theta2) - np.sin(theta2)))
    den = 3 - np.cos(2*theta1 - 2*theta2)
    return num / den

# Calculate the Energy of the sysem
def total_energy(theta1, theta2, omega1, omega2, m, g, l):
    T = m * l**2 * (omega1**2 + 0.5 * omega2**2 + omega1 * omega2 * np.cos(theta1 - theta2))
    V = -m * g * l * (2 * np.cos(theta1) + np.cos(theta2))
    return T + V

# RK4 integrator for all the thetas
def runge_kutta4(theta1, theta2, omega1, omega2, dt, g, l):
    k1_theta1 = theta1_dot(omega1)
    k1_theta2 = theta2_dot(omega2)
    k1_omega1 = omega1_dot(theta1, theta2, omega1, omega2, g, l)
    k1_omega2 = omega2_dot(theta1, theta2, omega1, omega2, g, l)

    k2_theta1 = theta1_dot(omega1 + 0.5 * dt * k1_omega1)
    k2_theta2 = theta2_dot(omega2 + 0.5 * dt * k1_omega2)
    k2_omega1 = omega1_dot(theta1 + 0.5 * dt * k1_theta1, theta2 + 0.5 * dt * k1_theta2, 
                           omega1 + 0.5 * dt * k1_omega1, omega2 + 0.5 * dt * k1_omega2, g, l)
    k2_omega2 = omega2_dot(theta1 + 0.5 * dt * k1_theta1, theta2 + 0.5 * dt * k1_theta2, 
                           omega1 + 0.5 * dt * k1_omega1, omega2 + 0.5 * dt * k1_omega2, g, l)

    k3_theta1 = theta1_dot(omega1 + 0.5 * dt * k2_omega1)
    k3_theta2 = theta2_dot(omega2 + 0.5 * dt * k2_omega2)
    k3_omega1 = omega1_dot(theta1 + 0.5 * dt * k2_theta1, theta2 + 0.5 * dt * k2_theta2,
                           omega1 + 0.5 * dt * k2_omega1, omega2 + 0.5 * dt * k2_omega2, g, l)
    k3_omega2 = omega2_dot(theta1 + 0.5 * dt * k2_theta1, theta2 + 0.5 * dt * k2_theta2, 
                           omega1 + 0.5 * dt * k2_omega1, omega2 + 0.5 * dt * k2_omega2, g, l)

    k4_theta1 = theta1_dot(omega1 + dt * k3_omega1)
    k4_theta2 = theta2_dot(omega2 + dt * k3_omega2)
    k4_omega1 = omega1_dot(theta1 + dt * k3_theta1, theta2 + dt * k3_theta2, 
                           omega1 + dt * k3_omega1, omega2 + dt * k3_omega2, g, l)
    k4_omega2 = omega2_dot(theta1 + dt * k3_theta1, theta2 + dt * k3_theta2, 
                           omega1 + dt * k3_omega1, omega2 + dt * k3_omega2, g, l)

    theta1_new = theta1 + (dt / 6) * (k1_theta1 + 2*k2_theta1 + 2*k3_theta1 + k4_theta1)
    theta2_new = theta2 + (dt / 6) * (k1_theta2 + 2*k2_theta2 + 2*k3_theta2 + k4_theta2)
    omega1_new = omega1 + (dt / 6) * (k1_omega1 + 2*k2_omega1 + 2*k3_omega1 + k4_omega1)
    omega2_new = omega2 + (dt / 6) * (k1_omega2 + 2*k2_omega2 + 2*k3_omega2 + k4_omega2)

    return theta1_new, theta2_new, omega1_new, omega2_new

# making a simulation loop (for the RK44)
time = [0]
theta1_values = [theta1_0]
theta2_values = [theta2_0]
omega1_values = [omega1_0]
omega2_values = [omega2_0]
energy_values = [total_energy(theta1_0, theta2_0, omega1_0, omega2_0, m, g, l)]

t = 0
while t < t_final:
    theta1, theta2, omega1, omega2 = runge_kutta4(theta1_values[-1], theta2_values[-1], 
                                                  omega1_values[-1], omega2_values[-1], dt, g, l)
    energy_new = total_energy(theta1, theta2, omega1, omega2, m, g, l)
    energy_variation = np.abs(energy_new - energy_values[-1])
    
    if energy_variation < tolerance: #just append values to each of the variables as long as the energy variation is bigger than the tolerance I set up above
        t += dt
        time.append(t)
        theta1_values.append(theta1)
        theta2_values.append(theta2)
        omega1_values.append(omega1)
        omega2_values.append(omega2)
        energy_values.append(energy_new)
    else:
        dt /= 2
        if dt < dt_min:
            print("Minimum dt reached. Exiting.")
            break
        print(f"Energy variation too high. Reducing dt to {dt:.6f} at t = {t:.4f}")

# Plot total energy vs. time
plt.plot(time, energy_values, color='blue')
plt.xlabel("Time (s)")
plt.ylabel("Total Energy (J)")
plt.title("Total Energy vs. Time (Adaptive RK4)")
plt.grid(True)
plt.tight_layout()
plt.show()


################################################ PART C


# Constants again again x2
g = 9.81  # m/s^2
l = 0.4   # m
m = 1     # kg

# Initial conditions
theta1_0 = np.radians(90)
theta2_0 = np.radians(90)
omega1_0 = 0
omega2_0 = 0

# Time parameters
t_final = 10  # in seconds
dt = 0.1

# Equations of motion
def theta1_dot(omega1): return omega1
def theta2_dot(omega2): return omega2

def omega1_dot(theta1, theta2, omega1, omega2, g, l):
    num = (omega1**2 * np.sin(2*theta1 - 2*theta2) + 
           2 * omega2**2 * np.sin(theta1 - theta2) + 
           (g/l) * (np.sin(theta1 - 2*theta2) + 3*np.sin(theta1)))
    den = 3 - np.cos(2*theta1 - 2*theta2)
    return -num / den

def omega2_dot(theta1, theta2, omega1, omega2, g, l):
    num = (4 * omega1**2 * np.sin(theta1 - theta2) + 
           omega2**2 * np.sin(2*theta1 - 2*theta2) + 
           2 * (g/l) * (np.sin(2*theta1 - theta2) - np.sin(theta2)))
    den = 3 - np.cos(2*theta1 - 2*theta2)
    return num / den

# RK4 integrator
def runge_kutta4(theta1, theta2, omega1, omega2, dt, g, l):
    k1_theta1 = theta1_dot(omega1)
    k1_theta2 = theta2_dot(omega2)
    k1_omega1 = omega1_dot(theta1, theta2, omega1, omega2, g, l)
    k1_omega2 = omega2_dot(theta1, theta2, omega1, omega2, g, l)

    k2_theta1 = theta1_dot(omega1 + 0.5 * dt * k1_omega1)
    k2_theta2 = theta2_dot(omega2 + 0.5 * dt * k1_omega2)
    k2_omega1 = omega1_dot(theta1 + 0.5 * dt * k1_theta1, theta2 + 0.5 * dt * k1_theta2, 
                           omega1 + 0.5 * dt * k1_omega1, omega2 + 0.5 * dt * k1_omega2, g, l)
    k2_omega2 = omega2_dot(theta1 + 0.5 * dt * k1_theta1, theta2 + 0.5 * dt * k1_theta2, 
                           omega1 + 0.5 * dt * k1_omega1, omega2 + 0.5 * dt * k1_omega2, g, l)

    k3_theta1 = theta1_dot(omega1 + 0.5 * dt * k2_omega1)
    k3_theta2 = theta2_dot(omega2 + 0.5 * dt * k2_omega2)
    k3_omega1 = omega1_dot(theta1 + 0.5 * dt * k2_theta1, theta2 + 0.5 * dt * k2_theta2,
                           omega1 + 0.5 * dt * k2_omega1, omega2 + 0.5 * dt * k2_omega2, g, l)
    k3_omega2 = omega2_dot(theta1 + 0.5 * dt * k2_theta1, theta2 + 0.5 * dt * k2_theta2, 
                           omega1 + 0.5 * dt * k2_omega1, omega2 + 0.5 * dt * k2_omega2, g, l)

    k4_theta1 = theta1_dot(omega1 + dt * k3_omega1)
    k4_theta2 = theta2_dot(omega2 + dt * k3_omega2)
    k4_omega1 = omega1_dot(theta1 + dt * k3_theta1, theta2 + dt * k3_theta2, 
                           omega1 + dt * k3_omega1, omega2 + dt * k3_omega2, g, l)
    k4_omega2 = omega2_dot(theta1 + dt * k3_theta1, theta2 + dt * k3_theta2, 
                           omega1 + dt * k3_omega1, omega2 + dt * k3_omega2, g, l)

    theta1_new = theta1 + (dt / 6) * (k1_theta1 + 2*k2_theta1 + 2*k3_theta1 + k4_theta1)
    theta2_new = theta2 + (dt / 6) * (k1_theta2 + 2*k2_theta2 + 2*k3_theta2 + k4_theta2)
    omega1_new = omega1 + (dt / 6) * (k1_omega1 + 2*k2_omega1 + 2*k3_omega1 + k4_omega1)
    omega2_new = omega2 + (dt / 6) * (k1_omega2 + 2*k2_omega2 + 2*k3_omega2 + k4_omega2)

    return theta1_new, theta2_new, omega1_new, omega2_new

# Setup for makinganimation
fig, ax = plt.subplots()
ax.set_xlim(-3* l, 3 * l)  # Set the x-axis limits in a way to fit the pendulums motion
ax.set_ylim(-3 * l, 3 * l)  # Set the y-axis limits in a way to fit the pendulums motion

# Create plot lines for the two pendulums
line1, = ax.plot([], [], 'o-', lw=2)  #  for first pendulum
line2, = ax.plot([], [], 'o-', lw=2)  # for second pendulum
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)  # Text to display the time in animation, I looked this up and someone had a youtube video how to do this

# Initialize the pendulum positions for animation
def init():
    line1.set_data([], [])  # start first pendulum line as empty
    line2.set_data([], [])  # start second pendulum line as empty
    time_text.set_text('')  # start time text as empty
    return line1, line2, time_text  # Return objects so then thay can be updated as animation goes on

# This function should be updating the animation
def update(frame):
    global theta1_0, theta2_0, omega1_0, omega2_0

    # Use RK4 to get new values for theta(1and 2) and omega (1 and 2)
    theta1, theta2, omega1, omega2 = runge_kutta4(theta1_0, theta2_0, omega1_0, omega2_0, dt, g, l)
    # Update initial values for the next frame in the run
    theta1_0, theta2_0, omega1_0, omega2_0 = theta1, theta2, omega1, omega2

    # Now this is Calculating the positions of the pendulum bobs
    x1 = l * np.sin(theta1)  # position of the first bob x
    y1 = -l * np.cos(theta1)  # position of the first bob y
    x2 = x1 + l * np.sin(theta2)  # position of the second bob x
    y2 = y1 - l * np.cos(theta2)  # position of the second bob y

    # next this will update the lines of the pendulum based on the positions calculated just above
    line1.set_data([0, x1], [0, y1])  # first pendulum
    line2.set_data([x1, x2], [y1, y2])  # second 
    time_text.set_text(f'Time = {frame * dt:.2f}s')  # this displays the current time in the animation 

    return line1, line2, time_text  # Return the updated things for the animation

# Create the actual animation
ani = animation.FuncAnimation(fig, update, frames=int(t_final / dt), init_func=init, blit=True, interval=dt * 1000)

# plot the animation, or I guess 'show' the animation
plt.show()






################################# Question 3 #######################################################################

# MOST OF THIS CODE IS TAKEN FROM DR. MILLERS fourier_tranform.py file (posted above in question 1) and it 
# I did make some changes to his code (in the fourier_series.py what I did is mostly at the bottom of the script)

# Also, at least on my computer this part takes a little to finish as in for the plot to pop up, 
# so I added the print statement at the beggining of question 4 so I knew if it was a problem with the code or just taking a while.

# This is my actually calling the fourier_transform.py it to compress a file (I just made a sampe signal and Dr. Miller said that was okay)

# You also have to zoom in on the plots to see clearly to compression of the wav

from fourier_transform import compress_audio_fft

# Generate a test signal (the one I made is just two sine waves)
sample_rate = 4400
duration = 1  # I am just using what would be 1 second as it taked a while to pop up on my computer second
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
signal = np.sin(2 * np.pi * 40 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)

# Add some noise to the signal
signal += 0.2 * np.random.randn(len(signal)) # I looked up how to add noise to a signal

# Compress th signal
compressed_signal, spectrum = compress_audio_fft(signal, keep_ratio=0.05)

# Plot
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Original Noisy Signal")

plt.subplot(2, 1, 2)
plt.plot(t, compressed_signal)
plt.title("Compressed Signal (5% of frequency components)")

plt.tight_layout()
plt.show()







################################# Question 4 #######################################################################

print("Made it to Question 4")

# Astronomical images (well those intended for scientific analysis) should avoid the JPEG format 
# primarily due to its data loss in compression. JPEG compression discards image data to reduce 
# file size, which obviously alters the precise measurements of brightness, position, and color 
# of celestial objects or other astronomical data/'stuff' in the image. For scientific purposes, 
# where accuracy is paramount, researchers need to preserve the original data captured by 
# the telescope. Using lossless formats like FITS (Flexible Image Transport System) or 
# TIFF (I am not totally sure how these work I just looked up lossless formats to see what 
# was out there) ensures that no information is lost, allowing for reliable photometric and astrometric 
# analysis, which are critical for drawing accurate conclusions about the data.





