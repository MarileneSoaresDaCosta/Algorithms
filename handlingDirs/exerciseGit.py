# python Exercise - github
#!/usr/bin/env python
#Python 2.7
#Harrison Ching
#hching AT ucdavis DOT edu

import os, re, sys, mmap
import matplotlib.pyplot as plt
import numpy as npy

#user prompt input
root_dir = raw_input('Enter root directory: ')
keyword = raw_input('Enter keyword to search: ')

#command line args
#root_dir = sys.argv[1]
#keyword = sys.argv[2]

#search through all files in given directory
def FileSearch(curr_dir, exp):
	#initialize count
	results = {}
	count = 0
	#list all files directory
	for filename in os.listdir(curr_dir):
		#check to make sure it is a file
		if os.path.isfile(filename):
			#open file, check for matches
			with open(filename) as f:
				ans = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
				#increment count if match found
				if ans.find(exp) != -1:
					count += 1
#				for line in f:
#					if exp in line:
#						count += 1
#						break
	#store count into array for given subdir
	results[curr_dir] = count
	
	return results[curr_dir]
	
#initialize key:value array
output = {}
#recursively walk through all dirs & call FileSearch for each subdir
for root, dirs, files in os.walk(root_dir):
	output[root] = FileSearch(root, keyword)
#output array of all the data
print output


#output bar graph using matplotlib 
graph = npy.arange(len(output))
plt.bar(graph, output.values(), align='center', width=0.5)
plt.xticks(graph, output.keys())
plt.ylim(0, max(output.values())+2)

plt.title('Number of Files with Keyword')
plt.xlabel('Subdirectory Names')
plt.ylabel('Count Values')
plt.show()

