#!/usr/bin/env python3.8
####################################################
#
# Author: M Joyce
#
####################################################
import numpy as np
import sys
import subprocess
import matplotlib.pyplot as plt

sys.path.append('/home/mjoyce/Wyoming/teaching/PHYS4840/MESA_Class/')
import janky_MESA_parser as jank

f = 'history.data' ## the file you copied over from ARCC

mesa_data = jank.load_mesa_table(f)

log_Teff = mesa_data["log_Teff"]
log_L = mesa_data["log_L"]


fig, ax = plt.subplots(1, figsize=(8,12))
plt.plot(log_Teff, log_L, "go-")
plt.xlabel('Log Teff (K)')
plt.ylabel('Log L')
plt.gca().invert_xaxis()
plt.show()
plt.close()