#!/usr/bin/env python

'''  
Steps: 
1. get input from user - two arguments:      
1.1 directory ("root_dir"), a string
1.2 keyword ("keyword"), either a simple string or a regular expression 

2. call function walk(root_dir, keyword), which uses the function walk 
from the module os to "generate the file names in a directory tree by 
walking the tree", in this case, top-down. For each subdirectory (including
the root directory, the function walk "yields the dirpath, dirnames, and 
filenames.

traverse directory (DFS?) looking for keyword in
filenames     2.1 if child = directory, save child as path
(subdirectory) and go to next child     2.2 if it is a file, search
name for keyword     2.3 if keyword found, add number of occurences to
subdirectory dict (key:value) 3. output 1 : dict 4. output 2: graph
where X is the subdir name (key) and Y is value


'''
import sys
import os
import glob
import re
import mmap


# # getting use input
# root_dir = raw_input('Enter the root directory: ')
# keyword = raw_input('Enter keyword to search (you can use a regular expression as well): ')
'''
# simple recursive traversal that prints path+filenames
def printDirFiles(p):
	results = {}
	for child in os.listdir(p):             
		cPath = os.path.join(p, child)
		# add cPath as key to dict results
		results[cPath] = 0
		if os.path.isdir(cPath):
			printDirFiles(cPath)
		else: 
			if os.path.isfile(cPath):
				results[cPath] +=1
	print results
'''
c = "testDir"
# printDirFiles(c)
d = "/Users/marilenedacosta/Dropbox/codingExercises"
e = "/Users/marilenedacosta/Dropbox"
f = "testDir/subdir2"
g = "testDir/subdir2/sub2subEmpty"
key1 = "caterpillar"
key2 = "^[a-zA-Z]+_TESTResult.*"

'''
#counts how many files in each subdir, including the root_dir
def printSubdirs(root_dir):
	results = {}
	count = 0
	curr_dir = root_dir

	# for elem in glob.glob(os.path.join(root_dir, '*')):
	# 	print elem

	for child in glob.glob(os.path.join(root_dir, '*')):
		# print 'child... ', child
		curr_dir = os.path.dirname(child) 
		if os.path.isdir(child): 
			if os.listdir(child) == []: # the directory is empty
				curr_dir = child
				results[curr_dir] = 0
			else: 
				curr_dir = child
				printSubdirs(curr_dir)
		else:
			count += 1
			results[curr_dir] = count
	print results

# printSubdirs(d)
'''


def walk(root_dir, keyword):
	#initialize key:value array
	output = {}
	reKey = re.compile(keyword)
	#recursively walk through all dirs & call searchSubdir for each subdir
	for path, subdirs, files in os.walk(root_dir):
		output[path] = searchSubdir(path, reKey)
	#output array of all the data
	print output

# counts how many files in each subdir have keyword in their names
def searchSubdir(subdir, reKey):
	results = {}
	count = 0
	for file in glob.glob(os.path.join(subdir, '*')):
		#check to make sure it is a file
		if os.path.isfile(file):
			#open file, check for matches
			print file
			with open(file) as f:
				'''
				Calling mmap with only two arguments has the advantage of 
				keeping your code portable between Windows and Unix-like 
				platforms.
				For both the Unix and Windows versions of the function, 
				access may be specified as an optional keyword parameter
				. access accepts one of three values: ACCESS_READ, ACCESS_WRITE,
				or ACCESS_COPY to specify readonly, write-through or 
				copy-on-write memory respectively. access can be used on both 
				Unix and Windows.
				'''
				m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
				if re.search(reKey, m):
					count += 1
				# while True:
				# 	line = m.readline() 
				# 	print line 
				# 	# break
				# 	if keyword in line: 
				# 		count += 1
				# 		break
				# 	if not line:
				# 		break
				# 	m.close()
					
	#store count into array for given subdir
	results[subdir] = count
	return results[subdir]


# walk(f, key1)



'''
breaking program into 2 parts: 
f1 reading one directory at a time and 
f2 saving results into a single dictionary 
why? because the functions above create a new dict inside every recursion
'''

# testing reg expression use

inputreg = "^[a-zA-Z]+_TESTResult.*"
teststrings = ["2345_TESTResult.txt", "&_TESTResult.* doc", "123", "@3ohog34^", "^AAa_TESTResult.doc" ]

# count = 0
# for s in teststrings:
# 	print "s", s
# 	if re.search(re.compile(inputreg), s):
# 		count +=1
# 	print "count", count

# simpler test
input1 = "\w+yada.*"
s1 = "hteeyada.txt"
input1re = re.compile(input1)
if re.search(input1re,s1) != None:
	print 'match found' 
else:
	print type(re.search(input1re,s1))


'''
example

import mmap
import re
import contextlib

pattern = re.compile(r'(\.\W+)?([^.]?nulla[^.]*?\.)',
                     re.DOTALL | re.IGNORECASE | re.MULTILINE)

with open('lorem.txt', 'r') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
        for match in pattern.findall(m):
            print match[1].replace('\n', ' ')

'''

# testing os.walk

# testwalk = []
# for path, subdir, file in os.walk(c):
# 	print file
