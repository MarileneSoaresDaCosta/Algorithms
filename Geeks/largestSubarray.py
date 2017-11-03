#!/usr/bin/env python

# assuming array of distinct integers & never empty
a = [1, 56, 58, 57, 90, 92, 91, 93, 94]
# a = [1, 56, 58, 57, 90, 92, 91]
curr = 0
last = curr + 1

a.sort()
print a

subarray = []
largestSub = 0

subsize = 1

while last < len(a):
	print 'curr ' , curr, 'last ', last
	if a[last] - a[curr] == 1:     # contiguous
		# print 'subsize', subsize
		subsize += 1
		curr += 1
		last += 1
		if subsize > largestSub:
			largestSub = subsize
		
	else:
		subsize = 1
		# print 'not cont and subsize ', subsize
		
		curr = last
		last += 1

	if subsize > largestSub:
		# print 'subsize', subsize
		largestSub = subsize

print 'largestSub out', largestSub




		