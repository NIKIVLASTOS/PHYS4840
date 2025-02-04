#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             IN CLASS STUFF February 4, 2025 
###				Nikiphoros Vlastos
###             
#				Log v Linear, data visualization, plotting & Github
###########################################



###### log is taken to mean log-bas-10 (np.log10) not base e

##### Linear vs Log: Shapes of spaces
## you do not change the value of the function but change the coordinate systems
## instead of transofmring coordinate system (axes) if you take the log of the function it will appear graphically the same

##### Data visualization choices
## Can do one coordinate in log and one in linear (semi-log plot)
## can look at min and max of data to determine if need a log-log semi-log or linear plot to display data






##### Excercise  #######

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 100, 500)
y = x**2.0

## linear plot
plt.plot(x,y, linestyle='-', color='blue', linewidth=5)
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.grid(True) ## turn on/off as needed
plt.show()
plt.close()

## log plot
plt.plot(x,y, linestyle='-', color='red', linewidth=5)
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.xscale('log')  # Set x-axis to log scale
plt.yscale('log')  # Set y-axis to log scale
plt.grid(True) ## turn on/off as needed
plt.show()
plt.close()



###### Version Control Systems (VCS)
### git is a type of VCS
## get enables distributed development
## github is a git hosting platform (github hosts git)





##### Excercise #1  #######

from nikiphoros_functions_lib import niki_y
import numpy 

## HERE IS THE LINEAR PLOT
x = np.linspace(1, 100, 500)  # x values
#print(niki_y(2))
y = niki_y(x) # complete this statement using the
		# function you wrote in your functions library

plt.plot(x,y, linestyle='--', color='green', linewidth=2)
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.grid(True) ## turn on/off as needed
plt.show()
plt.close()

## HERE IS THE log-log plot

x = np.linspace(1, 100, 500)  # x values
#print(niki_y(2))
y = niki_y(x) # complete this statement using the
		# function you wrote in your functions library

plt.plot(x,y, linestyle='--', color='black', linewidth=2)
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.xscale('log')  # Set x-axis to log scale
plt.yscale('log')  # Set y-axis to log scale
plt.grid(True) ## turn on/off as needed
plt.show()
plt.close()


## HERE IS THE  plot log(x) vs log(y)

x = np.linspace(1, 100, 500)  # x values
#print(niki_y(2))
y = niki_y(x) # complete this statement using the
		# function you wrote in your functions library

plt.plot(np.log10(x),np.log10(y), linestyle='--', color='orange', linewidth=2)
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.xscale('log')  # Set x-axis to log scale
plt.yscale('log')  # Set y-axis to log scale
plt.grid(True) ## turn on/off as needed
plt.show()
plt.close()




