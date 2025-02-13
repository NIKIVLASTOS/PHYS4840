



##### LECTURE: How to load a data file ##################

#### Options

## PANDAS
# import pandas as pd
# importated data are not automatically np arrays
# relies on files being oranized in a specific way
# to turn to arrays use 'blue=blue.to_numpy()'

## np.loadtxt
# Data is automaticaaly np arrays
# Cant deal with non-numerical data b/c casts everythin to np arrays

## line-by-line parsing
# Very flexible
# not very generalizable 




##### LECTURE: Data manipulation & visualization ##################





#################### In Class Excercise ##################


import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append('../')

filename = 'NGC6341.dat'

blue,  green, red = np.loadtxt(filename, usecols=(8, 14, 26), unpack=True)


#print(blue)
#print(green)
#print(red)

magnitude = blue
color     = blue - red



#plt.plot(color, magnitude, "ko")
#plt.savefig('terrible_figure.png')

quality_cut = np.where((green  > -99) & (blue  > -99) & (red  > -99))

fig, ax = plt.subplots( figsize=(100 , 100) )

acceptable_colors = color[quality_cut]
acceptable_Rband = magnitude[quality_cut]

plt.gca().invert_yaxis()

plt.plot(acceptable_colors, acceptable_Rband)

plt.xlabel("Color B - R", fontsize= 10)
plt.ylabel("Magnitutde B", fontsize=10)

plt.title("Hubble space telescope Data for the Globular Cluster NGC6341", fontsize=10)

#plt.plot(color, magnitude, "ko")
plt.savefig('new_figure.png')
#fig, ax = plt.subplots( figsize=(<width> , <height>) )


##### DID THIS WORK TOOOOO


















