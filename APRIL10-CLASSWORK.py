#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             APRIL 10
###				Nikiphoros Vlastos
###             
#				Fourier Analysis, Transform, Series... PART II
###########################################

# Fourier Tranform is more used than Fourier Series
# Transforms between frequaency and time domains

# How well do certain sinosoidal waves fit the frequency in the time domain. In the Frequency domiain it is the sinosoidals that fit well that are the high peaks

# Fourier Transform is reversible\

# Computational cost (and then time) grows quadrativally with discrete fourier transform so we usually use fast fourier transform O(N logN) compared to O(N^2)

# There are multiple Fast Fourier Transform Algorithms
# Radix-2 Cooley-Tukey (for powers of 2)
# Bluestein

# Have lots of versions because some are better for some things, others are better for other things


# You can do discrete cosine/sine transformation (where you only use cosine or sine)


# MOST OF THE ACTUAL CODING WORK FROM TODAY CAN BE FOUND IN THE ft_demo.py and ft_timing.py files in my GitHub if you're looking for proof of classwork from today