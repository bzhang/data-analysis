#! /usr/local/bin/python
import os, glob, struct, pickle
import numpy as np
from math import sqrt
import re
import matplotlib.pyplot as plt

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
	
def save_sex():
	global fitness_2000_sex, mutator_strength_2000_sex, n_dele_2000_sex, n_bene_2000_sex
	global fitness_3000_sex, mutator_strength_3000_sex, n_dele_3000_sex, n_bene_3000_sex
	global fitness_4000_sex, mutator_strength_4000_sex, n_dele_4000_sex, n_bene_4000_sex
	global fitness_5000_sex, mutator_strength_5000_sex, n_dele_5000_sex, n_bene_5000_sex
	global base_mu
	file = open("state_sex",'w')
	data = {'fitness_2000_sex':fitness_2000_sex,
			'fitness_3000_sex':fitness_3000_sex,
			'fitness_4000_sex':fitness_4000_sex,
			'fitness_5000_sex':fitness_5000_sex,
			'mutator_strength_2000_sex':mutator_strength_2000_sex,
			'mutator_strength_3000_sex':mutator_strength_3000_sex,
			'mutator_strength_4000_sex':mutator_strength_4000_sex,
			'mutator_strength_5000_sex':mutator_strength_5000_sex,
			'n_dele_2000_sex':n_dele_2000_sex,
			'n_dele_3000_sex':n_dele_3000_sex,
			'n_dele_4000_sex':n_dele_4000_sex,
			'n_dele_5000_sex':n_dele_5000_sex,
			'n_bene_2000_sex':n_bene_2000_sex,
			'n_bene_3000_sex':n_bene_3000_sex,
			'n_bene_4000_sex':n_bene_4000_sex,
			'n_bene_5000_sex':n_bene_5000_sex,
			'base_mu':base_mu
			}
	pickle.dump(data, file)		
	file.close()

def restore_sex():
	global fitness_2000_sex, mutator_strength_2000_sex, n_dele_2000_sex, n_bene_2000_sex
	global fitness_3000_sex, mutator_strength_3000_sex, n_dele_3000_sex, n_bene_3000_sex
	global fitness_4000_sex, mutator_strength_4000_sex, n_dele_4000_sex, n_bene_4000_sex
	global fitness_5000_sex, mutator_strength_5000_sex, n_dele_5000_sex, n_bene_5000_sex
	global base_mu
	file = open("state_sex",'r')
	data = pickle.load(file)
	file.close()
	fitness_2000_sex = data['fitness_2000_sex']
	fitness_3000_sex = data['fitness_3000_sex']
	fitness_4000_sex = data['fitness_4000_sex']
	fitness_5000_sex = data['fitness_5000_sex']
	mutator_strength_2000_sex = data['mutator_strength_2000_sex']
	mutator_strength_3000_sex = data['mutator_strength_3000_sex']
	mutator_strength_4000_sex = data['mutator_strength_4000_sex']
	mutator_strength_5000_sex = data['mutator_strength_5000_sex']
	n_dele_2000_sex = data['n_dele_2000_sex']
	n_dele_3000_sex = data['n_dele_3000_sex']
	n_dele_4000_sex = data['n_dele_4000_sex']
	n_dele_5000_sex = data['n_dele_5000_sex']
	n_bene_2000_sex = data['n_bene_2000_sex']
	n_bene_3000_sex = data['n_bene_3000_sex']
	n_bene_4000_sex = data['n_bene_4000_sex']
	n_bene_5000_sex = data['n_bene_5000_sex']
	base_mu = data['base_mu']

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

restore_sex()
f2k_sex_mean, f2k_sex_CI = list_mean_CI(fitness_2000_sex)
f3k_sex_mean, f3k_sex_CI = list_mean_CI(fitness_3000_sex)
f4k_sex_mean, f4k_sex_CI = list_mean_CI(fitness_4000_sex)
f5k_sex_mean, f5k_sex_CI = list_mean_CI(fitness_5000_sex)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.errorbar(np.log10(base_mu), f2k_sex_mean, yerr = f2k_sex_CI, fmt = '-')
plt.show()