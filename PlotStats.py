#! /usr/local/bin/python
import os, glob, struct, pickle
import numpy as np
from math import sqrt
import re
import matplotlib.pyplot as plt
from util import *

# data_path = "/Volumes/BigTwins/MutatorModelData/"
# output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
data_path = "/Users/bingjun/Documents/MutatorModel/"
output_path = "/Users/bingjun/Dropbox/MutatorModel/Results/"
os.chdir(data_path)
dirs = glob.glob("MutCount_*G5000*_MutaMR0.0*")
# dirs=glob.glob("MutCount*_R0.0_*_MutaMR0.0_*")
print(os.getcwd())
print(len(dirs))

nG_exp=re.compile(r"_G(?P<nG>\d+)_")
mu_exp=re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")

for dir_name in dirs:
	nG = nG_exp.search(dir_name)
	mu = mu_exp.search(dir_name)	
	base_mu = float(mu.group('mu'))
	n_gen = int(nG.group('nG'))
	print(base_mu)
	os.chdir(dir_name)
	
	fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI, n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI = restore_mean_CI()
	
	fig = plt.figure()
	plt.errorbar(range(1,n_gen+1),fitness_mean,fitness_CI,fmt='ro',ecolor='gray',capsize='0')
	plt.title("DeleMu = " + str(base_mu))
	plt.xlabel("Generation")
	plt.ylabel("Fitness")
	fig.savefig("fitness_" + dir_name + ".png")

	fig = plt.figure()
	plt.errorbar(range(1,n_gen+1),mutator_strength_mean,mutator_strength_CI,fmt='ro',ecolor='gray',capsize='0')
	plt.title("DeleMu = " + str(base_mu))
	plt.xlabel("Generation")
	plt.ylabel("Mutator Strength")
	fig.savefig("Mut_" + dir_name + ".png")

	fig = plt.figure()
	plt.errorbar(range(1,n_gen+1),n_dele_mean,n_dele_CI,fmt='ro',ecolor='gray',capsize='0')
	plt.title("DeleMu = " + str(base_mu))
	plt.xlabel("Generation")
	plt.ylabel("# of Deleterious mutations")
	fig.savefig("Dele_" + dir_name + ".png")

	fig = plt.figure()
	plt.errorbar(range(1,n_gen+1),n_bene_mean,n_bene_CI,fmt='ro',ecolor='gray',capsize='0')
	plt.title("DeleMu = " + str(base_mu))
	plt.xlabel("Generation")
	plt.ylabel("# of Beneficial mutations")
	fig.savefig("Bene_" + dir_name + ".png")
