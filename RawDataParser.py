#! /usr/local/bin/python
import os, glob, struct, pickle

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

# data_path = "/Volumes/BigTwins/MutatorModelData/"
# output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
data_path = "/Users/bingjun/Documents/MutatorModel/"
output_path = "/Users/bingjun/Dropbox/MutatorModel/Results/"
os.chdir(data_path)
dirs = glob.glob("MutCount_*_G5000*")
print(os.getcwd())
print(len(dirs))

n_gen = 5000
# counter = len(dirs)
for dir_name in dirs:
# if counter > 0:
	os.chdir(dir_name)
	print(dir_name)	
	files = glob.glob("*.txt")
	# n_file = len(files)
	fitness_pop = map(list,[[]]*n_gen)
	mutator_strength_pop = map(list,[[]]*n_gen)
	n_dele_pop = map(list,[[]]*n_gen)
	n_bene_pop = map(list,[[]]*n_gen)
	for file_name in files:
	# if n_file > 0:
		file = open(file_name,'rb')
		print(file_name)
		file.readline()
		records = [record for record in file.read().split('\n') if record]
		for i in range(0,n_gen):
			# print(fitness_pop[i])
			record = records[i].split()
			fitness_pop[i].append(record[1])
			mutator_strength_pop[i].append(record[3])
			n_dele_pop[i].append(record[5])
			n_bene_pop[i].append(record[7])
		file.close()
		# print(fitness_pop)
		# n_file -= 1
	# counter -= 1		
# else:
# 	break
	save_data()
	os.chdir("..")

print(fitness_pop[1])
	
	