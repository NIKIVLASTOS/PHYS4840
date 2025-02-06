#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             HOMEWORK #1 
###				Nikiphoros Vlastos
###             
#				I Probably spent 5 hours on this, but I was also reading through the textbook for help 
#				and looking up John von Neumann while doing this as well.
#
#
#				Some things have been hash tagged out so they do not all pull up when you run the file
#				I hope I labeled everything clear so you can see which questions go to which code.
#
###########################################


######### Finishing up the inclass lab from 01/30/25 so QUESTION 0 (All of the functions I wrote can be found in my nikiphoros_function_lib.py file) ############

### EXCERSISE #5 #####

from nikiphoros_functions_lib import niki_sqrt, niki_floor, niki_round, niki_min, niki_argmin

#budget = float(input("How much money do you have: "))

#cookie_change(budget)


### EXCERSISE #6 #####

#x = float(input("What number do you want the sqrt of: "))

#niki_sqrt(x)

###I tested the other functions in my terminal or in the functions file as I did not want to over clutter this file


### EXCERSISE #7 #####

import time
import numpy as np

large_data = [i for i in range(1000000, 0, -1)]  # A large descending list

#  niki_sqrt function
start_time = time.time()
niki_sqrt_result = niki_sqrt(large_data[0])
end_time = time.time()
niki_sqrt_time = end_time - start_time

#  numpy sqrt function
start_time = time.time()
numpy_sqrt_result = np.sqrt(large_data[0])
end_time = time.time()
numpy_sqrt_time = end_time - start_time

#  niki_floor function
start_time = time.time()
niki_floor_result = niki_floor(3.14159)
end_time = time.time()
niki_floor_time = end_time - start_time

# numpy floor function
start_time = time.time()
numpy_floor_result = np.floor(3.14159)
end_time = time.time()
numpy_floor_time = end_time - start_time

# niki_round function
start_time = time.time()
niki_round_result = niki_round(3.14159, 2)
end_time = time.time()
niki_round_time = end_time - start_time

# numpy round function
start_time = time.time()
numpy_round_result = np.round(3.14159, 2)
end_time = time.time()
numpy_round_time = end_time - start_time

# niki_min function
start_time = time.time()
niki_min_result = niki_min(large_data)
end_time = time.time()
niki_min_time = end_time - start_time

# numpy min function
start_time = time.time()
numpy_min_result = np.min(large_data)
end_time = time.time()
numpy_min_time = end_time - start_time

# niki_argmin function
start_time = time.time()
niki_argmin_result = niki_argmin(large_data)
end_time = time.time()
niki_argmin_time = end_time - start_time

# numpy argmin function
start_time = time.time()
numpy_argmin_result = np.argmin(large_data)
end_time = time.time()
numpy_argmin_time = end_time - start_time

print(f"niki_sqrt function time: {niki_sqrt_time:.6f} seconds")
print(f"Numpy sqrt function time: {numpy_sqrt_time:.6f} seconds")
print(f"niki_floor function time: {niki_floor_time:.6f} seconds")
print(f"Numpy floor function time: {numpy_floor_time:.6f} seconds")
print(f"niki_round function time: {niki_round_time:.6f} seconds")
print(f"Numpy round function time: {numpy_round_time:.6f} seconds")
print(f"niki_min function time: {niki_min_time:.6f} seconds")
print(f"Numpy min function time: {numpy_min_time:.6f} seconds")
print(f"niki_argmin function time: {niki_argmin_time:.6f} seconds")
print(f"Numpy argmin function time: {numpy_argmin_time:.6f} seconds")




#########################################################################################################################################
#########################################################################################################################################



####### QUESTION 1 ##########
#THIS WAS DONE ON PAPER




####### QUESTION 2 ##########


def sandwich_combo(money):                      												#THIS makes the function and takes one argument: 'money'
    prices = {'Ham': 3.65, 'Apple Brie': 4.25, 'Peanut Butter & Jelly': 3.00, 'Turkey': 3.35}	#Here I am making a dicitonary with the key being the name of the sandiwch and the value being the price
    
    best_combo = None   																		#THIS makes the variable for the best combo and sets it to 'none'
    min_change = float('inf')																	#THIS makes the variable for the minimum amount of change and makes it a float that can have infinite points
    
   
    for ham in range(int(money // prices['Ham']) + 1):											# goes through all possible values for each sandwich (whole)
        for ab in range(int(money // prices['Apple Brie']) + 1):
            for pbj in range(int(money // prices['Peanut Butter & Jelly']) + 1):
                for turkey in range(int(money // prices['Turkey']) + 1):
                    
                    
                    for half_sandwich in prices:												# goes through all possible values for each sandwich (half)
                        half_price = prices[half_sandwich] * 0.6  								# The PRice of half a sandwich is 0.6 that of a full sandwich
                        
                       
                        for has_half in [True, False]:											
                            if has_half:														# calculates the total cost of the current combination of sandwiches (including a half sandwich)
                                total = (ham * prices['Ham'] + ab * prices['Apple Brie'] + pbj * prices['Peanut Butter & Jelly'] + turkey * prices['Turkey'] + half_price)
                                               
                            else:																# calculates the total cost of the current combination of sandwiches (no half sandwich)
                                total = (ham * prices['Ham'] + ab * prices['Apple Brie'] + pbj * prices['Peanut Butter & Jelly'] +turkey * prices['Turkey'])
           
                            if total > money: 													# if the total cost of the current combination exceeds the money input it restarts
                                continue
                            
                            change = round(money - total, 2)           							# Gives the amount of change to two decimals
                            
                            
                            if change % 0.25 == 0 and change < min_change and has_half:			# sees if change is a multiple of 25 cents, less than the current minimum change, and if a half sanwich is included
                                min_change = change  											#replaces current change with the new lower change
                                best_combo = { 'Ham': ham, 'Apple Brie': ab, 'Peanut Butter & Jelly': pbj, 'Turkey': turkey,'Half': half_sandwich if has_half else None }     #replaces current best cominations with the new lower combination             
    
    return best_combo, min_change																# This returns the ultimate best combo and change

money = float(input("Enter the amount of money you have: "))
combo, change = sandwich_combo(money)
if combo:
    print("Your best combo is:", combo)
    print("The remaining change you will have is:$", change)
else:
    print("Sorry, No combination of sandwiches can be purchased with the given amount of money.")


####### QUESTION 3 ##########
####### I did excersice 2.1 be accident but will leave it in anyway ##########

from numpy import sqrt 

h = float(input("Enter the initial height of the ball:"))

g = 9.81
#s = (g * t**2)/2
t = sqrt((2 * h) / g)

print(f"The ball will hit the ground after {t:.2f} seconds.")

############################################################
######### 2.12 ########
from numpy import sqrt

primes = [2]


for n in range(3, 10001):
    is_prime = True
   
    for p in primes:
        if p > sqrt(n):
            break
        if n % p == 0:
            is_prime = False
            break
    
    if is_prime:
        primes.append(n)

print(primes)

####### 2.13 ##########

def catalan(n):
    if n == 0:
        return 1
    else:
        return ((4 * n - 2) / (n + 1)) * catalan(n - 1)

# Calculate and print C_100
print(catalan(100))

############################################################

def g(m, n):
    # Base case: if n is 0, return m
    if n == 0:
        return m
    # Recursive case: compute the GCD of n and m % n
    else:
        return g(n, m % n)

# Using the function to calculate the GCD of 108 and 192
result = g(108, 192)
print("The greatest common divisor of 108 and 192 is:", result)

##############################################################
##############################################################

# Pragraph on important Person

# Neumann János Lajos/John von Neumann (who was born in Budapest, Hungary) was a pioneering figure in computing. 
#He is possibly best known (at least from what I could find) for his development of the von Neumann architecture, 
#which remains the foundation of modern computer design. It says he was a mathematician, physicist, computer 
#scientist and engineer (so he did pretty much everything)! His model introduced the concept of a stored-program 
#computer, where both data and instructions are stored in the same memory. This then allowed for greater flexibility and efficiency. 
#Ultimately this innovation laid the groundwork for the development of general-purpose computers, which 
#in turn influenced everything from early mainframes to present day processors. Outside of pure computing, 
#von Neumann also made significant contributions to fields like game theory, quantum mechanics, and numerical analysis.
#In these other fields von Neumann is credited with playing a key role in the development of the hydrogen bomb, 
#applying his mathematical expertise to complex nuclear physics problems. And His work in game theory led to the creation 
#of the minimax theorem (I am not familiar with this), which remains fundamental in economics and strategic decision-making.








