#! /usr/local/bin/python
import os, glob, struct, pickle
import numpy as np

def save_data():
	global fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop
	file = open("state",'w')
	data = {'fitness_pop':fitness_pop, 
			'mutator_strength_pop':mutator_strength_pop, 
			'n_dele_pop':n_dele_pop, 
			'n_bene_pop':n_bene_pop}
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

# data_path = "/Volumes/BigTwins/MutatorModelData/"
# output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
data_path = "/Users/bingjun/Documents/MutatorModel/"
output_path = "/Users/bingjun/Dropbox/MutatorModel/Results/"
os.chdir(data_path)
dirs = glob.glob("MutCount_*_G5000*_MutaMR0.0_*")
print(os.getcwd())
print(len(dirs))

os.chdir(dirs[0])
restore_data()

fitness_pop = string_to_float(fitness_pop)
mutator_strength_pop = string_to_float(mutator_strength_pop)
n_dele_pop = string_to_float(n_dele_pop)
n_bene_pop = string_to_float(n_bene_pop)
			