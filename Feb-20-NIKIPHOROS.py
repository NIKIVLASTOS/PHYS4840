#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             Tuesday February 20, 2025
###				Nikiphoros Vlastos
###             
#				Lecture W/ Doctor Miller
#				Numerical Integration: TRAPZ, Simpsons, Romberg, errors	
###########################################

###########################################
# Lecture: Review
###########################################

# Trapezoidal Rule
#	Split into trapezoids


# Limitation of integration:
#	Computer cannot do continous functions
# 	Can only do descrete calculations

# Simpsons Rule
#	Like trapezoidal but quadratic functions

# Romberg
#	Iteratively integrate



###########################################
# Lecture: Intergration #2
###########################################


# Gauss Legendre Quadrature





###########################################
# Excercise #1: from guass_legendre.py
###########################################


import numpy as np

def f(x):
    return x**2  # Some function thats easy to integrate by hand and hence verify

# Number of points (n) for Gauss-Legendre Quadrature
n = 1000

# Compute the Gauss-Legendre Quadrature points (roots of the Legendre polynomial) and weights
root, weight = np.polynomial.legendre.leggauss(n)

#print the roots and weights for the points
print('root', root)
print('weight', weight)

# Compute the integral approximation manually using a for loop
#iterating through each legendre polynomial

integral_approximation = 0

for i in range(n):
	point = root[i]
	weights = weight[i]
	function_value = f(point)
	weighted_value = weights * function_value
	integral_approximation = integral_approximation + weighted_value
    #grab the root for this polynomial
    #grap the weight for this polynomial
    #Evaluate function at the root
    # Apply weight
    # append to running sum


exact_integral = 0.6666666666666666


# Print final comparison
#print("\nFinal Results:")
print(f"Approximated integral using Gauss-Legendre Quadrature: {integral_approximation}")
print(f"Exact integral: {exact_integral}")
print(f"Error: {abs(integral_approximation - exact_integral)}")


###########################################
# Excercise #2: integral_test.py CONTINUED FROM TUESDAY FEB 18
###########################################





import numpy as np
import time

# Example usage with array data
def trapezoidal(y_values, x_values, N):
    """
    Approximates the integral using trapezoidal rule for given y_values at given x_values.
    
    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        N (int): Number of intervals.

    Returns:
        float: The approximated integral.
    """
    a = 0
    b = 1
    h = (b-a) / N

    integral = (1/2) * (y_values[0] + y_values[-1]) * h  # First and last terms

    for k in range(1, N):
        xk = a + k * h  # Compute x_k explicitly
        yk = np.interp(xk, x_values, y_values)  # Interpolate y at x_k manually in loop
        integral += yk * h

    return integral


# Simpson's rule for array data
def simpsons(y_values, x_values, N):
    """
    Approximates the integral using Simpson's rule for given y_values at given x_values.

    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        N (int): Number of intervals (must be even).

    Returns:
        float: The approximated integral.
    """

    a = 0
    b = 1
    h = (b-a) / N

    integral =  (y_values[0] + y_values[-1])# First and last y_value terms

    for k in range(1, N, 2):  # Odd indices (weight 4)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 4 * yk

    for k in range(2, N, 2):  # Even indices (weight 2)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 2 * yk

    return (h / 3) * integral  # Final scaling


# Romberg integration for array data
def romberg(y_values, x_values, max_order):
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
    a = 0
    b = 1
    N = 1
    h = (b - a)

    # First trapezoidal estimate
    R[0, 0] = (h / 2) * (y_values[0] + y_values[-1])

    for i in range(1, max_order):
        N = 2**i #Remember: we are recomputing the integral with different N (and therefore h)
        h =  (b-a)/2**i#Look at the github derivation for richardson extrapolation

        sum_new_points = sum(np.interp(a + k * h, x_values, y_values) for k in range(1, N, 2))
        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_new_points

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)

    return R[max_order - 1, max_order - 1]


def timing_function(integration_method, x_values, y_values, integral_arg):
    """
    Times the execution of an integration method.

    Parameters:
        integration_method (function): The numerical integration function.
        x_values (array-like): The x values.
        y_values (array-like): The corresponding y values.
        integral_arg (int, optional): EITHER Number of intervals to use (Simpson/Trapz) OR the maximum order of extrapolation (Romberg).

    Returns:
        tuple: (execution_time, integration_result)
    """
    start_time = time.time()
    result = integration_method(y_values, x_values, integral_arg)
    end_time = time.time()
    
    return end_time - start_time, result



# Function to integrate
def function(x):
    return x * np.exp(-x)

# Precompute data for fair comparisons
x_data = np.linspace(0, 1, 100000000)  # High-resolution x values
y_data = function(x_data)

# Testing parameters
N = 9 # Number of intervals
max_order = 9 # Romberg's accuracy level

# Measure timing for custom methods
trap_time, trap_result = timing_function(trapezoidal, x_data, y_data, N)
simp_time, simp_result = timing_function(simpsons, x_data, y_data, N)
romb_time, romb_result = timing_function(romberg, x_data, y_data, max_order)


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






import matplotlib.pyplot as plt

#plotting example.Sshowing how we can make a list, populate it and plot it

#def plotforintegration(x):
	#a function that does stuff
 #   return x/2, x**2

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
trap_time, trap_result = timing_function(trapezoidal, x_data, y_data, N)
simp_time, simp_result = timing_function(simpsons, x_data, y_data, N)
romb_time, romb_result = timing_function(romberg, x_data, y_data, max_order)

for Number in range(1,11):
	Trapezoid_N.append(Number)
	Simpson_N.append(Number)
	romberg_N.append(Number)																				




	# Precompute data for fair comparisons
	x_data = np.linspace(0, 1, 100000000)  # High-resolution x values
	y_data = function(x_data)
	

	# Measure timing for custom methods
	trap_time, trap_result = timing_function(trapezoidal, x_data, y_data, Number)
	simp_time, simp_result = timing_function(simpsons, x_data, y_data, Number)
	romb_time, romb_result = timing_function(romberg, x_data, y_data, Number)


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

	# Print results with error analysis
	#print("\nIntegration Method Comparison")
	#print("=" * 80) # why 80? https://peps.python.org/pep-0008/
	#print(f"{'Method':<25}{'Result':<20}{'Error':<20}{'Time (sec)':<15}")
	#print("-" * 80)
	#print(f"{'Custom Trapezoidal':<25}{trap_result:<20.8f}{trap_error:<20.8e}{trap_time:<15.6f}")
	#print(f"{'Custom Simpson\'s':<25}{simp_result:<20.8f}{simp_error:<20.8e}{simp_time:<15.6f}")
	#print(f"{'Custom Romberg':<25}{romb_result:<20.8f}{romb_error:<20.8e}{romb_time:<15.6f}")
	#print("=" * 80)
   
   
print(Trapezoid_N)
print(Trapezoid_error)
print(Trapezoid_time)
print(Simpson_N)
print(Simpson_error)
print(Simpson_time)
print(romberg_N)
print(romberg_error)
print(romberg_time)
print(romberg_N)

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
plt.plot(romberg_time, romberg_error, color='red', marker='x', , linestyle='-', label='romb_error')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Time (log scale)')
plt.ylabel('Function Error (log scale)')
plt.title('Comparison of Accuracy of Integration Methods V. Time')
plt.legend()
plt.show()





