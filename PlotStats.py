#! /usr/local/bin/python
import os, glob, struct, pickle
import numpy as np
from math import sqrt
import re
import matplotlib as plt
import util

# data_path = "/Volumes/BigTwins/MutatorModelData/"
# output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
data_path = "/Users/bingjun/Documents/MutatorModel/"
output_path = "/Users/bingjun/Dropbox/MutatorModel/Results/"
os.chdir(data_path)
dirs = glob.glob("MutCount_*_R0.0_*G5000*_MutaMR0.0*")
# dirs=glob.glob("MutCount*_R0.0_*_MutaMR0.0_*")
print(os.getcwd())
print(len(dirs))

regexp=re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_"
				  r"_G(?P<nG>[\d]+)_")
for dir_name in dirs:
	result = regexp.search(dir_name)
	base_mu = float(result.group('mu'))
	n_gen = int(result.group('nG'))
	
	util.restore_mean_CI()
	fig = plt.figure()
	errorbar(range(1,n_gen+1),fitness_mean,fitness_CI,fmt='ro',ecolor='gray',capsize='0')
	fig.savefig(dir_name.png)
