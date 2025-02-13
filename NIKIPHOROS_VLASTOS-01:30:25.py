#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             January 30, 2025 
###				Nikiphoros Vlastos
###             Thursday: Lab/Lecture Day
#
###########################################

import numpy as np
#from scipy.special import sqrt


#Poll Everywhere: What does this return?
vector = [10,11,12]
def normalize_vector(vector):
	answer = np.linalg.norm(vector)
	return answer, vector
	print(answer, vector)
#It returns a tuple (both a float and integer)


####### REVIEW FROM LAST CLASS ########

### If structural issues (e.g. SYTNAX ERRORS), the code will not even run (it cant compile)
### if logic errors it breaks while running ('when it hits that line in the running code')



########## FUNCTIONS AND FLOW-OF-CONTROL #######################

########### FUNCTIONS: 
## Take one or more arguments
## Can but do not have to return a quantity
## Ideally functions should only complete one task
## Should take the minimum number of arguments possible
## Programs should be built up from individual components


##### EXCIERCISE 1 ############
#my_number = 16

#from_numpy = np.sqrt(my_number)
#from_scipy = sqrt(my_number)

#print("from_numpy")
#print("from_scipy")

#scipy is not working on my computer




##### FLOW-OF-CONTROL



########### EXCIERCISE 3 ############


#def my_function(vector):
#	a = vector[0]
#	b = vector[1]
#	c = vector[2]
#
#	return np.linalg.norm(vector)

## recall that'norm' computed the square root of the sum of the squares of vector components

#vector = [1,2,3,4]
#print(my_function(vector))


### THE ANSWER IS 3.7416573867739413

### IF YOU GIVE A VECTOR OF 2:
# GET THE ERROR: IndexError: list index out of range

### IF YOU GIVE A VECTOR OF 4:
# GET AN ANSWER OF 5.477225575051661




########### EXCIERCISE 3 ############
import my_function_lib as mfl


vector = [1,2,3]
print( mfl.my_function(vector))








