#! /usr/local/bin/python

import os, glob, struct, pickle
data_path = "/Volumes/BigTwins/MutatorModelData/"
output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
# dataPath = "~/Documents/MutatorModel"
# outputPath = "~/Dropbox/MutatorModel/Results/"
os.chdir(data_path)
dirs = glob.glob("MutCount_*_G5000*_MutaMR0.0_*")
print(os.getcwd())
print(len(dirs))

counter = 1
for dir_name in dirs:

	if counter > 0:
		os.chdir(dir_name)
		print(dir_name)	
		files = glob.glob("*.txt")
		n_file = 1
		for file_name in files:
			if n_file > 0:
				file = open(file_name,'rb')
				print(file_name)
				for i in range(1,11):
					print(file.readline())
				file.close()
				n_file -= 1
		counter -= 1
	else:
		break

def save_data():
	globle fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop
	file = open("state",'w')
	data = {'fitness_pop':fitness_pop, 
			'mutator_strength_pop':mutator_strength_pop, 
			'n_dele_pop':n_dele_pop, 
			'n_bene_pop':n_bene_pop}
	pickle.dump(data, file)		
	file.close()
	
def restore_data():
	globle fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop
	file = open("state",'r')
	data = pickle.load(file)
	file.close()
	fitness_pop = data['fitness_pop']
	mutator_strength_pop = data['mutator_strength_pop']
	n_dele_pop = data['n_dele_pop']
	n_bene_pop = data['n_bene_pop']
	
	