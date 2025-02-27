#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             Tuesday February 27, 2025
###				Nikiphoros Vlastos
###             
#				
#				Numerical Differrentiation II
###########################################

import numpy as np
import matplotlib.pyplot as plt
from math  import tanh, cosh

#import sys
#sys.path.append('../')
#import nikiphoros_functions_lib as nv




def f_tanh(x):
	fx = 1.0 + 0.5*tanh(2.0*x)
	return fx


def df_dx(x):
	dfdx = 1.0/(np.cosh(2.0*x)**2.0)
	return dfdx


## compute the instantaneous derivatives
## using the central difference approximation
## over the interval -2 to 2

x_lower_bound = -2.0
x_upper_bound = 2.0

N_samples = 100

#####################
#
# Try different values of h
# What did we "prove" h should be
# for C = 10^(-16) in Python?
#
#######################

xdata = np.linspace(x_lower_bound, x_upper_bound, N_samples)
h = 1e-16## what goes here?

central_diff_values1 = []
for x in xdata:
	central_difference = (f_tanh(x + 0.5*h) - f_tanh(x - 0.5*h) ) / h
	central_diff_values1.append(central_difference)

h = 1e-8## what goes here?

central_diff_values2 = []
for x in xdata:
	central_difference = (f_tanh(x + 0.5*h) - f_tanh(x - 0.5*h) ) / h
	central_diff_values2.append(central_difference)

h = 1## what goes here?

central_diff_values3 = []
for x in xdata:
	central_difference = (f_tanh(x + 0.5*h) - f_tanh(x - 0.5*h) ) / h
	central_diff_values3.append(central_difference)


h = 2## what goes here?

central_diff_values4 = []
for x in xdata:
	central_difference = (f_tanh(x + 0.5*h) - f_tanh(x - 0.5*h) ) / h
	central_diff_values4.append(central_difference)

h = 0.1## what goes here?

central_diff_values5 = []
for x in xdata:
	central_difference = (f_tanh(x + 0.5*h) - f_tanh(x - 0.5*h) ) / h
	central_diff_values5.append(central_difference)

## Add the analytical curve
## let's use the same xdata array we already made for our x values

analytical_values = []
for x in xdata:
	dfdx = df_dx(x)
	analytical_values.append(dfdx)


plt.plot(xdata, analytical_values, linestyle='-', color='black')
plt.plot(xdata, central_diff_values1, "*", color="green", markersize=8, alpha=0.5, label="h=1e-16")
plt.plot(xdata, central_diff_values2, "*", color="blue", markersize=8, alpha=0.5, label="h=1e-8")
plt.plot(xdata, central_diff_values3, "*", color="red", markersize=8, alpha=0.5, label="h=1")
plt.plot(xdata, central_diff_values4, "*", color="yellow", markersize=8, alpha=0.5, label="h=2")
plt.plot(xdata, central_diff_values5, "o", color="pink", markersize=8, alpha=0.5, label="h=1e-1")
plt.ylim(0,1.1)
plt.legend()
plt.show()
#plt.savefig('numerical_vs_analytic_derivatives.png')
#plt.close()


# 1e-8 gives a good approximation, but so does 1e-1





############# IN class excercise #2 ###########################


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# some data
x = np.array([0, 1, 2, 3, 4, 5,6,7,8,9,10,11,12])
y = np.array([0, 1, 0, 1, 0, 1,0,1,0,1,0,1,0])  

# Define fine-grained x-values for interpolation
x_domain = np.linspace(min(x), max(x), 100)

# Linear Interpolation
linear_interp = interp1d(x, y, kind='linear')
y_linear = linear_interp(x_domain)

# quadratic Interpolation
quad_interp = interp1d(x, y, kind='quadratic')
y_quad = quad_interp(x_domain)

# Cubic Spline Interpolation
cubic_spline = CubicSpline(x, y)
y_cubic = cubic_spline(x_domain)

# Plot the results
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', label='Data Points', zorder=3)
plt.plot(x_domain, y_linear, '--', label='Linear Interpolation', linewidth=2)
plt.plot(x_domain, y_quad, '--', label='Quadratic Interpolation', linewidth=2)
plt.plot(x_domain, y_cubic, label='Cubic Spline Interpolation', linewidth=2)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear vs. Cubic Spline Interpolation')
plt.grid(True)
plt.show()



# Q1: The linear interpolation is much less smooth (the linear is 'linear' so unless their are an extremely high 
# number of (between two other points in which a ccurve my exist) point you can't get 'curved' lines)

# Q2: When you make the points oscilate (or add points so that it oscillates) or the data is exponential in nature the linear inerpolation will not 
# improve (infact will likely decrease in quality), the cubic spline on the other hand increases in quality when
# you have oscillatory or exponential behavior, while it may not perform as well if the data is linear in nature

# Q3: When the point are sinosodal in nature the first move from 0 to 1 for the cubic splin overshoots point 1 then return
# This also happens similarly at the final two points I have plotted 
# (this can likely be remediated by adding a point inbetween the two at 0.5), however, after the first 
# and last points the function follows a sinosodal curve very well. While the linear interpolation
# Simply goes back and fourth in a straight line and does not give a good approximation of a true sinosdal function


# Q4: The Quadratic interpolation seems to better represent the sinosodal function than the cubic (it overshoots at the fist and second points by less than the cubic)
