
'''
l = 3

r = 9

a = []

if l%2 == 0:
	first = l + 1
else:
	first = l

if r%2 == 0:
	last = r
else:
	last = r + 1

for i in range(first, last, 2):
	a.append(i)

print a
'''
'''
def  balancedSum(sales):
    i = 1
    while i < len(sales):
        sliceL = sales[:i]
        sliceR = sales[i+1:]
        if sum(sliceL) == sum(sliceR):
            return i
            
        else:
            i += 1


second attempt did not work


sales = [1, 2, 3, 3]

b = [1, 2, 1]

i = 1

sliceL = []
sliceR = sales
while i < len(sales):
	sliceL.append(sales[i-1])
	sliceR.pop()
	sliceR.pop()
	if sum(sliceL) == sum(sliceR):
		print i
		break
	else:
		i += 1
print i
'''
import operator
arr = [3,1,2,2,4, 1,1,1,4,4,4,5]

from collections import Counter

d = Counter(arr)


sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print sorted_d

for tup in sorted_d:
	for prints in range(0, tup[1]):
		print tup[0]


'''
for key, value in sorted_d.iteritems():
        for p in range(1, value):
        	print key

'''










