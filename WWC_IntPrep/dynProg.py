"""
Python Algorithms: Mastering Basic Algorithms in the Python Language
Magnus Lie Hetland

Chapter 8 - Tangled Dependencies and Memoization

"""

def fib(i):
  if i < 2: return 1
  return fib(i-1)+ fib(i-2)


from functools import wraps

def memo(func):
  cache = {}                      # stored subproblem solutions
  @wraps(func)                    # make wrap look like func
  def wrap(*args):                # the memoized wrapper
    if args not in cache:         # not already computed?
      cache[args] = func(*args)   # compute & cache solution
    return cache[args]            # return the cached solution
  return wrap                     # return the wrapper

fib = memo(fib)
print fib(100)

# another way of calling the function using memo as a decorator
@memo
def fib(i):
  if i < 2: return 1
  return fib(i-1)+ fib(i-2)

print fib(100)

"""
pg 179
Calculating binomial coefficients. The combinatorial meaning of C(n, k) 
is the number of k-sized subsets you can get from a set of size n.
We decompose the problem by conditioning on whether some element is included.
That is, we get one recursive call if an element is included and another 
if it is not.
If it is included, we have to count the k -1-sized subsets of the 
remaining n -1 elements, which is simply C(n -1, k -1). 
If it is not included, we have to look for subsets of size k, or C(n -1, k)

"""
@memo
def C(n, k):
  if k == 0: return 1
  if n == 0: return 0
  return C(n-1, k-1) + C(n-1, k)

print 'binomial coefficients'

print C(4, 2)
print C(10, 7)
print C(100, 50)


""" 
pg 199
"""

from collections import defaultdict

# example of using defaultdict
"""
When a letter is first encountered, it is missing from the mapping, 
so the default_factory function calls int() to supply a default 
count of zero. The increment operation then builds up the count 
for each letter. (Python documentation)
"""
s = 'mississippi'
d = defaultdict(int)
for k in s:
  d[k] += 1

print 'defaultdict example 1'
print d.items()

# example 2
x = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
b = defaultdict(list)
for k, v in x:
  b[k].append(v)

print 'defaultdict example 2'  
print b.items()

# example 3: setting the default_factory to set:
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
  d[k].add(v)

print d.items()

"""
Pascal Triangle  using a multidimensional array
"""
# from collections import defaultdict 
n, k = 4, 2
C = defaultdict(int)
for row in range(n+1):
  C[row, 0] = 1
  for col in range(1, k+1):
    C[row, col] = C[row-1, col-1] + C[row-1, col]

# print C[n,k]

print C.items()

