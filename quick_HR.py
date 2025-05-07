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

sys.path.append('/Users/uw-user/PHYS4840_labs')
import janky_MESA_parser as jank

f = '12M_history.data' ## the file you copied over from ARCC
g = 'history.data' ## the file you copied over from ARCC

mesa_data = jank.load_mesa_table(f)
mesa_data2 = jank.load_mesa_table(g)

log_Teff = mesa_data["log_Teff"]
log_L = mesa_data["log_L"]

log_Teff2 = mesa_data2["log_Teff"]
log_L2 = mesa_data2["log_L"]



fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns


axs[0].plot(log_Teff, log_L, "go-")
axs[0].set_xlabel('Log Teff (K)')
axs[0].set_ylabel('Log L')
axs[0].invert_xaxis()
axs[0].set_title("Track from 12M_pre_ms_to_core_collapse")


axs[1].plot(log_Teff2, log_L2, "bo-")
axs[1].set_xlabel('Log Teff (K)')
axs[1].set_ylabel('Log L')
axs[1].invert_xaxis()
axs[1].set_title("Track from 1M_pre_ms_to_wd")


plt.tight_layout()
plt.show()


