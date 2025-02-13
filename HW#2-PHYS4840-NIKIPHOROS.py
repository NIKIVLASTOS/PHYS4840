#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
##########################################
#
###             HOMEWORK #2
###				Nikiphoros Vlastos
###             
#				
###########################################

####### PROBLEM 0 (REST OF LAB FROM FEB 6) #################

##PARTS OF THE CODE for this PROBLEM WERE TAKEN FROM THE FILE: Feb-6-2024-NIKIPHOROS.py

### THIS IS THE CODE DR. JOYCE GAVE OF FOR THE 'BAD FIGURE' ###
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append('../')
import nikiphoros_functions_lib as mfl


filename = 'NGC6341.dat'

## # Col.  9: F336W calibrated magnitude
## # Col. 15: F438W calibrated magnitude
## # Col. 27: F814W calibrated magnitude

blue, green, red = np.loadtxt(filename, usecols=(8, 14, 26), unpack=True)

magnitude = blue
color     = blue - red

#plt.plot(color, magnitude, "ko")
#plt.savefig('terrible_figure.png')

#########################################################
### CREATING THE NEW ('IMPROVED') FIGURE ###
#########################################################

filename = 'NGC6341.dat'

# Load data (WHEN I LOOKED IT SAID MEMBERSHIP PROBABLILITY WAS IN THE 33 COL of the .dat file)
blue, green, red, membership_prob = np.loadtxt(filename, usecols=(8, 14, 26, 32), unpack=True)

# Exclude values marked as -99 or smaller as dr.joycce said
quality_cut = np.where((blue > -99) & (green > -99) & (red > -99) & (membership_prob > 0))

# Filter valid data
acceptable_colors = (blue - red)[quality_cut]
acceptable_magnitudes = blue[quality_cut]
acceptable_probs = membership_prob[quality_cut]

#  figure size
fig, ax = plt.subplots(figsize=(6, 8))

# THIS WILL Plot THE NEW DATA (HASHTAGGED OUT ONCE ADDED COLOR CODING)
#ax.plot(acceptable_colors, acceptable_magnitudes, marker='o', linestyle='', color='black', markersize=3, alpha=0.6)

# Scatter plot with color-coded membership probability
sc = ax.scatter(acceptable_colors, acceptable_magnitudes, c=acceptable_probs, cmap='viridis', s=10, alpha=0.6)


# Add the colorbar to the plot
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label("Membership Probability", fontsize=12)

# Invert y-axis (As dr. Joyce said)
ax.invert_yaxis()

# Label axes
ax.set_xlabel("COLOR: B-R", fontsize=12)
ax.set_ylabel("MAGNITUDE: B", fontsize=12)
ax.set_title("Hubble Space Telescope Data for \n the Globular Cluster NGC6341", fontsize=14)

# Set  limits
ax.set_xlim(-2, 5)
ax.set_ylim(25, 13.1)  # Remember, y-axis is inverted

 #Save the  figure (HASHTAGGED OUT SO NEXT STEP I CAN SEE THE PLOT)
#plt.savefig('improved_figure.png', dpi=300, bbox_inches='tight')

# Show the plot(HASHTAGGED OUT SO NEXT STEP I CAN SEE THE PLOT)
#plt.show()


#########################################################
####### PROBLEM 1  ################# IF YOU GO TO Feb-13-LABDAY.py in my Github you have my submission for this problem, This will load a crude version that was done prior to class when I did not have all the instructions
#########################################################

# Load MIST data
filename_mist = 'MIST_v1.2_feh_m1.75_afe_p0.0_vvcrit0.4_HST_WFPC2.iso.cmd'


blue, green, red, membership_prob = np.loadtxt(filename, usecols=(8, 14, 26, 32), unpack=True)

log_age, mist_f336w, mist_f814w = np.loadtxt(filename_mist, usecols=(1,12,20), unpack=True)  # LOG AGE (column 2), F336W magnitude (column 13), # F814W magnitude (column 21)

print(log_age[:5],mist_f336w[:5], mist_f814w[:5])  

linear_age = np.power(10, log_age) #turn log_age into linear age

print(linear_age)

# Exclude values marked as -99 or smaller as Dr. Joyce said
quality_cut_mist = (mist_f336w > -99) & (mist_f814w > -99) & (linear_age >= 12e9) & (linear_age <= 14e9)

# quality cut
mist_f336w = mist_f336w[quality_cut_mist]
mist_f814w = mist_f814w[quality_cut_mist]


mist_colors = mist_f336w - mist_f814w
mist_magnitudes = mist_f336w

# Set up the figure for plotting
fig, ax = plt.subplots(figsize=(6, 8))

# Plot NGC6341 data
sc = ax.scatter(acceptable_colors, acceptable_magnitudes, c=acceptable_probs, label='NGC6341', cmap='viridis', s=10, alpha=0.6)
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label("Membership Probability", fontsize=12)

# Overlay the MIST isochrone model
ax.scatter(mist_colors, mist_magnitudes, color='red', label='MIST Isochrone', s=10, alpha=0.6)


# labels and title
ax.set_xlabel("COLOR: B - R", fontsize=12)
ax.set_ylabel("MAGNITUDE: B", fontsize=12)  
ax.set_title("Hubble Space Telescope Data \n and MIST Isochrone for NGC6341", fontsize=14)

# limit and apply log scale
ax.set_xlim(-4, 7.5)
ax.set_ylim(25, -12) 
#ax.set_yscale('log')  


# Show legend
ax.legend()

# Show plot
plt.show()



#########################################################
########################### PROBLEM 2 ###############################
#########################################################

import numpy as np
import matplotlib.pyplot as plt

# the function y = x^4 for all of the plots
def func(x):
    return x**4

# defines the x values over the domain -100 to 100
x = np.linspace(-100, 100, 400)



# Compute y values for the function
y = func(x)

# Compute log10 of the function (THIS SHOULD avoiding log of 0 by excluding x = 0)
y_log = np.log10(np.abs(y))

# Set up the figure with 3 subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
# Plot on a linear grid (first panel of the 3)
axs[0].plot(x, y, color='blue', label=r'$y = x^4$', lw=2)
axs[0].set_title('Linear Grid', fontsize=14)
axs[0].set_xlabel('x', fontsize=12)
axs[0].set_ylabel('y', fontsize=12)
axs[0].grid(True)
axs[0].legend()

# Plot on a log-log grid (second panel of the 3)
axs[1].loglog(x[x != 0], y[x != 0], color='green', label=r'$y = x^4$', lw=2)  # Exclude x = 0
axs[1].set_title('Log-Log Grid', fontsize=14)
axs[1].set_xlabel('x', fontsize=12)
axs[1].set_ylabel('y', fontsize=12)
axs[1].grid(True)
axs[1].legend()

# Plot log10 of the function on a linear grid (third panel of the 3)
axs[2].plot(x[x != 0], y_log[x != 0], color='red', label=r'$\log_{10}(y)$', lw=2)  # Exclude x = 0
axs[2].set_title('Logarithm of y', fontsize=14)
axs[2].set_xlabel('x', fontsize=12)
axs[2].set_ylabel(r'$\log_{10}(y)$', fontsize=12)
axs[2].grid(True)
axs[2].legend()

# layout and show the figure
plt.tight_layout()
plt.show()




#########################################################
##################### Problem 3 #######################
#########################################################


import numpy as np
import matplotlib.pyplot as plt

# Loading data using the np method Dr. Joyce showed us
filename = "sunspots.txt"
data = np.loadtxt(filename)

# Taking the data from the correct columns in the loaded file
time = data[:, 0]  # Time (months since Jan 1749)
sunspots = data[:, 1]  # Sunspot numbers

# Limit to first 1000 data points
time_1000 = time[:1001]
sunspots_1000 = sunspots[:1001]

# This will compute a running average with r = 5 for each point along the graph
r = 5
running_avg = np.convolve(sunspots_1000, np.ones(2*r + 1) / (2*r + 1), mode='valid')

# This Adjusts the time axis for running average
avg_time = time_1000[r:-r]

# Create figure with three subplots
fig, axes = plt.subplots(3, 1, figsize=(10, 12))

# Part (a): Full sunspot data
axes[0].plot(time, sunspots, color="blue", alpha=0.6)
axes[0].set_title("Sunspots Over Time (Full Data)")
axes[0].set_xlabel("Time (Months since Jan 1749)")
axes[0].set_ylabel("Sunspot Number")
axes[0].grid(True)

# Part (b): First 1000 data points
axes[1].plot(time_1000, sunspots_1000, color="green", alpha=0.6)
axes[1].set_title("Sunspots Over Time (First 1000 Data Points)")
axes[1].set_xlabel("Time (Months since Jan 1749)")
axes[1].set_ylabel("Sunspot Number")
axes[1].grid(True)

# Part (c): First 1000 data points with running average
axes[2].plot(time_1000, sunspots_1000, label="Original Data", color="blue", alpha=0.5)
axes[2].plot(avg_time, running_avg, label=f"Running Average (r={r})", color="red", linewidth=2)
axes[2].set_title("Sunspots Over Time with Running Average")
axes[2].set_xlabel("Time (Months since Jan 1749)")
axes[2].set_ylabel("Sunspot Number")
axes[2].legend()
axes[2].grid(True)

# Adjust layout and show plot
plt.tight_layout() #makes it look good
plt.show()

## WHEN I RUN THIS ON MY COMPUTER THE GIFURE PRINTS TOO BIG TO THE SCREEN SO YOU MAY HAVE THE SHRINK THIS FIGURE TO SEE THE THIRD PLOT

#########################################################
################ Problem 4 ########################
#########################################################


## 1. Navigate to your local repository
#cd /path/to/your/repo  

## 2. Ensure you are on the main branch
#git checkout main  


# MAY RETURN SOMETHING LIKE "Already on 'main'
# Your branch is up to date with 'origin/main'.""

## 3. Pull the latest changes from GitHub to avoid conflicts
#git pull origin main

# MAY RETURN SOMETHING LIKE: "Already on 'main'
#Your branch is up to date with 'origin/main'.
#uw-user@FVFD30HXP3XY PHYS4840_labs % git pull origin main 
#From https://github.com/NIKIVLASTOS/PHYS4840
# * branch            main       -> FETCH_HEAD
#Already up to date." 

## 4. Stage all changes (or specify files instead of `.`)
#git add .  

## 5. Commit changes with a message
#git commit -m "Descriptive message about the changes"  

## 6. Push the committed changes to GitHub
#git push origin main  



#########################################################
############### Problem 4b #####################
#########################################################


# THIS IS TAKEN DIRECTLY FROM Dr Joyce's Github: PHYS4840/git_instructions.sh

## (1) navigate to the repository you want to un-git in the terminal
## (2) issue the following commands:
# (3) rm -rf .git
# (4) rm -rf .gitignore


#########################################################
############### Problem 5 #####################
#########################################################

# All my files have been uploaded to Github

