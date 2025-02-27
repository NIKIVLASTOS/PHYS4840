import numpy as np

#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################

def cookie_change(budget):
    cookie_price = [2.65, 3.20, 3.45, 3.70]
    cookie_name = ['sugar', 'chocolate', 'snickerdoodle', 'smores']
    values = []
    for price in cookie_price:
        if budget // price != 0:
            change = budget - (price * (budget // price))
            values.append(change)
        else:
            values.append(budget)
    
    best_option = np.argmin(values)
    
    for i in range(len(cookie_name)):
        print(f"If you buy the {cookie_name[i]} cookie you will get ${round(values[i], 2)} of change")

    print(f"You should buy the {cookie_name[best_option]} you will get only ${round(values[best_option], 3)} of change")

#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################

def niki_sqrt(x, tolerance=1e-10):
    # IDK if we are supposed to do the line that says what these function do, but this function takes the square root of a number
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number") #This was taking a long time ti figure out so I am not doing negative square roots
    if x == 0 or x == 1:
        return x
    
    # This would be an initial guess for which the code starts with
    guess = x / 2.0
    
    #  th guess is modified over and over and overuntil the difference is smaller than the tolerance
    while abs(guess**2 - x) >   tolerance:
        guess = (guess + x / guess) / 2
    
    print(f"The sqrt of {x} is {guess}")
    return guess

#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################

def niki_floor(x):
    # thos should return the largest integer <= x
    if x < 0:
        return int(x) if x == int(x) else int(x) - 1
    else:
        return int(x) 

#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################

def niki_round(x, digits=0):
    # This will round a number to a specified number of digits, if a second number is not input it will round to 0
    factor = 10 ** digits  
    return int(x * factor + 0.5) / factor if x > 0 else int(x * factor - 0.5) / factor

#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################

def niki_min(*args):
    # I was trying to figure out how to make this work for a list and tuple (not just manually entering the number when you call the function) and asked my cousin and he showed me this way
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = args[0]  # makes the list/tuple into the arguments
    
    if not args:
        raise ValueError("At least one value is required")  # this pops up if there are no values entered when the function is called
    
    
    min_value = None
    first = True
    for value in args:
        # If it's the first value, set it as the minimum value
        if first:
            min_value = value
            first = False
        
        if min_value > value:
            min_value = value
        
        if value > min_value:
            pass  
    
    return min_value

#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################


def niki_argmin(*args):
    # I used the same as above for the instance of having a list or tuple
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = args[0]  # makes the list/tuple into the arguments
    
    if not args:
        raise ValueError("At least one value is required")  # this pops up if there are no values entered when the function is called
    
    min_value = None
    min_index = None
    first = True
    index = 0
    
    # this for loop will go through the values and find the index of the minimum
    for value in args:

        if first:
            min_value = value
            min_index = index
            first = False
        

        if value < min_value:
            min_value = value
            min_index = index
        
        if value > min_value:
            pass  
        
        index += 1
    
    return min_index



#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################

def niki_y(x):
    y = 2.0*x**3.0
    return y




#########################################################
####### FUNCTION THAT COMPUTES A DISTANCE MODULUS GIVEN A DISTANCE IN PARSECS #################
#########################################################


def distance_modulus(distance_pc):
    import math
  
    if distance_pc <= 0:
        raise ValueError("Distance must be greater than zero.")
    
    return 5 * math.log10(distance_pc/10) 
    


#########################################################
####### FUNCTION THAT COMPUTES f(x) = 1 + 1/2*[tanh(2x)] #################
#########################################################

def f_tanh(x):
    import numpy as np
    """Function to call: 1 + 1/2 [tanh(2x)]"""
    return (1 + 1/2*(np.tanh(2*x)))



#########################################################
####### FUNCTION THAT SHOWS data for HW#2 Problem #2 #################
#########################################################

#a very small plotting function as i suspect something is up with the data...
def show_data(x_gaia, y_gaia,x_vega, y_vega):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 5))
    plt.plot(x_gaia, y_gaia, label="GAIA")
    plt.plot(x_vega, y_vega, label="Vega")
    plt.xlabel("Wavelength")
    plt.ylabel("Flux")
    plt.title("GAIA and Vega Data")
    plt.legend()
    plt.show()



#########################################################
####### FUNCTION THAT computes trapezoidal integration method #################
#########################################################

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

#########################################################
####### FUNCTION THAT computes simpsons integration method #################
#########################################################


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

#########################################################
####### FUNCTION THAT computes romberg integration method #################
#########################################################

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

