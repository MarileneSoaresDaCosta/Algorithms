# python 2.7


import sys

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(str, raw_input())
    a.append(a_temp)

# print a
'''
# given the indexes of two elements on an array, switch their positions
testarray = ['a', 'b', 'c', '%', 's', 'l', 'd', '*']
print testarray
'''

def switch(array, pos1, pos2):
	array[pos1], array[pos2] = array[pos2], array[pos1]


def findCharsToSwitch(array):
	first = 0
	last = len(array) - 1
	while first != last and last > first:
		if array[first].isalpha():
			if array[last].isalpha():
				switch(array, first, last)
				first += 1
				last -= 1
			else:
				last -= 1
		else:
			first += 1
	return array
				
	
for subarray in a:
	s = "".join(findCharsToSwitch(subarray))
	print s


'''
adapted to python 3 for Geeks
#code
import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_temp = list(map(str, input()))
    a.append(a_temp)

def switch(array, pos1, pos2):
	array[pos1], array[pos2] = array[pos2], array[pos1]


def findCharsToSwitch(array):
	first = 0
	last = len(array) - 1
	while first != last and last > first:
		if array[first].isalpha():
			if array[last].isalpha():
				switch(array, first, last)
				first += 1
				last -= 1
			else:
				last -= 1
		else:
			first += 1
	return array
				
	
for subarray in a:
	s = "".join(findCharsToSwitch(subarray))
	print (s)

'''

































