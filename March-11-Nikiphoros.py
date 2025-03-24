#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             Tuesday March 11, 2025
###				Nikiphoros Vlastos
###             
#				
#				Exam Review
###########################################

#Solve the the equation x = 2-e^-x
from math import exp, sqrt, log
import numpy as np

x = 1.0
for i in range(10):
	x = 2-exp(-x)
	print(x)


#Solve the the equation x = e^1-x^2
# ln(x) = 1-x^2
# x = sqrt(1-ln(x))


#Form A
x = 0.5
for i in range(50):
	x = np.exp(1-x**2)
	print(x)


#Form B
x = 0.5
for i in range(50):
	x = np.sqrt(1.0-np.log(x))
	print(x)