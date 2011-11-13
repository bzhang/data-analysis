#! /usr/local/bin/python
import os, glob, struct, pickle
import numpy as np
from math import *
import re
from matplotlib.pyplot import *
from util import *

# data_path = "/Volumes/BigTwins/MutatorModelData/"
# output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
data_path = "/Users/bingjun/Documents/MutatorModel/"
output_path = "/Users/bingjun/Dropbox/MutatorModel/Results/"
os.chdir(data_path)
dirs = glob.glob("MutCount_M0.0_R1.0_G5000_N500_BeneMR1.0E-4_DeleMR0.01_BeneE1.01_DeleE0.99_MutStr2_InitMutaMR0.0_EvolMutaMR0.01_StartEvol*")
# MutCount_M0.0_R1.0_G5000_N500_BeneMR1.0E-4_DeleMR0.01_BeneE1.01_DeleE0.99_MutStr2_MutaMR0.01_Prob2M0.5_MutaE2
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
	
	# fig = figure()
	# errorbar(range(1,n_gen+1),fitness_mean,fitness_CI,color='r',capsize=0,ecolor='gray')
	# title("DeleMu = " + str(base_mu))
	# xlabel("Generation")
	# ylabel("Fitness")
	# fig.savefig("fitness_" + dir_name + ".png")
	# 
	fig = figure()
	errorbar(range(1,n_gen+1),mutator_strength_mean,mutator_strength_CI,fmt='r',ecolor='gray',capsize=0)
	yscale('log',basey=2)
	title("Sexual Populations")
	# title("DeleMu = " + str(base_mu))
	xlabel("Generation")
	ylabel("Log Mutator Strength")
	fig.savefig("Log2_Mut_" + dir_name + ".png")
	# 
	fig = figure()
	errorbar(range(1,n_gen+1),n_dele_mean,n_dele_CI,fmt='r',ecolor='gray',capsize=0)
	# title("DeleMu = " + str(base_mu))
	title("Sexual Populations")
	xlabel("Generation")
	ylabel("# of Deleterious mutations")
	fig.savefig("Dele_" + dir_name + ".png")
	
	fig = figure()
	errorbar(range(1,n_gen+1),n_bene_mean,n_bene_CI,fmt='r',ecolor='gray',capsize=0)
	title("Sexual Populations")
	# title("DeleMu = " + str(base_mu))
	xlabel("Generation")
	ylabel("# of Beneficial mutations")
	fig.savefig("Bene_" + dir_name + ".png")
	
	# fig = figure()
	fig, ax1 = subplots()
	ax2 = ax1.twinx()

	ax1.plot(range(1,n_gen+1),fitness_mean,'b-')
	ax1.set_xlabel("Generation")
	ax1.set_ylabel("Fitness")	
	ax2.plot(range(1,n_gen+1),mutator_strength_mean,'r-')
	ax2.set_yscale('log',basey=2)
	ax2.set_ylabel("Log Mutator Strength")
	# ax2.yaxis.tick_right()
	# Change the axis colors...
	ax1.tick_params(axis='y', labelcolor='blue')
	ax1.yaxis.label.set_color('blue')
	ax2.tick_params(axis='y', labelcolor='red', color='red')
	ax2.yaxis.label.set_color('red')
	title("Sexual Populations")
	
	fig.savefig("Log2_FitMut_" + dir_name + ".png")

	
	os.chdir("..")