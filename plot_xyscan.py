#!/usr/bin/env python

""" File: plot_xyscan.py
	Author: Sarah Lindner
	Date of last change: 10.09.2014

"""
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
import pickle # save plots in pickle format which can be opened in interactive window
import argparse
import filename_handling
import argparse

# get arguments from command line
parser = argparse.ArgumentParser()
parser.add_argument('in_file', help = 'input filename')
parser.add_argument('-lim', nargs = 2, type=int, help = 'lower and upper limits for color coding') 
args = parser.parse_args() 


def main():

	in_filestub = filename_handling.filestub( args.in_file )

	print"Plotting file: %r" % args.in_file

	data = np.loadtxt( args.in_file, delimiter="\t")

	ax = plt.subplot(111)

	plt.gca().invert_yaxis()

	if not (args.lim):
		plt.imshow(data, cmap='viridis', interpolation='nearest', origin='upper')
	if (args.lim):
		plt.imshow(data, cmap='viridis', interpolation='nearest', origin='upper', vmin=args.lim[0], vmax=args.lim[1])
	# plt.colorbar(shrink=.92)

	plt.autoscale(tight = True) # suppress white space in plot

	cbar = plt.colorbar(orientation = 'vertical',format = '%.2e', shrink=.92) 
	cbar.ax.tick_params(labelsize=15) 


	plt.title(in_filestub, fontsize = 23)
	plt.xlabel('X-axis (pixel)', fontsize = 20)
	plt.ylabel('Y-axis (pixel)', fontsize = 20)
	plt.tick_params(axis = 'both', labelsize = 15)

	# plt.tight_layout() # suppress chopping off labels

	plt.savefig( (in_filestub +'.png'))

	pickle.dump(ax, file((in_filestub +'.pickle'), 'w'))

	# plt.show()


if __name__ == '__main__':
    main()