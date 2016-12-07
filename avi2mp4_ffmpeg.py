#!/usr/bin/python


###	Automatically compresses all avi files in folder using ffmpeg and repackages them as mp4 files ###


import subprocess, os

cmd = "ls"
files = subprocess.Popen(cmd, stdout = subprocess.PIPE, universal_newlines=True)
videofiles = []

for line in files.stdout.readlines():
	if line[-5:] == ".avi\n":
		videofiles.append(line[:-1])

if not videofiles:
	print("No .avi files found.")

for x in videofiles:
	os.system("ffmpeg -i %s -crf 20 %s.mp4" %(x, x[:-4]))