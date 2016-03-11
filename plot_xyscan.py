#!/usr/bin/env python

""" File: plot_xyscan.py
	Author: Sarah Lindner
	Date of last change: 10.09.2014

"""
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
import pickle # save plots in pickle format which can be opened in interactive window

current_script, my_file = argv 	# get the arguments from the command line
								# by default, the executing script is also passed to
								# argv; to seperate the inpu filename, the current 
								# script is stored in a dummy variable

my_output = my_file.replace('.txt', '')

print"Plotting file: %r" % my_file

data = np.loadtxt( my_file, delimiter="\t")

ax = plt.subplot(111)

plt.gca().invert_yaxis()


plt.imshow(data, cmap='viridis', interpolation='nearest', origin='upper')
# plt.colorbar(shrink=.92)

plt.autoscale(tight = True) # suppress white space in plot

cbar = plt.colorbar(orientation = 'vertical',format = '%.2e', shrink=.92) 
cbar.ax.tick_params(labelsize=15) 


plt.title(my_output, fontsize = 23)
plt.xlabel('X-axis (pixel)', fontsize = 20)
plt.ylabel('Y-axis (pixel)', fontsize = 20)
plt.tick_params(axis = 'both', labelsize = 15)

# plt.tight_layout() # suppress chopping off labels

plt.savefig( (my_output +'.png'))

pickle.dump(ax, file((my_output +'.pickle'), 'w'))

# plt.show()
