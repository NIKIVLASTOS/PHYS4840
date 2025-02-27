#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             HOMEWORK #3
###				Nikiphoros Vlastos
###             
#				
###########################################

###########################################
# Question #0: Completion of Labs from the Week
###########################################
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import time


import nikiphoros_functions_lib as nv
# Precompute data for fair comparisons
x_data = np.linspace(0, 1, 100000000)  # High-resolution x values
y_data = nv.function1(x_data)

# Testing parameters
N = 9 # Number of intervals
max_order = 9 # Romberg's accuracy level

# Measure timing for custom methods
trap_time, trap_result = nv.timing_function1(nv.trapezoidal1, x_data, y_data, N)
simp_time, simp_result = nv.timing_function1(nv.simpsons1, x_data, y_data, N)
romb_time, romb_result = nv.timing_function1(nv.romberg1, x_data, y_data, max_order)


# True integral value
true_value = 0.26424111765711535680895245967707826510837773793646433098432639660507700851

# Compute errors
trap_error = np.abs(true_value - trap_result) / true_value
simp_error = np.abs(true_value - simp_result) / true_value
romb_error = np.abs(true_value - romb_result) / true_value

# Print results with error analysis
print("\nIntegration Method Comparison")
print("=" * 80) # why 80? https://peps.python.org/pep-0008/
print(f"{'Method':<25}{'Result':<20}{'Error':<20}{'Time (sec)':<15}")
print("-" * 80)
print(f"{'Custom Trapezoidal':<25}{trap_result:<20.8f}{trap_error:<20.8e}{trap_time:<15.6f}")
print(f"{'Custom Simpson\'s':<25}{simp_result:<20.8f}{simp_error:<20.8e}{simp_time:<15.6f}")
print(f"{'Custom Romberg':<25}{romb_result:<20.8f}{romb_error:<20.8e}{romb_time:<15.6f}")
print("=" * 80)



# Initialise lists
Trapezoid_time = []
Trapezoid_error= []
Trapezoid_N= []
Simpson_time = []
Simpson_error= []
Simpson_N = []
romberg_time = []
romberg_error= []
romberg_N = []




# Measure timing for custom methods
trap_time, trap_result = nv.timing_function1(nv.trapezoidal1, x_data, y_data, N)
simp_time, simp_result = nv.timing_function1(nv.simpsons1, x_data, y_data, N)
romb_time, romb_result = nv.timing_function1(nv.romberg1, x_data, y_data, max_order)

for Number in range(1,11):
	Trapezoid_N.append(Number)
	Simpson_N.append(Number)
	romberg_N.append(Number)																				


	
	x_data = np.linspace(0, 1, 100000000)  # This will make a high-resolution of x values
	y_data = nv.function1(x_data)
	

	# Measure timing for custom methods
	trap_time, trap_result = nv.timing_function1(nv.trapezoidal1, x_data, y_data, Number)
	simp_time, simp_result = nv.timing_function1(nv.simpsons1, x_data, y_data, Number)
	romb_time, romb_result = nv.timing_function1(nv.romberg1, x_data, y_data, Number)


	# True integral value
	true_value = 0.26424111765711535680895245967707826510837773793646433098432639660507700851

	# Compute errors
	trap_error = np.abs(true_value - trap_result) / true_value
	simp_error = np.abs(true_value - simp_result) / true_value
	romb_error = np.abs(true_value - romb_result) / true_value

	Trapezoid_error.append(np.abs(true_value - trap_result) / true_value)
	Simpson_error.append(np.abs(true_value - simp_result) / true_value)
	romberg_error.append(np.abs(true_value - romb_result) / true_value)
	Trapezoid_time.append(trap_time)
	Simpson_time.append(simp_time)
	romberg_time.append(romb_error)



plt.figure() # Create a figure
plt.plot(Trapezoid_N, Trapezoid_error, color='blue', marker='x', markersize=8 , linestyle='-', label='Trapezoid_error')
plt.plot(Trapezoid_N, Simpson_error, color='green', marker='x', markersize=8, linestyle='-', label='Simpson_error')
plt.plot(Trapezoid_N, romberg_error, color='red', marker='x', markersize=8, linestyle='-', label='romb_error')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('N values (log scale)')
plt.ylabel('Function Error (log scale)')
plt.title('Accuracy of Integration Methods')
plt.legend()

plt.show()


plt.figure()  # Create a new figure 
plt.plot(Trapezoid_time, Trapezoid_error, color='blue', marker='x', markersize=8, linestyle='-', label='Trapezoid_error')
plt.plot(Simpson_time, Simpson_error, color='green', marker='x', markersize=8, linestyle='-', label='Simpson_error')
plt.plot(romberg_time, romberg_error, color='red', marker='x', markersize=8, linestyle='-', label='romb_error')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Time (log scale)')
plt.ylabel('Function Error (log scale)')
plt.title('Comparison of Accuracy of Integration Methods V. Time')
plt.legend()
plt.show()

plt.figure() #plotting just the trapezoid time v error
plt.plot(Trapezoid_time, Trapezoid_error, color='blue', marker='x', markersize=8, linestyle='-', label='Trapezoid_error')
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel('Time')
plt.ylabel('Function Error')
plt.title('Comparison of Accuracy of Trapezoid Integration Methods V. Time')
plt.legend()
plt.show()


plt.figure() #plotting just the simpsins time v error
plt.plot(Simpson_time, Simpson_error, color='green', marker='x', markersize=8, linestyle='-', label='Simpson_error')
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel('Time (log scale)')
plt.ylabel('Function Error (log scale)')
plt.title('Comparison of Accuracy of Simpson Integration Method V. Time')
plt.legend()
plt.show()

plt.figure()
plt.plot(romberg_time, romberg_error, color='red', marker='x', markersize=8, linestyle='-', label='romb_error')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Time (log scale)')
plt.ylabel('Function Error (log scale)')
plt.title('Comparison of Accuracy of Romberg Integration Method V. Time')
plt.legend()
plt.show()



###########################################
# Question #1: 
###########################################

## Load in CSV files (If you're grading this, the files are in the same directory as this file in my Github)
#gaia_data = pd.read_csv("GAIA_G.csv", header=None)  # GAIA_G.csv has two columns: wavelength, flux
#vega_data = pd.read_csv("Vega_SED.csv")  # Vega_SED.csv has three columns: wavelength, flux, continuum (ignore continuum)

## Extract relevant columns of data from the read in files
#gaia_wavelength = gaia_data.iloc[:, 0].values
#gaia_flux = gaia_data.iloc[:, 1].values

#vega_wavelength = vega_data["WAVELENGTH"].values                                             
#vega_flux = vega_data["FLUX"].values

## select values for N & max_order
#N = 1000  # for Trapezoidal and Simpson's  
#max_order = 10  # for Romberg 

## Ensure N is even for Simpson’s Rule
#if N % 2 != 0:
#    N += 1  


## Compute integrals using the functions we made in class (and from question 0 in this HW)
#gaia_trap = trapezoidal(gaia_flux, gaia_wavelength, N)
#gaia_simp = simpsons(gaia_flux, gaia_wavelength, N)
#gaia_romb = romberg(gaia_flux, gaia_wavelength, max_order)

#vega_trap = trapezoidal(vega_flux, vega_wavelength, N)
#vega_simp = simpsons(vega_flux, vega_wavelength, N)
#vega_romb = romberg(vega_flux, vega_wavelength, max_order)


## Print results
#print("\nComputed Areas:")
#print("=" * 60)
#print(f"{'Method':<20}{'GAIA Area':<20}{'Vega Area':<20}")
#print("-" * 60)
#print(f"{'Trapezoidal':<20}{gaia_trap:<20.6f}{vega_trap:<20.6f}")
#print(f"{'Simpson\'s':<20}{gaia_simp:<20.8f}{vega_simp:<20.6f}")
#print(f"{'Romberg':<20}{gaia_romb:<20.6f}{vega_romb:<20.6f}")
#print("=" * 60)





## Create a figure and axis for GAIA
#plt.figure(figsize=(12, 6))

## Plot GAIA data
#plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
#plt.plot(gaia_wavelength, gaia_flux, color='blue', label='GAIA Flux')
#plt.title('GAIA G Band Data')
#plt.xlabel('Wavelength (nm)')
#plt.ylabel('Flux')
#plt.grid(True)
#plt.legend()

# Plot vega data
#plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
#plt.plot(vega_wavelength, vega_flux, color='orange', label='Vega Flux')
#plt.title('Vega Spectral Energy Distribution')
#plt.xlabel('Wavelength (nm)')
#plt.ylabel('Flux')
#plt.grid(True)
#plt.legend()

# make layout tight
#plt.tight_layout()
#plt.show()



##### NV:EVERYTHING ABOVE HERE (which has been commented out) was my first effort before meeting with Dr. Miller 
#    about the reasons behind why my intergrals were what they were, Below is the improved code with comments and slight changes from Dr. Miller's Github


# NV: also as this section is not code I sole wrote any coments I made I clarified by 'NV:'

# NV:For this part I am improting my functions as I have the integration methods and the 'show_data' method from Dr. Miller now placed into my functions library

# Load the CSV files into a pandas data frame
gaia = pd.read_csv("GAIA_G.csv", header=None, names=["Wavelength", "Flux"]) # NV: Here Dr. Miller is assigning the 'names' to each of the columns as they are not specified in the csv file. I could also just un hash my read in from above but for continuity have not
vega = pd.read_csv("vega_SED.csv")

# Split the data into lists
x_gaia = np.array(gaia["Wavelength"]) #NV: this name was assigned in the above step by Dr. Miller (it does not actually have the name's in the csv file itself)
y_gaia = np.array(gaia["Flux"])

x_vega = np.array(vega["WAVELENGTH"])
y_vega = np.array(vega["FLUX"])

nv.show_data(x_gaia, y_gaia,x_vega, y_vega) #hmm yes this looks bad (NV:I talked to Dr. Miller about why this was, also this is calling the show_data function from my library and plotting the data as it is without any further modification)

#We dont need to set a seperation as we have that from the data - its already binned. 
#Romberg still needs to know how long to compute for though 
max_order = 8 # NV: Here the max order is being set for the next set of calculations/plots

# NV: This is the GAIA data integration for each of the three methods
trapz_gaia   = nv.trapezoidal(x_gaia, y_gaia) #NV:Again these are calling the functions from my functions library and setting the variables to the corresponding functions
simpson_gaia = nv.simpsons(x_gaia, y_gaia)
romberg_gaia = nv.romberg(x_gaia, y_gaia, max_order)

# NV: This is the Vega data integration for each of the three methods
trapz_vega   = nv.trapezoidal(x_vega, y_vega) #NV:Again these are calling the functions from my functions library and setting the variables to the corresponding functions
simpson_vega = nv.simpsons(x_vega, y_vega)
romberg_vega = nv.romberg(x_vega, y_vega, max_order)


# NV: This is printing the results of our three integration methods for our 2 different data sets
print("GAIA Data Integration:")
print("Trapezoidal Rule:   ", trapz_gaia)
print("Simpson's Rule:     ", simpson_gaia)
print("Romberg Integration:", romberg_gaia)

print("\nVega Data Integration:")
print("Trapezoidal Rule:   ", trapz_vega)
print("Simpson's Rule:     ", simpson_vega) 
print("Romberg Integration:", romberg_vega)
print("=============================\n") 


# NV: We see that for the Vega Data we are still getting a wide variance in our integration calculations which should not be the case! I
# talked with Dr. Miller about this and as what is done below the problem will me remediated


#hmmm, that plot looked bad...
#We should remove the long tail from the Vega SED
#Romberg does not work well with things like this.
#See the final two paragraphs of page 162 in Mark Newmans book. 
#NV:because it goes out for a long time with nothing we need to create a threshold to cut off the 'tail' of the Vega data to allow for more accurate integrations)

threshold_y = 0.2e-10    #at what point does the SED basically become 0?
## this is relative to the scale of the SED, not just some small number
## NV: this sets the threshold at values of y that are less than 0.2e-10 (a very small number...I guess depending on what you consider small)

mask = np.where(y_vega > threshold_y)
#mask = y_vega > threshold_y     #create a mask to identify where the data is below the value     
# NV: I believe Dr. Miller said this part was actually written by Dr. Joyce. What is being done is the  mask is essentially saying look in the old data and wherever the y points are greater than the threshold keep those
x_vega = x_vega[mask]           #new data = masked old data 
y_vega = y_vega[mask]


nv.show_data(x_gaia, y_gaia,x_vega, y_vega) #Better, the Vega SED has a different scale to Gaia
#Thats fine as long as we dont run into floating point uncertainty... how small can we go?
# NV: again we are now using the show_data function to plot the new data with how it looks


# GAIA data integration
# NV: This Data has not changes
trapz_gaia   = nv.trapezoidal(x_gaia, y_gaia)
simpson_gaia = nv.simpsons(x_gaia, y_gaia)
romberg_gaia = nv.romberg(x_gaia, y_gaia, max_order)

# Vega data integration
# NV: now we are going to calculate the new results and they should be close in agreement if our 'mask/threshold worked'
trapz_vega   = nv.trapezoidal(x_vega, y_vega)
simpson_vega = nv.simpsons(x_vega, y_vega)
romberg_vega = nv.romberg(x_vega, y_vega, max_order)


#print results
print("\n After setting a lower limit on the Vega SED...")
print("GAIA Data Integration:")
print("Trapezoidal Rule:   ", trapz_gaia)
print("Simpson's Rule:     ", simpson_gaia)
print("Romberg Integration:", romberg_gaia)

print("\nVega Data Integration:")
print("Trapezoidal Rule:   ", trapz_vega)
print("Simpson's Rule:     ", simpson_vega) 
print("Romberg Integration:", romberg_vega)


###########################################
# Question #2: Written
###########################################


# Suppose we want to compute the area under the curve defined by the function 
# f(x)=sin(x) from x=0 to x=π. This function is periodic and oscillates between 0 and 1, 
# making it a good candidate for numerical integration. The exact integral 
# can be calculated analytically, but in many practical situations, 
# we might not have an explicit formula or the function could be too complex to integrate analytically.

# Integration Method Choice: Simpson's Rule

# I would choose Simpson's Rule for numerical integration in this scenario because:

# 1.) Accuracy: Simpson's Rule provides a good balance of accuracy and computational 
# efficiency. It uses parabolic segments to approximate the area under the curve, 
# which often results in a more accurate estimate compared to methods like the Trapezoidal Rule, 
# especially for functions that are smooth and well-behaved like f(x)=sin(x).

# 2.) Computation Time: Simpson's Rule typically requires fewer function evaluations 
# than higher-order methods while still achieving high accuracy. This is especially advantageous 
# when the function is expensive to compute or if we need to perform the integration repeatedly in simulations.

# 3.) Error Control: The error in Simpson's Rule can be estimated, allowing for adaptive 
# techniques where the number of intervals can be increased if the error estimate is not satisfactory.


###########################################
# Question #3: I Have hashed out my functions as they are in my functions library but left them so You can see what they look like
###########################################


# The problem did not say to have these functions in our library functions library 
# so I have the functions directly in here so you can see thembut could move 
# them if that is what is neccesary. They are also in my library

## part a ### 

#def functz(x):
#    """Computes the value of the function f(x) = x^2."""
#    return x ** 2

#def compute_sum(n):
#    """Computes the sum s = sum(f(xi)) for i from 1 to n."""
#    s = 0
#    for i in range(1, n + 1):
#        s += functz(i)
#    return s

# Example 
n = 10  # You can change this value to compute the sum for different n
result = nv.compute_sum(n)
print(f"The sum s from 1 to {n} of f(x) where f(x) = x^2 is: {result}")


## part b ### 

#def compute_average(S):
#    """Computes the average x bar of the set S."""
#    n = len(S)  # Number of elements in S
#    if n == 0:
#        return 0  # Handle case where S is empty
#    total_sum = sum(S)  # Sum of all elements in S
#    x_bar = total_sum / n  # Calculate average
#    return x_bar

# Example 
S = [1, 2, 3, 4, 5]  # You can change this list to any group of numbers
average = nv.compute_average(S)
print(f"The average x bar of the set S is: {average}")


## part c ### 

#def factorial(n):
#    """Computes the factorial of n (n!)."""
#    if n < 0:
#        return "Undefined for negative numbers"  # Factorial is not defined for negative numbers
#    result = 1
#    for i in range(1, n + 1):
#        result *= i  # Multiply result by i for each i from 1 to n
#    return result

# Example 
n = 3  # You can change this value to compute the factorial of any non-negative integer
fact = nv.factorial(n)
print(f"The factorial of {n} is: {fact}")



###########################################
# Question #4: Book Excercise 5.20: AGAIN, I Have hashed out my functions as they are in my functions library but left them so You can see what they look like
###########################################

###########################
## part a ### 
###########################

# This makes the function to integrate
#def function(x):
#    """Function to integrate: sin^2(x) / x^2."""
#    result = np.where(x == 0, 1, (np.sin(x)**2) / (x**2))  # We learned np.where in an intro coding class I took last year it takes (condition, x (if condition is true), y (if condition is not true))
#    return result

#def step(x1, x2, f1, f2, delta):
 #   """Recursive function to integrate using adaptive trapezoidal rule with local extrapolation"""
 #   xm = 0.5 * (x1 + x2)
 #   fm = function(xm)
 #   h = x2 - x1
 #   
 #   # Trapezoidal rule estimates
 #   I1 = 0.5 * h * (f1 + f2)
 #   I2 = 0.25 * h * (f1 + 2 * fm + f2)
 #   
 #   # Error estimate
 #   error = abs(I2 - I1) / 3.0
 #   
 #   target = h * delta # Target accuracy for this slice
    
 #   if error < target: # checking to see if reached target accuracy
 #       return (h / 6) * (f1 + 4 * fm + f2) # Use Simpson's rule if at our target accuracy for final value of integral
 #   else:
 #    # Recursively integrate smaller slices until we get desired accuracy
 #       left = step(x1, xm, f1, fm, delta)
 #       right = step(xm, x2, fm, f2, delta)
 #       return left + right

#def adaptive_trapezoidal(a, b, epsilon):
#    """Computes the integral of f(x) from a to b to within accuracy epsilon."""
#    delta = epsilon / (b - a)
#    return step(a, b, function(a), function(b), delta)

# Compute the integral from 0 to 10 with accuracy 10^-4
a, b, epsilon = 0, 10, 1e-4
result = nv.adaptive_trapezoidal(a, b, epsilon)
print(f"Computed integral: {result:.6f}")

###########################
## part b ### 
###########################

# Including f(x1) and f(x2) as arguments in the step function is a smart optimization 
# because it avoids redundant function evaluations, improving efficiency. 
# If the function only received x1 and x2, it would need to recompute f(x1) and f(x2)
# every time it was called, leading to unnecessary recalculations. In an 
# integration method that relies on recursion, this would significantly increase 
# computational time (and then money), especially if evaluating f(x) is expensive, such as when it 
# involves trigonometric or exponential operations. Additionally, passing precomputed 
# values ensures consistency in function evaluations, reducing potential floating-point 
# errors that could arise from separate calculations in different recursive calls. By including 
# f(x1) and f(x2) as arguments, the algorithm becomes more efficient.

###########################
## part c ### 
###########################

#  store slice endpoints, empty list to start
slice_points = []

#def step2(x1, x2, f1, f2, delta, slice_points):
#    """trapezoidal rule with slice tracking"""
#    slice_points.extend([x1, x2])  # Store slice endpoints each time#

#    xm = 0.5 * (x1 + x2)
#    fm = function(xm)
#    h = x2 - x1
#    
#    # Trapezoidal rule estimates
#    I1 = 0.5 * h * (f1 + f2)
#    I2 = 0.25 * h * (f1 + 2 * fm + f2)
#    
#    # Error estimate
 #   error = abs(I2 - I1) / 3.0
 #   target = h * delta  # Target accuracy for this slice

#    if error < target: # checking to see if we have reached our target accuracy
#        return (h / 6) * (f1 + 4 * fm + f2)  # Use Simpson's rule if at our target accuracy for final value of integral
#    
#    else:
#     # Recursively integrate smaller slices until we get desired accuracy
#        left = step2(x1, xm, f1, fm, delta, slice_points)
#        right = step2(xm, x2, fm, f2, delta, slice_points)
#        return left + right

# integration function
#def adaptive_trapezoidal2(a, b, epsilon):
#    """Computes the integral and tracks slice points"""
#    slice_points = [] 
#    delta = epsilon / (b - a)
#    result = step2(a, b, function(a), function(b), delta, slice_points)
#    return result, slice_points



# Compute the actual integral
a, b, epsilon = 0, 10, 1e-4
result, slice_points = nv.adaptive_trapezoidal2(a, b, epsilon)
print(f"Computed integral: {result:.6f}")

# Remove duplicate points and sort for plotting
slice_points = sorted(set(slice_points))

# Plot function
x_vals = np.linspace(a, b, 1000)
y_vals = nv.function(x_vals)

plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_vals, label=r'$f(x) = \frac{\sin^2(x)}{x^2}$', color='blue')
plt.scatter(slice_points, nv.function(np.array(slice_points)), color='red', label='Integration slice points', zorder=3, s=20) #zorder will set the red dots inthe front of the plot
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.title("Adaptive Trapezoidal Integration Slice Points")
plt.show()
