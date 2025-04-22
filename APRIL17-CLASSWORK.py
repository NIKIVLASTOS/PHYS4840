#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             APRIL 17
###				Nikiphoros Vlastos
###             
#				PDEs II: boundary-value problems; relaxation; Initial Value Problems
###########################################




######## This is the code from the Book for Example 9.3

from numpy import empty
from pylab import plot,xlabel,ylabel,show

# Constant
L = 0.01 # thickness of steel in meters
D = 4.25e-6 # Thermal diffusivity
N = 100 # Number of divisions in the grid
a = L/N #grid Spacing
h = 1e-4 #Time-step
epsilon = h/1000

Tlo = 0.0 #low temp
Tmid= 20.0 # mid temp
Thi = 50.0 # high temp

t1 = 0.01
t2 = 0.1
t3 = 0.4
t4 = 1.0
t5 = 10.0
tend = t5+epsilon

# Create arrays
T = empty(N+1,float)
T[0] = Thi
T[N] = Tlo
T[1:N] = Tmid
Tp = empty(N+1, float)
Tp[0] = Thi
Tp[N] = Tlo

# Main loop
t = 0.0
c = h*D/(a*a)
while t<tend:

	#Calculate the new values of T
	for i in range(1,N):
		Tp[i] = T[i] + c*(T[i+1]+T[i-1]-2*T[i])

	T,Tp = Tp,T
	t += h 

	#Make plots at given times 
	if abs(t-t1)<epsilon:
		plot(T)
	if abs(t-t2)<epsilon:
		plot(T)
	if abs(t-t3)<epsilon:
		plot(T)
	if abs(t-t4)<epsilon:
		plot(T)
	if abs(t-t5)<epsilon:
		plot(T)

	xlabel("x")
	ylabel("T")
	show()


	







