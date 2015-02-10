""" File: plot_xyscan.py
	Author: Sarah Lindner
	Date of last change: 10.09.2014

"""
import numpy as np
import matplotlib.pyplot as plt
from sys import argv

current_script, my_file = argv 	# get the arguments from the command line
								# by default, the executing script is also passed to
								# argv; to seperate the inpu filename, the current 
								# script is stored in a dummy variable

my_output = my_file.replace('.txt', '')

print "Plotting file: %r" % my_file

data = np.loadtxt( my_file, delimiter="\t")

plt.gca().invert_yaxis()

# plt.pcolor(data)
plt.pcolor(data, vmin=0, vmax=20000)

plt.autoscale(tight = True) # suppress white space in plot

cbar = plt.colorbar(orientation = 'vertical',format = '%.2e') 
# cbar = plt.colorbar(orientation = 'vertical',format = '%.2e', vmin=0, vmax=20000) 
cbar.ax.tick_params(labelsize=15) 
# plt.jet()

plt.title(my_output, fontsize = 23)
plt.xlabel('X-axis (pixel)', fontsize = 20)
plt.ylabel('Y-axis (pixel)', fontsize = 20)
plt.tick_params(axis = 'both', labelsize = 15)

plt.tight_layout() # suppress chopping off labels

plt.savefig( (my_output +'.png'))
plt.savefig( (my_output +'.pdf'))

plt.show()
