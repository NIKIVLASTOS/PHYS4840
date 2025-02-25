#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             Tuesday February 25, 2025
###				Nikiphoros Vlastos
###             
#				
#				Numerical Differrentiation I
###########################################



###########################################
# Excercise #1: Book Problem 5.15 (pg 194 of text book)
###########################################

import numpy as np

def f_tanh(x):
    """Function to call: 1 + 1/2 [tanh(2x)]"""
    return (1 + 1/2*(np.tanh(2*x)))


number = 1
answer = f_tanh(number)
print(answer)

def central_difference(f_tanh, x, h=1e-10):
    return (f_tanh(x + h) - f_tanh(x - h)) / (h)


x_values = np.linspace(-2, 2, 100)
derivatives = np.array([central_difference(f_tanh, x) for x in x_values])

print(derivatives)



## THIS IS NOT DONE YET, I WILL ALSO EMAIL PHOTOS OF MY NOTES FROM LECTURE TODAY SO YOU KNOW I PARTICIPATED
