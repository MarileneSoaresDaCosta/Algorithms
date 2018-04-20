#!/usr/bin/env python


def isUnique(string):
	string = string.lower()
	for i in range(0, len(string) - 1):
		for j in range(i+1, len(string)):
			# print(string[i], string[j])
			if string[i] == string[j]:
				# print(string[i], string[j])
				return False
	return True



# testing:
if isUnique('abcd') == True:
	print('passed [should return true]')
else:
	print ('failed [should return true')


if isUnique('abcc') == False:
	print('passed [should return false]')	
else:
	print ('failed [should return false]')