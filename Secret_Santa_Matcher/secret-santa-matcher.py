from collections import defaultdict
from random import *
import random

filename = input("Text file name with list of participants (e.g., names.txt): ")
file = open(filename, "r")

gift_givers = []
available_names = []
receivers = []

for line in file:
	if line[-1:] == "\n":
		line = line[:-1]
	gift_givers.append(line)
	available_names.append(line)

for x in gift_givers:
	if x == "" or x == " ":
		gift_givers.remove(x)
		available_names.remove(x)

a = 0
while a < len(gift_givers):
	name = random.choice(available_names)
	if gift_givers[a] != name:
		receivers.append(name)
		available_names.remove(name)
		a += 1

i = 0
while i < len(gift_givers):
	print(gift_givers[i] + " : " + receivers[i])
	i += 1