#!/usr/bin/env python
import os
import glob
import shutil 

# print("Path at terminal when executing this file")
# print(os.getcwd() + "\n")

# print("This file path, relative to os.getcwd()")
# print(__file__ + "\n")

# print("This file full path (following symlinks)")
# full_path = os.path.realpath(__file__)
# print(full_path + "\n")

# print("This file directory and name")
# path, filename = os.path.split(full_path)
# print(path + ' --> ' + filename + "\n")

# print("This file directory only")
# print(os.path.dirname(full_path))


# print "Check if a certain directory is in the cwd:"
# root_dir = raw_input('Enter the root directory: ')


rootName = 'testDirRoot'

def createDir(name):
	if os.path.isdir(name):
		print 'this dir already exists'
		# exit()
	else:
		print 'creating new dir'
		os.mkdir(name)
		if os.path.isdir(name):
			print 'now the dir has been created'

createDir(rootName)

# defining names of subdirs
subdirList = []

for i in range(1,4):
	subdirList.append(rootName + "/sub" + str(i))
for subdir in subdirList:
	createDir(subdir)

# print created directories 
print 'checking out list of subdirs:'
for path, subdirs, files in os.walk(rootName):
	print path

not_keywords = "string for all files"
keywords = "alpha_TESTResult.txt caterpillar CaTeRpIlLaR"

# creates files with keywords
n = 5
for subdir in subdirList:
	for i in range(1, n):
		filename = "haskeys" + str(i) + ".txt"
		# print 'filename: ', filename
		filepath = os.path.join(subdir, filename)
		with open(filepath, "w") as f:
			f.write(keywords)
			f.close
		filename = "haskeys"
		# print 'n ', n
	n += 1

# creates files without keywords
n = 4
for subdir in subdirList:
	for i in range(1, n):
		filename = "nokeys" + str(i) + ".txt"
		# print 'filename: ', filename
		filepath = os.path.join(subdir, filename)
		with open(filepath, "w") as f:
			f.write(not_keywords)
			f.close
		filename = "nokeys"
	n += 1

# create empty directory under the root
createDir(rootName + "/Empty")



def removeDir(path):
	if os.path.isdir(path):
		shutil.rmtree(path, ignore_errors=True)

	else:
		print "Not a valid directory"

removeDir(rootName + "/Empty")

