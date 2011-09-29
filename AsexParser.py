#! /usr/local/bin/python
import os, glob, struct, pickle
import numpy as np
from math import sqrt
import re

def save_data():
	global fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop
	file = open("state",'w')
	data = {'fitness_pop':fitness_pop, 
			'mutator_strength_pop':mutator_strength_pop, 
			'n_dele_pop':n_dele_pop, 
			'n_bene_pop':n_bene_pop}
	pickle.dump(data, file)		
	file.close()

def save_mean_CI():
	global fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI
	global n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI
	file = open("state_mean_CI",'w')
	data = {'fitness_mean':fitness_mean, 
			'mutator_strength_mean':mutator_strength_mean, 
			'n_dele_mean':n_dele_mean, 
			'n_bene_mean':n_bene_mean,
			'fitness_CI':fitness_CI, 
			'mutator_strength_CI':mutator_strength_CI, 
			'n_dele_CI':n_dele_CI, 
			'n_bene_CI':n_bene_CI
			}
	pickle.dump(data, file)		
	file.close()
	
def save_asex():
	global fitness_2000_asex, mutator_strength_2000_asex, n_dele_2000_asex, n_bene_2000_asex
	global fitness_3000_asex, mutator_strength_3000_asex, n_dele_3000_asex, n_bene_3000_asex
	global fitness_4000_asex, mutator_strength_4000_asex, n_dele_4000_asex, n_bene_4000_asex
	global fitness_5000_asex, mutator_strength_5000_asex, n_dele_5000_asex, n_bene_5000_asex
	global base_mu
	file = open("state_asex",'w')
	data = {'fitness_2000_asex':fitness_2000_asex,
			'fitness_3000_asex':fitness_3000_asex,
			'fitness_4000_asex':fitness_4000_asex,
			'fitness_5000_asex':fitness_5000_asex,
			'mutator_strength_2000_asex':mutator_strength_2000_asex,
			'mutator_strength_3000_asex':mutator_strength_3000_asex,
			'mutator_strength_4000_asex':mutator_strength_4000_asex,
			'mutator_strength_5000_asex':mutator_strength_5000_asex,
			'n_dele_2000_asex':n_dele_2000_asex,
			'n_dele_3000_asex':n_dele_3000_asex,
			'n_dele_4000_asex':n_dele_4000_asex,
			'n_dele_5000_asex':n_dele_5000_asex,
			'n_bene_2000_asex':n_bene_2000_asex,
			'n_bene_3000_asex':n_bene_3000_asex,
			'n_bene_4000_asex':n_bene_4000_asex,
			'n_bene_5000_asex':n_bene_5000_asex,
			'base_mu':base_mu
			}
	pickle.dump(data, file)		
	file.close()

def restore_data():
	global fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop
	file = open("state",'r')
	data = pickle.load(file)
	file.close()
	fitness_pop = data['fitness_pop']
	mutator_strength_pop = data['mutator_strength_pop']
	n_dele_pop = data['n_dele_pop']
	n_bene_pop = data['n_bene_pop']

def string_to_float(nested_list):
	result = map(list,[[]]*len(nested_list))	
	for i in range(0,len(nested_list)):
		for j in range(0,len(nested_list[i])):
			result[i].append(float(nested_list[i][j]))
	return result

def mean_95CI(list):
	n, mean, std, se, ci = len(list), 0, 0, 0, 0
	for i in list:
		mean = mean + i
	mean = mean / float(n)
	for i in list:
		std = std + (i - mean)**2
	std = sqrt(std / float(n-1))
	se = std / sqrt(float(n))
	ci = 1.96 * se
	return mean, ci

def list_mean_CI(nested_list):
	mean_list, CI_list = [], []
	for i in nested_list:
		mean, ci = mean_95CI(i)
		mean_list.append(mean)
		CI_list.append(ci)
	return mean_list, CI_list

# data_path = "/Volumes/BigTwins/MutatorModelData/"
# output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
data_path = "/Users/bingjun/Documents/MutatorModel/"
output_path = "/Users/bingjun/Dropbox/MutatorModel/Results/"
os.chdir(data_path)
dirs = glob.glob("MutCount_*_R0.0_*G5000*_MutaMR0.0_*")
# dirs=glob.glob("MutCount*_R0.0_*_MutaMR0.0_*")
print(os.getcwd())
print(len(dirs))

fitness_2000_asex, mutator_strength_2000_asex, n_dele_2000_asex, n_bene_2000_asex = [],[],[],[]
fitness_3000_asex, mutator_strength_3000_asex, n_dele_3000_asex, n_bene_3000_asex = [],[],[],[]
fitness_4000_asex, mutator_strength_4000_asex, n_dele_4000_asex, n_bene_4000_asex = [],[],[],[]
fitness_5000_asex, mutator_strength_5000_asex, n_dele_5000_asex, n_bene_5000_asex = [],[],[],[]

base_mu = []
regexp=re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")

for dir_name in dirs:
	mu = regexp.search(dir_name)
	base_mu.append(float(mu.group('mu')))

	os.chdir(dir_name)
	print(dir_name)
	restore_data()
			
	# fitness_mean, fitness_CI = list_mean_CI(fitness_pop)
	# mutator_strength_mean, mutator_strength_CI = list_mean_CI(mutator_strength_pop)
	# n_dele_mean, n_dele_CI = list_mean_CI(n_dele_pop)
	# n_bene_mean, n_bene_CI = list_mean_CI(n_bene_pop)

	fitness_2000_asex.append(fitness_mean[2000-1])
	mutator_strength_2000_asex.append(mutator_strength_mean[2000-1])
	n_dele_2000_asex.append(n_dele_mean[2000-1])
	n_bene_2000_asex.append(n_bene_mean[2000-1])

	fitness_3000_asex.append(fitness_mean[3000-1])
	mutator_strength_3000_asex.append(mutator_strength_mean[3000-1])
	n_dele_3000_asex.append(n_dele_mean[3000-1])
	n_bene_3000_asex.append(n_bene_mean[3000-1])

	fitness_4000_asex.append(fitness_mean[4000-1])
	mutator_strength_4000_asex.append(mutator_strength_mean[4000-1])
	n_dele_4000_asex.append(n_dele_mean[4000-1])
	n_bene_4000_asex.append(n_bene_mean[4000-1])

	fitness_5000_asex.append(fitness_mean[5000-1])
	mutator_strength_5000_asex.append(mutator_strength_mean[5000-1])
	n_dele_5000_asex.append(n_dele_mean[5000-1])
	n_bene_5000_asex.append(n_bene_mean[5000-1])
		
	# save_mean_CI()
	os.chdir("..")
	
# sort lists by base_mu
base_mu = np.log10(base_mu)
inds = np.argsort(base_mu)
base_mu.sort()
fitness_2000_asex = list(np.take(fitness_2000_asex,inds))
fitness_3000_asex = list(np.take(fitness_3000_asex,inds))
fitness_4000_asex = list(np.take(fitness_4000_asex,inds))
fitness_5000_asex = list(np.take(fitness_5000_asex,inds))
mutator_strength_2000_asex = list(np.take(mutator_strength_2000_asex,inds))
mutator_strength_3000_asex = list(np.take(mutator_strength_3000_asex,inds))
mutator_strength_4000_asex = list(np.take(mutator_strength_4000_asex,inds))
mutator_strength_5000_asex = list(np.take(mutator_strength_5000_asex,inds))
n_dele_2000_asex = list(np.take(n_dele_2000_asex,inds))
n_dele_2000_asex = list(np.take(n_dele_3000_asex,inds))
n_dele_2000_asex = list(np.take(n_dele_4000_asex,inds))
n_dele_2000_asex = list(np.take(n_dele_5000_asex,inds))
n_bene_2000_asex = list(np.take(n_bene_2000_asex,inds))
n_bene_2000_asex = list(np.take(n_bene_3000_asex,inds))
n_bene_2000_asex = list(np.take(n_bene_4000_asex,inds))
n_bene_2000_asex = list(np.take(n_bene_5000_asex,inds))

save_asex()

