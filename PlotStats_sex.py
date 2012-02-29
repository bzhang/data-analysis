#! /usr/local/bin/python
import os, glob, struct, pickle
import numpy as np
from math import sqrt
import re
from matplotlib.pyplot import *
from matplotlib.axes import *
from matplotlib.numerix import arange
from matplotlib.ticker import *
from util import *


# data_path = "/Volumes/BigTwins/MutatorModelData/"
# output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
data_path = "/Users/bingjun/Documents/MutatorModel/"
output_path = "/Users/bingjun/Dropbox/MutatorModel/Results/"
os.chdir(data_path)

fitness_2000_sex,fitness_3000_sex,fitness_4000_sex,fitness_5000_sex,base_mu = restore_sex()
# TODO: plot into files
# fig = figure(figsize=(10,10))
fig,ax1 = subplots(figsize=(10,8))
matplotlib.rcParams.update({'font.size': 18})
ax1.plot(base_mu, fitness_2000_sex)
ylim(0.965,1.140)
ax1.set_yticks([0.965,1,1.035,1.07,1.105,1.14])
ax1.set_xlabel('Log Deleterious Mutation Rate',fontsize=20)
ax1.set_ylabel('Fitness at 2000th Generation',fontsize=20)
title('Sexual Population',fontsize=20)
fig.savefig("Sex_OptMR_f2k.png")

fig,ax1 = subplots(figsize=(10,8))
matplotlib.rcParams.update({'font.size': 18})
ax1.plot(base_mu, fitness_3000_sex)
ylim(0.965,1.140)
ax1.set_yticks([0.965,1,1.035,1.07,1.105,1.14])
ax1.set_xlabel('Log Deleterious Mutation Rate', fontsize=20)
ax1.set_ylabel('Fitness at 3000th Generation', fontsize=20)
title('Sexual Population', fontsize=20)
fig.savefig("Sex_OptMR_f3k.png")

fig,ax1 = subplots(figsize=(10,8))
matplotlib.rcParams.update({'font.size': 18})
ax1.plot(base_mu, fitness_4000_sex)
ylim(0.965,1.140)
ax1.set_yticks([0.965,1,1.035,1.07,1.105,1.14])
ax1.set_xlabel('Log Deleterious Mutation Rate', fontsize=20)
ax1.set_ylabel('Fitness at 4000th Generation', fontsize=20)
title('Sexual Population', fontsize=20)
fig.savefig("Sex_OptMR_f4k.png")

fig,ax1 = subplots(figsize=(10,8))
matplotlib.rcParams.update({'font.size': 18})
ax1.plot(base_mu, fitness_5000_sex)
ylim(0.965,1.140)
ylim(0.965,1.140)
ax1.set_yticks([0.965,1,1.035,1.07,1.105,1.14])
ax1.set_xlabel('Log Deleterious Mutation Rate', fontsize=20)
ax1.set_ylabel('Fitness at 5000th Generation', fontsize=20)
title('Sexual Population', fontsize=20)
fig.savefig("Sex_OptMR_f5k.png")
