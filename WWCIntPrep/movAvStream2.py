"""
WWC Int Prep meeting April 5, 2017
Problem 2: 
    given a stream of numbers, calculate the moving avg of the last 
    k numbers (subset of size k).
    Return the max value in the subset as well.
"""


import sys
from collections import deque

class MovingAverage(object):
    def __init__(self, size):
        self.__size = size
        self.__sum = 0
        self.__q = deque([])

    def next(self, val):
        # while len(self.__q) < self.__size:
        #     self.next(n)
        if len(self.__q) == self.__size:
            self.__sum -= self.__q.popleft()
        self.__sum += val
        self.__q.append(val)
        print self.__q
        return 1.0 * self.__sum / len(self.__q)

print 'enter the size of the subset'
k = int(raw_input().strip())

m = MovingAverage(k)
print 'enter data and q to quit'

for i in range(k):
    n = int(raw_input().strip())
    m.next(n)
print m.next(n)




"""
input:
1 
2 
3 
4 
5 
6 
q

"""

  