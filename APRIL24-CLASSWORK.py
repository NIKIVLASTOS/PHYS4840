#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             APRIL 24
###				Nikiphoros Vlastos
###             
#				Spectral methods, Gaussian sampling, Pseudo-random processes
###########################################



# Spectral Methods

# 	AKA Fourier Transform
# 	AKA Spectral Decomposition

# 	Break the Problem into sine and cosines



#####################################
#
# This is the code from Fourier_explicit.py (From Dr. Joyce's GitHub)
# 
#####################################

import numpy as np
import matplotlib.pyplot as plt

# Domain setup
N = 1000  
x = np.linspace(-np.pi, np.pi, N, endpoint=False)
f = np.cos(x)  # Function to integrate

# Manual computation of Fourier coefficients: f-hat
def manual_fourier_coeffs(f, x):
    N = len(x)
    dx = x[1] - x[0]
    L = N * dx  # Total domain length

    # Manually construct frequency indices k
    # Assume domain is periodic over [0, L)
    k = np.zeros(N)
    for n in range(N):
        if n <= N // 2:
            k[n] = n
        else:
            k[n] = n - N
    k = (2 * np.pi / L) * k  # Convert to angular frequencies

    # Compute Fourier coefficients manually
    fhats = np.zeros(N, dtype=complex)
    for n in range(N):
        exponent = -1j * k[n] * x
        fhats[n] = (1 / N) * np.sum(f * np.exp(exponent))

    return k, fhats


k, fk = manual_fourier_coeffs(f, x)

for i in range(len(k)):
    print("coeff number", i,\
          "    Fourier wave number k:", int(k[i]),\
          "    Fourier coefficient fk:", fk[i])

# Integrate: divide by i*k (except at k=0)
Fk = np.zeros_like(fk) ## populate an object the shape of fk with zeros 
nonzero = k != 0 # the set 'nonzero' is defined as those for which k != 0 (slicker version of np.where() )
Fk[nonzero] = fk[nonzero] / (1j * k[nonzero]) # perform the integration, AKA division in Fourier, for k[nonzero]
Fk[~nonzero] = 0.0  # ~nonzero means "not nonzero," so we are separating the 0-entry of FK out 
                    # and setting it to zero so as not to enounter a divide-by-zero error

# Reconstruct integrated function
f_integrated = np.real(np.sum([Fk[n] * np.exp(1j * k[n] * x) for n in range(N)], axis=0))

# Plot
x_array_for_sin = np.linspace(-np.pi, np.pi, 10000)

plt.plot(x_array_for_sin, np.sin(x_array_for_sin), '-', linewidth=1, color='black', label='True sin(x)')
plt.plot(x, f_integrated, "go-", linewidth=2, markersize=10, alpha=0.6, label='Integrated cos(x)')

plt.legend()
plt.title("Spectral Integration via Manual Fourier Series")
plt.grid(True)
plt.show()


#####################################
#
# This is from use_FFT.pt (From Dr. Joyce's GitHub)
# 
#
#####################################

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Set up the domain and function
N = 1000                             
L = 2 * np.pi                      # Domain length [-π, π]
x = np.linspace(-np.pi, np.pi, N, endpoint=False)  # Grid points
f = np.cos(x)                      # Function to integrate

# Step 2: Compute the FFT of the function (go to frequency space)
f_hat = np.fft.fft(f)              # Fourier coefficients (complex)

# Step 3: Build the frequency array
k = np.fft.fftfreq(N, d=L/N)       # Frequencies in cycles per unit length
k = 2 * np.pi * k                  # Convert to angular frequencies (radians)

# Step 4: Integrate in Fourier space by dividing by ik
F_hat = np.zeros(N, dtype=complex) # Initialize integrated coefficients

for i in range(N):
    if k[i] != 0:
        F_hat[i] = f_hat[i] / (1j * k[i])
    else:
        F_hat[i] = 0  # No contribution from the DC component (mean value)

# Step 5: Inverse FFT to return to real space
f_integrated = np.fft.ifft(F_hat).real  # Take the real part

# Plot results
x_array_for_sin = np.linspace(-np.pi, np.pi, 10000)

plt.plot(x_array_for_sin, np.sin(x_array_for_sin), '-', linewidth=1, color='black', label='True sin(x)')
plt.plot(x, f_integrated, "ro-", linewidth=2, markersize=10, alpha=0.6, label='Integrated cos(x)')

plt.legend()
plt.title("Spectral Integration using NumPy FFT")
plt.grid(True)
plt.show()



############################################## IN CLASS EXCERCISE ############################################################################################


#Q1: 
# Obviosuly the imports are the same 
# For the Manual when the domain is being set up there is only a "N", "x", "f". While the using numpy we also set a 'L' (domain length)

# For the manual we set the length in the manual_fourier_coeffs section by setting "L = N * dx"


#Q2
# I think once you get close to 20 basis functions you get a relatively smooth curve (as soon from unzoomed plot), 
# and once you get to 100 basis functions you need to zoom significantly in to see the deviation from the actualy 
# bent function between two of the function. Once you get to 100 as well, the time it takes for the manual version is appreciably longer
# This is still only a second or so for the manual one, but is still noticeably longer than the NumPy one. 
# As you increase to N=1000 the difference between manual and NumPy version increase more




# PSUEDO-RANDOM NUMBER GENERATION (PRNG)

# Random Stuff: Decay, Quantum stuff, Brownian motion



############################################# Mini In Class Excercise ##########################################################################################


#####################################
#
# From psuedo_rand_demo.py (From Dr. Joyce's GitHub)
#
#####################################

import numpy as np

seed = 15

# Mersenne Twister (default legacy)
rng1 = np.random.default_rng(np.random.MT19937(seed))
print("Mersenne Twister:", rng1.random(1))

# PCG64 (NumPy default)
rng2 = np.random.default_rng(seed)
print("PCG64:", rng2.random(1))

# Philox (counter-based PRNG, parallel-safe)
rng3 = np.random.Generator(np.random.Philox(seed))
print("Philox:", rng3.random(1))

# SFC64 (good for speed and statistical quality)
rng4 = np.random.Generator(np.random.SFC64(seed))
print("SFC64:", rng4.random(1))



# Q3: Well they clearly only change when you change the seed. 


# The period, or length before repetition, of the MT19937 sequence is 2^19937. 
# PCG-64 has a period of 2^128



####################### Gaussian Random Numbers #####################################################################

##### Next Inclass Excercies #####################################################################

#####################################
#
# This is from the rutherford.py (From Dr. Joyce's GitHub)
#
#####################################
import time 

from math import sqrt,log,cos,sin,pi # Importing math functions from the math library
from random import random #importing random from the random library

Z = 79 # Atomic number of gold (used in Rutherford scattering)
e = 1.602e-19 # base charge
E = 7.7e6*e # Kinetic energy of incident alpha particles in Joules
epsilon0 = 8.854e-12 # Vacuum permittivity in F/m
a0 = 5.292e-11
sigma = a0/100 # Width of Gaussian , much smaller than Bohr radius

N = int(1e7) # This is the number of particles

# Function to generate a random (x,y) point using a 2D Gaussian 
def gaussian():
    r = sqrt(-2*sigma*sigma*log(1-random()))
    theta = 2*pi*random()
    # Convert from polar to Cartesian coordinates
    x = r*cos(theta)
    y = r*sin(theta)
    return x,y

start_time = time.time()

count = 0
for i in range(N):
    x,y = gaussian()
    b = sqrt(x*x+y*y)
       # Check if the particle is reflected based on Coulomb potential threshold
    # Condition derived from classical Rutherford scattering cross-section
    if b<Z*e*e/(2*pi*epsilon0*E):
        count += 1

end_time = time.time()
execution_time = end_time - start_time

print(count,"particles were reflected out of",N)
print(f"Execution time: {execution_time:.6f} seconds")

# The Fortran code is in the file "oddball.f90" in my directory

# Execution time for Python for 1000000 is 0.777801 seconds

