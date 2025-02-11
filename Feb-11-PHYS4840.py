#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             Tuesday February 11, 2025
###				Nikiphoros Vlastos
###             
#				     CLASS #7: Numerical limits of Python, Optimization, Timing & Github
###########################################


## In Dr. Joyce's Gitbuh can go to git_instructions.sh to find Github help


######## LECTURE #####################

#### Python is not perfect

### Limitations
## 		Flaoting point precision
## 		memory management

#Python uses IEE 754 double-precision format
print(0.1+0.2)
print(repr(0.1+0.2))

#Q: what is happening in the second command
#A: 0.1 aqnd 0.2 do not have exact binary representations, and neither does their sum! The repr() function gives a literal representation of a variable

#Q: Why does the first command seam "OK"?
#A the print() function applies formatting, which can mask this issue! To check the exact value of your floats, use repr()


######### Mini-Excercise ##############

from math import sqrt
x = 1.0
y = 1.0 +(1e-14)*sqrt(2)

answer_1 = 1e14*(y-x)
answer_2 = sqrt(2)


print("answer1: ",answer_1)
print("answer2: ",answer_2)

Percent_difference = (answer_2 - answer_1)/answer_2

print(abs(Percent_difference)*100)




#### Python Weakness:

### Memory management and limitations

## The largest number that can be represented in IEEE 754 double-precision float is 1.8 X 10^308, which is the decimal representation of the binary number 2^1024
## The smallest number Python can do is: 

## By default, Python manages memory with automatic grabage collection
#This frees the programmer from having to manage
#memory explicity a at the cost of computation overhead


###Segfaults
## A Segfault (segmentation fault) is a low-level memory access violation that happens when 
#a program tries to acces (read or write) to a restricted memory location

#Python runs insade an interpreter that mangaes memory

#advantages of garbage collection
#	Ease of use
#	Reduces memory leaks
#	Safe from segmentation faults

#Disadvantages of C's manual memory management



### PYTHON IS SAFE, EASY NO SEGFAULTS AT THE COST OF SPEED
### C GIVE MOST CONTROL OVER MEMORY, EXTREMELY SAFE
### FROTRAN IS MOST ROBUST AGAINST LEAKS



### PYTHON Weakness: Performance & Random number generation

# Python default random number generation is not truly random


##### TIMING YOUR CODE ####


### ANOTHER MINI EXCERCISE ###



### THIS CODE IS TAKEN FROM time_tests_w_timeit.py
import timeit
import numpy as np

setup_code = """
nums = list(range(100000))
"""
list_comp_time = timeit.timeit("[x**2 for x in nums]", setup=setup_code, number=100)
map_time = timeit.timeit("list(map(lambda x: x**2, nums))", setup=setup_code, number=100)

print("List comprehension time: ","%.5f"%list_comp_time ," seconds")
print("Map function time: ",      "%.5f"%map_time       ," seconds")
print("")

#-----------------------------------------

setup_code = "nums_list = list(range(100000)); nums_set = set(nums_list)"
list_time = timeit.timeit("99999 in nums_list", setup=setup_code, number=10000)
set_time = timeit.timeit("99999 in nums_set", setup=setup_code, number=10000)

print(f"List membership test time: ", "%.5f"%list_time ," seconds")
print(f"Set membership test time: ",  "%.5f"%set_time,  " seconds")
print("")

#-----------------------------------------
########################
#
# In-class Exercise!!
#
#########################

setup_code = "import numpy as np; my_array = np.arange(100000)"

#### compare the speed of 
# 		sum([x**2 for x in range(100000)])
#               vs
#       np.sum(my_array**2)
##
## for 100 iterations, then 1000


list_comp_time1 = timeit.timeit("sum([x**2 for x in range(100000)])", setup=setup_code, number=100)
map_time1 = timeit.timeit("np.sum(my_array**2)", setup=setup_code, number=100)


list_comp_time2 = timeit.timeit("sum([x**2 for x in range(100000)])", setup=setup_code, number=1000)
map_time2 = timeit.timeit("np.sum(my_array**2)", setup=setup_code, number=1000)


print(f"List1 membership test time for 100 iterations: ", "%.5f"%list_comp_time1 ," seconds")
print(f"map1 membership test time for 100 iterations: ",  "%.5f"%map_time1,  " seconds")

print(f"List2 membership test time for 1000 iterations: ", "%.5f"%list_comp_time1 ," seconds")
print(f"map2 membership test time for 1000 iterations: ",  "%.5f"%map_time1,  " seconds")



#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################


### now we are using the time module     

import time
import numpy as np
import sys
import pandas as pd

filename = 'NGC6341.dat'

###################################################
#
# testing np.loadtxt()
#
###################################################
"""
put the action you want to time between the
star and end commands
"""

start_numpy = time.perf_counter()


blue, green, red, probability = np.loadtxt(filename,\
                 usecols=(8, 14, 26, 32), unpack=True)
print("len(green): ", len(green))


end_numpy  = time.perf_counter()

print('Time to run loadtxt version: ', end_numpy-start_numpy, ' seconds')



###################################################
#
# testing custom parser
#
###################################################
start_parser = time.perf_counter()

## Initialize lists to store the data. Note that these ARE NOT ARRAYS!!
## you cannot 'append' to an array! You must append to a list, then
## cast as an array later
blue, green, red = [], [], []


with open(filename, 'r') as file:
    for line in file:
        # Skip lines that start with '#'
        if line.startswith('#'):
            continue
        
        # Split the line into columns based on spaces
        columns = line.split()
        
        blue.append(float(columns[8]))   # Column 9 
        green.append(float(columns[14])) # Column 15 
        red.append(float(columns[26]))   # Column 27 

blue = np.array(blue)
green = np.array(green)
red = np.array(red)

print("len(green): ", len(green))

end_parser  = time.perf_counter()

print('Time to run custom parser version: ', end_parser-start_parser, ' seconds')


###################################################
#
# testing pandas
#
###################################################
start_pandas = time.perf_counter()

df = pd.read_csv(filename, delim_whitespace=True, comment='#', header=None, skiprows=54)

# Extract the columns corresponding to
# F336W, F438W, and F814W magnitudes
blue = df.iloc[:, 8]   # Column 9 
green = df.iloc[:, 14]  # Column 15 
red = df.iloc[:, 26]   # Column 27 

blue = blue.to_numpy()
green = green.to_numpy()
red = red.to_numpy()

print("len(green):", len(green))

end_pandas  = time.perf_counter()

print('Time to run pandas version: ', end_pandas-start_pandas, ' seconds')


##WHAT I AM GETTING
#len(green):  158219
#Time to run loadtxt version:  0.2071820970159024  seconds
#len(green):  158219
#Time to run custom parser version:  0.375819289998617  seconds
#len(green): 158219
#Time to run pandas version:  0.7458597089862451  seconds

