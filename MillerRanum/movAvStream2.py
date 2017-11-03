
import sys
from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.__size = size
        self.__sum = 0
        self.__q = deque([])

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.__q) == self.__size:
            self.__sum -= self.__q.popleft()
        self.__sum += val
        self.__q.append(val)
        print self.__q
        return 1.0 * self.__sum / len(self.__q)

print 'enter data and q to quit'
n = raw_input().strip()

m = MovingAverage(3)
stop = False
print 
while not stop: 
  if n == 'q':
    stop = True
    print 'end of process'
  else: 
    n = int(raw_input().strip())
    print m.next(n)
print 'end'


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

  