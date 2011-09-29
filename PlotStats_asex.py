#! /usr/local/bin/python
import os, glob, struct, pickle
import numpy as np
from math import sqrt
import re
import matplotlib.pyplot as plt
import util	

# data_path = "/Volumes/BigTwins/MutatorModelData/"
# output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
data_path = "/Users/bingjun/Documents/MutatorModel/"
output_path = "/Users/bingjun/Dropbox/MutatorModel/Results/"
os.chdir(data_path)

util.restore_asex()
# TODO: plot into files
figure()
plt.plot(base_mu, fitness_2000_asex)
plt.xlabel('Deleterious Mutation Rate')
plt.ylabel('Fitness at 2000 Generation')
plt.show()

figure()
plt.plot(base_mu, fitness_3000_asex)
plt.xlabel('Deleterious Mutation Rate')
plt.ylabel('Fitness at 3000 Generation')
plt.show()

figure()
plt.plot(base_mu, fitness_4000_asex)
plt.xlabel('Deleterious Mutation Rate')
plt.ylabel('Fitness at 4000 Generation')
plt.show()

figure()
plt.plot(base_mu, fitness_5000_asex)
plt.xlabel('Deleterious Mutation Rate')
plt.ylabel('Fitness at 5000 Generation')
plt.show()
