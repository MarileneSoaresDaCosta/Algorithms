"""
WWC Int Prep meeting April 5, 2017
Problem 2: 
    given a stream of numbers, calculate the moving avg of the last 
    k numbers (subset of size k).
    Return the max value in the subset as well.
     - In the example below, input is a file 
     - the very first k-1 results are 'inconsistent' until the queue is 
       populated with enough data
"""
import sys
from collections import deque

class queue:
  def __init__(self, size):
    self.array = deque([0]*size)
    self.sum = 0
    self.size = size

  def push(self, item):
    self.sum -= self.array.popleft()
    self.sum += item
    self.array.append(item)
    return 1.0 * self.sum / self.size , max(self.array)

windowsize = 3
q = queue(windowsize)

f = open('nums.txt')
for line in f.readlines():
  n = int(line.strip())
  print q.push(n)

