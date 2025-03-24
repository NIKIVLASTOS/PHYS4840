#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             HOMEWORK #4
###				Nikiphoros Vlastos
###             
#				
###########################################

import matplotlib.pyplot as plt

from scipy.integrate import quad

import numpy as np
from numpy import array,empty




# I HAVE THE HADNWRITTEN PARTS HAD TO BE EMAILED AS I AM OUT OF TOWN BUT CAN GIVE THEM IN PERSON WHEN I RETURN ON THURSDAY
# ANY FUNCTIONS I CALL ARE ALSO IN MY GITHUB in the "nikiphoros_functions_lib.py" FILE

########################################################################################################################
# Completing in class lab from March 4th
########################################################################################################################

#######################################################################
#FROM DR. JOYCE: gaussian_elimination.py
###########################################################################

A = np.array([ [2,1,4,1], 
			[3,4,-1,-1], 
			[1,-4,1,5], 
			[2,-2,1,3] ],float)

vector = np.array([-4,3,9,7],float)

## dimension 
N = len(vector)

for m in range(N):

	## first, divide by the diagonal element
	divisor = A[m,m]

	## divide every entry in row m by the divisor
	A[m,:] /= divisor

	## the above is shorthand for this operation:
	## A[m,:] = A[m,:]/divisor

	##anything we do to the matrix we must do to the vector:
	vector[m] /= divisor

	## now subtract multipls of the top row from the lower rows
	## to zero out rows 2,3 and 4
	for i in range(m+1, N): ## note that we start from the second row: m+1

		## because the first row now has 1 in the upper-left corner,
		## the factor by which we have to multiply the first row to subtract
		## it from the second is equal to the value in the first entry
		## of the second row
		multiplication_factor = A[i,m] 

		## now we must apply this operation to the entire row 
		## AND vector, as usual 
		A[i,:]    -= multiplication_factor*A[m,:]
		vector[i] -= multiplication_factor*vector[m] 


print('the upper diagonal version of A is: \n', A)
print('The solutions is: \n', vector)

## Write the next part of this program:
##  how do we solve the system of equations now that we have
##  an upper-diagonal matrix?

## you may consult example 6.1 in your textbook if you need help

#########################################################################
# My Actual Part
#########################################################################

# This solve for each of the variables, then prints them all out
z =  np.round(vector[3] / A[3,3]) 
y = np.round(vector[2] / A[2,2])
x = np.round(((vector[1] / A[1,1]) - A[1,2]*y - A[1,3]*z))
w = np.round(((vector[0]/ A[0,0]) - A[0,1]*x - A[0,2]*y - A[0,3]*z))
print(f'W = {w}, X = {x}, Y = {y}, Z = {z}')




#########################################################################
#FROM DR. JOYCE: LU_decomposition.py
#########################################################################

A = array([[2, 1, 4, 1], 
            [3, 4, -1, -1], 
            [1, -4, 1, 5], 
            [2, -2, 1, 3]], float)

## dimension 
N = len(A)

# Initialize L as the N=4 identity matrix 
L = np.array([[1.0 if i == j else 0.0 for j in range(N)] for i in range(N)])
# this above is just a more explicit way of doing
#L = np.identity(N)

print("L looks like this: \n", L) ## should return the N=4 I


# initalize U as a copy of A
U = A.copy()


## this double loop will transform L
## into the lower-diagonal form we need
for m in range(N):
    for i in range(m+1, N):        
        
        # Compute the multiplier for the current row operation
        L[i, m] = U[i, m] / U[m, m]
        
        # Subtract the appropriate multiple of the pivot row from the current row
        U[i, :] -= L[i, m] * U[m, :]

print('The lower triangular matrix L is:\n', L)
print('The upper triangular matrix U is:\n', U)

## Write the next part of this program:
##  How do we solve the system of equations using forward and backward substitution?
##  Use L and U to solve Ax = b for a given vector b.

## HINT: see the end of 6.1.4 in your textbook (equations 6.37 through 6.39 in my version)

###################################################################
# My Actual Part
###################################################################

vector1 = np.array([-4,3,9,7],float)

from numpy.linalg import solve

U_x = solve(U,vector1)
L_Ux = solve(L,U_x)
print(L_Ux)


########################################################################################################################
# Completing in class lab from March 6th
########################################################################################################################

##########################################
# eigenvalues.py Assignment
############################################
import numpy as np
from numpy import array,empty

A = np.array([ [2, -1, 3,],\
			   [-1, 4, 5], 
			   [3,  5, 6] ],float)

eigenvector_1 =  np.array([-0.5774,\
						   -0.5774,\
						   0.5774],float)

LHS = np.dot(A, eigenvector_1)

## Bonus: Why doesn't this line work??
#LHS = A*eigenvector_1

RHS = -2.0*eigenvector_1

print("LHS:\n",LHS, "\n\nRHS:\n",RHS)





#############################################
# QR_decomposition.py
#############################################

#'''
#by importing and using the QR decomposition 
#algorithm in my_functions_lib.py:
#1) Find Q and R
#2) Confirm that Q is orthogonal
#3) Confirm that R is upper triangular
#4) Confirm that the matrix A introduced in eigenvalues.py
#can indeed be reconstructed by the dot product 
#of matrices Q and R
#''''

import nikiphoros_functions_lib as nv

#print(nv.qr_decomposition(A))

Q = nv.qr_decomposition(A)[0]
R = nv.qr_decomposition(A)[1]
A = np.dot(Q,R)
I = np.dot(Q,np.matrix.transpose(Q))
I_2 = np.dot(np.matrix.transpose(Q),Q)

print(np.matrix.transpose(Q))
print(np.linalg.inv(Q))
print(np.matrix.transpose(Q)-np.linalg.inv(Q))
print(I)
print(I_2)
print(Q)
print(R)
print(A)

## This has shown that Q is orthonoraml as Q^T*Q=Q*Q^T=I


########################################################################################################################
# Question 1
########################################################################################################################

#THIS IS DONE ON PAPER AND WILL BE HANDED IN IN PERSON



########################################################################################################################
# Question 2
########################################################################################################################


######################
# Part a
######################


# making the function for the integrand
def integrand(x, a):
    return x**(a-1) * np.exp(-x)

# This creates an array of x values from 0 to 5 with 500 steps inbetween them
x = np.linspace(0, 5, 500)

# make a plot for the integrand for different values of 'a'
plt.plot(x, integrand(x, 2), label=r'$a=2$', color='blue')
plt.plot(x, integrand(x, 3), label=r'$a=3$', color='green')
plt.plot(x, integrand(x, 4), label=r'$a=4$', color='red')

# this makes labels and titles
plt.xlabel('x')
plt.ylabel(r'Integrand: $x^{a-1} e^{-x}$')
plt.title('Graph of the integrand for different values of a')

# Make a legend for the plot
plt.legend()

# show the actual plot
plt.show()

######################
# Part b
######################

#THIS IS DONE ON PAPER AND WILL BE HANDED IN IN PERSON

######################
# Part c
######################

#THIS IS DONE ON PAPER AND WILL BE HANDED IN IN PERSON

######################
# Part d
######################

#THIS IS DONE ON PAPER AND WILL BE HANDED IN IN PERSON

######################
# Part e
######################
import numpy as np
from scipy.integrate import quad

# Define the integrand for the Gamma function using change of variables
def gamma_integrand(z, a, c):
    x = c * z / (1 - z + 1e-14)  # Avoid division by zero by adding 1e-14
    jacobian = c / (1 - z + 1e-14) ** 2  # Correct the Jacobian
    return (x ** (a - 1)) * np.exp(-x) * jacobian

# Define the gamma function using the change of variables
def gamma(a, c=1.0):
    result, _ = quad(gamma_integrand, 0, 1, args=(a, c))
    return result

# Test my function with Gamma(3/2) and compare to what the book says it should roughly be
result = gamma(3/2)
expected_value = 0.5 * np.sqrt(3.14159265)

print(f"Gamma(1/2) = {result}")
print(f"Expected value = {expected_value}")

######################
# Part f
######################

# This is just calculating Gamma(3), Gamma(6), and Gamma(10)
gamma_3 = gamma(3)
gamma_6 = gamma(6)
gamma_10 = gamma(10)

# print the results for Gamma(3), Gamma(6), and Gamma(10)
print(f"Gamma(3) = {gamma_3}")
print(f"Gamma(6) = {gamma_6}")
print(f"Gamma(10) = {gamma_10}")

# print corresponding factorials for comparison to my calculated gamma values, gotten from the problem
print(f"2! = {np.math.factorial(2)}")
print(f"5! = {np.math.factorial(5)}")
print(f"9! = {np.math.factorial(9)}")




########################################################################################################################
# Question 3
########################################################################################################################

######################
# Part 1
######################

# Supporting #mlinearalgebrafacts that show our matrix has unique solitions:
# (1) The matrix A is invertible (non-singular): given by the following
# A is invertible if and only if its rank is equal to its size (i.e., the number of rows or columns). For a 4x4 matrix, this means the rank must be 4.
# while A matrix's rank is the number of linearly independent rows (or columns). If the rank is 4, the system of equations is linearly independent, 
# and thus, it will have a unique solution. This is because when the rank is equal to the number of unknowns, the system of equations is well-conditioned and solvable.

######################
# Part 2
######################

# This is my LU Decomposition Function
def LU_decomposition(A):
    n = A.shape[0]
    L = np.zeros_like(A, dtype=float)
    U = np.zeros_like(A, dtype=float)
    
    for i in range(n):
        # Uppe Triangular
        for j in range(i, n):
            U[i, j] = A[i, j] - np.sum(L[i, :i] * U[:i, j])
        
        # Lower Triangular
        for j in range(i, n):
            if i == j:
                L[i, i] = 1
            else:
                L[j, i] = (A[j, i] - np.sum(L[j, :i] * U[:i, i])) / U[i, i]
                
    return L, U

# Making the matrix A
A = np.array([[1, 0, 0, 0],
              [0, 1, 1, -1],
              [0, 2, 4, 0],
              [0, 2, -1, 2]])

L, U = LU_decomposition(A)

print("L matrix (lower triangular):")
print(L)
print("\nU matrix (upper triangular):")
print(U)

# This is my QR Decomposition Function 
def QR_decomposition(A):
    n, m = A.shape
    Q = np.zeros_like(A, dtype=float)
    R = np.zeros((n, m), dtype=float)
    
    for i in range(m):
        # Compute the i-th column of Q
        Q[:, i] = A[:, i]
        
        for j in range(i):
            R[j, i] = np.dot(Q[:, j], A[:, i])
            Q[:, i] = Q[:, i] - R[j, i] * Q[:, j]
        
        R[i, i] = np.linalg.norm(Q[:, i])
        Q[:, i] = Q[:, i] / R[i, i]
        
    return Q, R

# This is taking my QR Decomposition function and using it for the matrix A defined above
Q, R = QR_decomposition(A)

print("\nQ matrix:")
print(Q)
print("\nR matrix:")
print(R)


######################
# Part 2
######################

# Verify Orthogonality: Q^T Q should be the identity matrix
Q_transpose = np.transpose(Q)
print("\nQ^T * Q (should be identity):")
print(np.round(np.dot(Q_transpose, Q)))

# Verify Upper Triangularity: All values below the diagonal of R should be zero, it will print "R is upper triangular" if they are 0
print("\nCheck if R is upper triangular:")
for i in range(R.shape[0]):
    for j in range(i):
        if R[i, j] != 0:
            print(f"R[{i},{j}] = {R[i, j]} is non-zero, R is not upper triangular.")
        else:
        	print(f"R is upper triangular.")






########################################################################################################################
# Question 4
########################################################################################################################




#Interpolation:

#Interpolation is a technique used to estimate values (that are unknown) between two known values in a dataset. 
#It is useful when you have a set of discrete data points and want to find an approximate value at a 
#point within the range of those data points. This happens a lot in experimental work as data is usually not continous.
# In interpolation, the goal is to construct a function that passes through the given data points.

#Method: You can use various methods for interpolation, such as linear interpolation, polynomial interpolation, 
#or spline interpolation. These methods differ in the degree of smoothness or complexity of the interpolating function.
# Obviously depending on need one would choose the best interpolation method.

#Use Case: You use interpolation when you want to estimate values of a function at points where you don't have data, 
#but the function is assumed to be continuous or smooth between the known points. This could be something that takes
# place over a period of time but you only have measures every 10 second. Clearly what ever you are measuring was also present 
# in the time between the 10 second intervals, so interpolation could help understand points between actual measured values.

#Example: Suppose you have the temperature data at 10:00 AM and 10:10 AM and so on every 10 minutes for an hour, 
# If you want to estimate the temperature at 10:05 AM (or any other in between point, You can use interpolation 
# to predict the temperature at 11:00 AM based on the data from 10:00 AM and 12:00 PM.

#Numerical Differentiation:

#Numerical differentiation is a technique used to approximate the derivative (rate of change) of a 
#function based on discrete data points. In numerical differentiation, you estimate the slope of 
#the function at a specific point using the values of the function at nearby points.

#Method: Common methods of numerical differentiation include the forward difference, backward difference, 
#and central difference methods. Each method uses data from surrounding points to approximate the 
# derivative at a specific point.

#Use Case: Numerical differentiation is useful when you have a dataset and need to find the rate of change 
#of the function represented by the data. This is often the case when you are interested in 
#how a quantity changes over time,  or space.

#Example: Suppose you're studying the velocity of a car at various time intervals, 
# and you want to estimate the car's acceleration (the derivative of velocity) at a specific time. 
#You would use numerical differentiation to estimate the car's acceleration at that time 
# based on the velocity data you have.

#Summary 
#Interpolation estimates unknown values within a dataset, while numerical differentiation 
#estimates the rate of change (derivative) of a function at specific points.



########################################################################################################################
# Question 5
########################################################################################################################

import math

# This is my function to compute the eigenvalues of a 2x2 matrix
def eigenvalues_2x2(a, b, c, d):
    # Calculate the discriminant of it
    discriminant = (a + d) ** 2 - 4 * (a * d - b * c)
    
    # this will check if the discriminant is non-negative if it is it will print 'Complex eigenvalues'
    if discriminant < 0:
        raise ValueError("Complex eigenvalues")
    
    # This is calculating the eigenvalues using the quadratic formula
    eig1 = ((a + d) + math.sqrt(discriminant)) / 2
    eig2 = ((a + d) - math.sqrt(discriminant)) / 2
    
    return eig1, eig2

# Make Matrix A that looks like [[4, 1], [2, 3]] to be plugged into my function above
a, b, c, d = 4, 1, 2, 3

# Get the eigenvalues
eig1, eig2 = eigenvalues_2x2(a, b, c, d)

# Print the eigenvalues
print("Eigenvalues of the matrix A:")
print(f"Eigenvalue 1: {eig1}")
print(f"Eigenvalue 2: {eig2}")



# my function to compute eigenvalues of a 3x3 matrix
def eigenvalues_3x3(matrix):
    # Calculate the characteristic polynomial using numpy's roots function. the characteristic polynomial is the determinant of (A - lambda * I)
    coeffs = np.poly(matrix)
    eigenvals = np.roots(coeffs)  
    return eigenvals


B = np.array([[1, 2, 3],
              [0, 1, 4],
              [0, 0, 1]])

# calculate the eigenvalues of matrix B
eigenvals_B = eigenvalues_3x3(B)

# Print Values
print("Eigenvalues of the matrix B:")
print(np.round(eigenvals_B, decimals=3))


C = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# calculate the eigenvalues of Matrix C above
eigenvals_c = eigenvalues_3x3(C)

# Print Values
print("Eigenvalues of the matrix C:")
print(np.round(eigenvals_c, decimals=3))


D = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 10]])

# Calculate the eigenvalues of Matrix D above
eigenvals_D = eigenvalues_3x3(D)

# Print Values
print("Eigenvalues of the matrix D:")
print(np.round(eigenvals_D, decimals=3))



