#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##!/usr/bin/python3.8
##########################################
#
###             Thursday March 6, 2025
###				Nikiphoros Vlastos
###             
#				
#				Gaussian Processes & matrices (Dr. Joel)
###########################################

###



## Gausiian processes (is a special cse of CARMA)
#Continouis-Time autoregressive motion average (CARMA) Process
#		p must be real or p must be in complex conjugate pairs


# We can module al ight curve that is the solution to a CARMA as a combination of signal, noise, and linear trends:
#		(1)	y = s + n +Lq

#Taking the covariance of the curve 1, the signalhas a covariance of:
#			S= <ss^T>

#The total covariance of the light curve is the sum of the originial covariance and the noise covariance:
#		C =






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
