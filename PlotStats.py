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
				n_gen = sum(1 for line in file) - 1
				print(n_gen)
				fitness_pop = map(list,[[]]*n_gen)
				mutator_strength_pop = map(list,[[]]*n_gen)
				n_dele_pop = map(list,[[]]*n_gen)
				n_bene_pop = map(list,[[]]*n_gen)
				print(file_name)
				header = file.readline()
				print(header)
				record_format = 'hdddddddd'
				record_size = struct.calcsize(record_format)				
				for i in range(0,10):
					record = file.read(record_size)					
					print(record)
					fitness_pop[i].append(record[1])
					mutator_strength_pop[i].append(record[3])
					n_dele_pop[i].append(record[5])
					n_bene_pop[i].append(record[7])
				file.close()
				print(fitness_pop)
				n_file -= 1
		counter -= 1
	else:
		break

save_data()

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
	
	