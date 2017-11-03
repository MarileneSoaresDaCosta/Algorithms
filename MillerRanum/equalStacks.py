# https://www.hackerrank.com/challenges/equal-stacks
"""
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in such a way as to maximize the height.

Note: An empty stack is still a stack.

Input Format

The first line contains three space-separated integers, n1, n2, and n3, describing the respective number of cylinders in stacks 1, 2, and 3. The subsequent lines describe the respective heights of each cylinder in a stack from top to bottom:


Output Format
Print a single integer denoting the maximum height at which all stacks will be of equal height.
"""


import sys
from collections import deque


n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))


def convertToDeque(stack):
    outD = []
    acc = 0
    for num in stack[::-1]:
      acc += num
      outD.append(acc)
    return deque(outD)

h1 = convertToDeque(h1)
h2 = convertToDeque(h2)
h3 = convertToDeque(h3)

# print h1
# print h2
# print h3

stop = False 
while h1[-1] != h2[-1] or h2[-1] != h3[-1] and stop == False:
    # print 'h1, h2, h3', h1, h2, h3
    if h1[-1] > h2[-1] or h1[-1] > h3[-1]:
        if len(h1) == 1:  # down to last one, still no solution
          stop = True  # this avoids 'underflow': pop an empty stack
          break
        else:
          # print "pop h1[-1]",  h1[-1]
          h1.pop()

    elif h2[-1] > h1[-1] or h2[-1] > h3[-1]:
        if len(h2) == 1:
          stop = True
          break
        else:
          # print "pop h2[-1]", h2[-1]
          h2.pop()
          
    elif h3[-1] > h2[-1] or h3[-1] > h1[-1]:
        if len(h3) == 1:
          stop = True
          break
        else:
          # print "pop h3[-1]", h3[-1]
          h3.pop()
if stop == True:
  print 0
else: 
  print h1[-1] # the last remaining in h1 == h2 == h3



"""
Input
5 3 4
3 2 1 1 1
4 3 2
1 1 4 1


3 3 3
1 2 3
10 20 30
100 200 300
"""













