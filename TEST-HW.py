import numpy as np

# Load GAIA_G.csv
gaia_data = np.loadtxt("GAIA_G.csv", delimiter=",", skiprows=1)
gaia_wavelength = gaia_data[:, 0]  # First column
gaia_flux = gaia_data[:, 1]  # Second column

# Load Vega_SED.csv
vega_data = np.loadtxt("Vega_SED.csv", delimiter=",", skiprows=1)
vega_wavelength = vega_data[:, 0]  # First column
vega_flux = vega_data[:, 1]  # Second column

# Ensure data is sorted (just in case)
gaia_sorted = np.argsort(gaia_wavelength)
gaia_wavelength, gaia_flux = gaia_wavelength[gaia_sorted], gaia_flux[gaia_sorted]

vega_sorted = np.argsort(vega_wavelength)
vega_wavelength, vega_flux = vega_wavelength[vega_sorted], vega_flux[vega_sorted]

# Integration methods
def trapezoidal(y_values, x_values):
    return np.trapz(y_values, x_values)

def simpsons(y_values, x_values):
    if len(x_values) % 2 == 0:  # Simpson's rule requires an odd number of points
        x_values = x_values[:-1]
        y_values = y_values[:-1]
    return np.trapz(y_values, x_values)  # Use trapezoidal as a fallback

def romberg(y_values, x_values):
    from scipy.integrate import romb
    if not (len(x_values) & (len(x_values) - 1)) == 0:
        print("Romberg integration requires a power-of-2 number of intervals.")
        return None
    return romb(y_values, dx=(x_values[1] - x_values[0]))

# Compute integrals
gaia_trap = trapezoidal(gaia_flux, gaia_wavelength)
gaia_simp = simpsons(gaia_flux, gaia_wavelength)
gaia_romb = romberg(gaia_flux, gaia_wavelength)

vega_trap = trapezoidal(vega_flux, vega_wavelength)
vega_simp = simpsons(vega_flux, vega_wavelength)
vega_romb = romberg(vega_flux, vega_wavelength)

# Print results
print("\nGAIA Integration Results:")
print(f"Trapezoidal: {gaia_trap:.6f}")
print(f"Simpson's: {gaia_simp:.6f}")
print(f"Romberg: {gaia_romb if gaia_romb is not None else 'N/A'}")

print("\nVega SED Integration Results:")
print(f"Trapezoidal: {vega_trap:.6f}")
print(f"Simpson's: {vega_simp:.6f}")
print(f"Romberg: {vega_romb if vega_romb is not None else 'N/A'}")














def f(x):
    """Computes the value of the function f(x) = x^2."""
    return x ** 2

def compute_sum(n):
    """Computes the sum s = sum(f(xi)) for i from 1 to n."""
    s = 0
    for i in range(1, n + 1):
        s += f(i)
    return s

# Example usage
n = 10  # You can change this value to compute the sum for different n
result = compute_sum(n)
print(f"The sum s from 1 to {n} of f(x) where f(x) = x^2 is: {result}")














def compute_average(S):
    """Computes the average x bar of the set S."""
    n = len(S)  # Number of elements in S
    if n == 0:
        return 0  # Handle case where S is empty
    total_sum = sum(S)  # Sum of all elements in S
    x_bar = total_sum / n  # Calculate average
    return x_bar

# Example usage
S = [1, 2, 3, 4, 5]  # You can change this list to any group of numbers
average = compute_average(S)
print(f"The average x bar of the set S is: {average}")






def factorial(n):
    """Computes the factorial of n (n!)."""
    if n < 0:
        return "Undefined for negative numbers"  # Factorial is not defined for negative numbers
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by i for each i from 1 to n
    return result

# Example usage
n = 3  # You can change this value to compute the factorial of any non-negative integer
fact = factorial(n)
print(f"The factorial of {n} is: {fact}")














import numpy as np

def f(x):
    """Function to integrate: sin^2(x) / x^2."""
    if x == 0:
        return 1  # Limiting value at x = 0 as the problem said in an if statment
    return (np.sin(x)**2) / (x**2)

def step(x1, x2, f1, f2, delta):
    """Recursive function to integrate using adaptive trapezoidal rule with local extrapolation."""
    xm = 0.5 * (x1 + x2)
    fm = f(xm)
    h = x2 - x1
    
    # Trapezoidal rule estimates
    I1 = 0.5 * h * (f1 + f2)
    I2 = 0.25 * h * (f1 + 2 * fm + f2)
    
    # Error estimate
    error = abs(I2 - I1) / 3.0
    
    # Target accuracy for this slice
    target = h * delta
    
    if error < target:
        # Use Simpson's rule for better accuracy
        return (h / 6) * (f1 + 4 * fm + f2)
    else:
        # Recursively integrate smaller slices
        left = step(x1, xm, f1, fm, delta)
        right = step(xm, x2, fm, f2, delta)
        return left + right

def adaptive_trapezoidal(a, b, epsilon):
    """Computes the integral of f(x) from a to b to within accuracy epsilon."""
    delta = epsilon / (b - a)
    return step(a, b, f(a), f(b), delta)

# Compute the integral from 0 to 10 with accuracy 10^-4
a, b, epsilon = 0, 10, 1e-4
result = adaptive_trapezoidal(a, b, epsilon)
print(f"Computed integral: {result:.6f}")











def trapezoidal(x, y):
    integral = 0.0
    for i in range(len(x) - 1):
        dx = x[i+1] - x[i]
        integral += (y[i] + y[i+1]) * dx / 2
    return integral


def simpsons(x, y):

    N = len(x) - 1

    h = (x[-1] - x[0]) / N
    integral = y[0] + y[-1]
    for i in range(1, N):
        if i % 2 == 1:
            integral += 4 * y[i]
        else:
            integral += 2 * y[i]
    return integral * h / 3


def trapezoidal(x_values, y_values):
    """
    Approximates the integral using trapezoidal rule for given y_values at given x_values.
    
    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        N (int): Number of intervals.

    Returns:
        float: The approximated integral.
    """
    
    N = len(x_values) - 1
    a = x_values[0]
    b = x_values[-1]
    h = (b - a) / N  # Properly calculating h

    integral = (1/2) * (y_values[0] + y_values[-1]) * h  # First and last terms

    for k in range(1, N):
        xk = a + k * h  # Compute x_k explicitly
        yk = np.interp(xk, x_values, y_values)  # Interpolate y at x_k manually in loop
        integral += yk * h

    return integral


def simpsons(x_values, y_values):
    """
    Approximates the integral using Simpson's rule for given y_values at given x_values.

    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        N (int): Number of intervals (must be even).

    Returns:
        float: The approximated integral.
    """

    N = len(x_values) - 1
    a, b = x_values[0], x_values[-1]
    h = (b - a) / N

    integral = y_values[0] + y_values[-1]  # First and last terms

    for k in range(1, N, 2):  # Odd indices (weight 4)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 4 * yk

    for k in range(2, N, 2):  # Even indices (weight 2)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 2 * yk

    return (h / 3) * integral  # Final scaling



def romberg(x_values, y_values, max_order):
    """
    Approximates the integral using Romberg's method for given y_values at given x_values.

    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        max_order (int): Maximum order (controls accuracy).

    Returns:
        float: The approximated integral.
    """
    R = np.zeros((max_order, max_order))
    a, b = x_values[0], x_values[-1]
    N = 1
    h = (b - a)

    # First trapezoidal estimate
    R[0, 0] = (h / 2) * (y_values[0] + y_values[-1])

    for i in range(1, max_order):
        N *= 2
        h /= 2

        sum_new_points = sum(np.interp(a + k * h, x_values, y_values) for k in range(1, N, 2))
        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_new_points

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)

    return R[max_order - 1, max_order - 1]


#a very small plotting function as i suspect something is up with the data...
def show_data(x_gaia, y_gaia,x_vega, y_vega):
    plt.figure(figsize=(10, 5))
    plt.plot(x_gaia, y_gaia, label="GAIA")
    plt.plot(x_vega, y_vega, label="Vega")
    plt.xlabel("Wavelength")
    plt.ylabel("Flux")
    plt.title("GAIA and Vega Data")
    plt.legend()
    plt.show()

import pandas as pd

# Load the CSV files into a pandas data frame
gaia = pd.read_csv("GAIA_G.csv", header=None, names=["Wavelength", "Flux"])
vega = pd.read_csv("vega_SED.csv")

# Split the data into lists
#This can be done in many different ways but for the sake of clarity (and NOT speed) I will do this
x_gaia = np.array(gaia["Wavelength"])
y_gaia = np.array(gaia["Flux"])

x_vega = np.array(vega["WAVELENGTH"])
y_vega = np.array(vega["FLUX"])

show_data(x_gaia, y_gaia,x_vega, y_vega) #hmm yes this looks bad

#We dont need to set a seperation as we have that from the data - its already binned. 
#Romberg still needs to know how long to compute for though 
max_order = 8

# GAIA data integration
trapz_gaia   = mfl.trapezoidal(x_gaia, y_gaia)
simpson_gaia = mfl.simpsons(x_gaia, y_gaia)
romberg_gaia = mfl.romberg(x_gaia, y_gaia, max_order)

# Vega data integration
trapz_vega   = mfl.trapezoidal(x_vega, y_vega)
simpson_vega = mfl.simpsons(x_vega, y_vega)
romberg_vega = mfl.romberg(x_vega, y_vega, max_order)


#print results
print("GAIA Data Integration:")
print("Trapezoidal Rule:   ", trapz_gaia)
print("Simpson's Rule:     ", simpson_gaia)
print("Romberg Integration:", romberg_gaia)

print("\nVega Data Integration:")
print("Trapezoidal Rule:   ", trapz_vega)
print("Simpson's Rule:     ", simpson_vega) # why is this one different?
print("Romberg Integration:", romberg_vega)
print("=============================\n")





#hmmm, that plot looked bad...
#We should remove the long tail from the Vega SED
#Romberg does not work well with things like this.
#See the final two paragraphs of page 162 in Mark Newmans book.

threshold_y = 0.2e-10    #at what point does the SED basically become 0?
## this is relative to the scale of the SED, not just some small number

mask = np.where(y_vega > threshold_y)
#mask = y_vega > threshold_y     #create a mask to identify where the data is below the value
x_vega = x_vega[mask]           #new data = masked old data 
y_vega = y_vega[mask]


mfl.show_data(x_gaia, y_gaia,x_vega, y_vega, output_png = 'result.png') #Better, the Vega SED has a different scale to Gaia
#Thats fine as long as we dont run into floating point uncertainty... how small can we go?


# GAIA data integration
trapz_gaia   = mfl.trapezoidal(x_gaia, y_gaia)
simpson_gaia = mfl.simpsons(x_gaia, y_gaia)
romberg_gaia = mfl.romberg(x_gaia, y_gaia, max_order)

# Vega data integration
trapz_vega   = mfl.trapezoidal(x_vega, y_vega)
simpson_vega = mfl.simpsons(x_vega, y_vega)
romberg_vega = mfl.romberg(x_vega, y_vega, max_order)


#print results
print("\n After setting a lower limit on the Vega SED...")
print("GAIA Data Integration:")
print("Trapezoidal Rule:   ", trapz_gaia)
print("Simpson's Rule:     ", simpson_gaia)
print("Romberg Integration:", romberg_gaia)

print("\nVega Data Integration:")
print("Trapezoidal Rule:   ", trapz_vega)
print("Simpson's Rule:     ", simpson_vega) # why is this one different?
print("Romberg Integration:", romberg_vega)
