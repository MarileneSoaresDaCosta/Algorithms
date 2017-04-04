# # testing itertools
# n = 10
# r = 4
# indices = range(n)
# cycles = range(n, n-r, -1)

# print indices
# print cycles

"""
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    print 'cycles', cycles, 'indices', indices
    print 'first', tuple(pool[i] for i in indices[:r])
    
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                print '2nd', tuple(pool[i] for i in indices[:r])
                break
        else:
            return 


arr = '012'
print permutations(arr, 2)
"""

import random

# arr = list(range(3))
# print arr
# random.shuffle(arr)
# print arr



"""
interview prep - problem 1 - warm up - given n, return its index
"""
"""
n = 5
arr = [1, 5, 10, 40, 50, 100]

# using built-in function

if n in arr:
  print arr.index(n)


# without built-in function
found = -1
for i in range(len(arr)):
  if arr[i] == n:
    found = i

if found == -1:
  print 'not found'
else:
  print 'index is: ', found
"""

"""
problem 2 - binary search
"""
"""
n = 5
arr = [1, 5, 10, 40, 50, 100]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
    41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def foo(arr, target):
  min = 0
  max = len(arr)-1
  while max >= min:
    guess = (max + min) / 2
    print guess
    if arr[guess] == target:
      return guess
    elif arr[guess] < target:
      min = guess + 1
      print 'new min', min
    else:
      max = guess - 1
      print 'new max', max
  return -1


print foo(primes, 73)

"""

"""
problem 3 - intersection of two arrays
"""
"""
lst1 = [1, 5, 10, 5, 40, 50, 5, 100, 17, 97]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
    41, 43, 47, 53, 59, 61, 67, 71, 5, 5, 73, 79, 83, 89, 97]


def foo(a1, a2):
  res = []
  if len(a1) < 1 or len(a2) < 1:
    return res
  else:
    for i in range(len(a1)):
      if a1[i] in a2:
        res.append(a1[i])
  return set(res)

print foo(lst1, primes)

"""

""" 
problem 4 - reverse array in place

"""
lst1 = [1, 5, 10, 5, 40, 50, 5, 100, 17, 97, 1000]
lst2 = [1, 2, 3]

def rev(arr):
  n = len(arr)
  # print n
  if n < 1:
    return arr
  else:
    for i in range(n/2):
      # print 'arr[i], arr[n -1 - i]', arr[i], arr[n -1 - i]
      arr[i], arr[n -1 - i] = arr[n -1 - i], arr[i]
      # print 'after', arr[i], arr[n -1 - i]
    return arr

print rev(lst1)
print rev(lst2)






















