import time

# decorators wrap a function, modifying its behavior.
def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper



# fibonacci tabulated

def fib(n):
  arr = [0]* (n+1)

  # base case
  arr[1] = 1

  # calculate and store
  for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]
  return arr[n]

# print fib(9)

# print fib(20)

# print fib(101)



# fib memoized, unlimited

# print 'Fib memoized, unlimited'

from functools import wraps

# general decorator that memoizes a recursive function
def memo(func):
  # use a dictionary as cache to avoid limits and fill on demand
  cache = {}
  @wraps(func)
  def wrap(*args):
    if args not in cache:
      cache[args] = func(*args)
    return cache[args]
  return wrap

@memo
def fib(n):
  if n < 2:
    return 1
  return fib(n - 1) + fib(n - 2)

# print fib(100)


"""
Hetland, ch 8 Longest Increasing Subsequence (LIS) problem
"""
# Memoized Recursive Solution for LIS 
def rec_lis(seq): 
  t1 = time.time() 
  @memo
  def L(cur):                               # Longest ending at seq[cur]
    res =1                                  # Length is at least 1  
    for pre in range(cur):                  # Potential predecessors                
      if seq[pre] <= seq[cur]:              # A valid (smaller) predec.
        res = max(res, 1 + L(pre))          # Can we improve the solution?         
    return res 
  t2 = time.time()                             
  return max(L(i) for i in range(len(seq))),  "Time it took to run the function: " + str((t2 - t1)) 

inputlist = [10, 22, 9, 33, 21, 50, 41, 60, 80]

print  rec_lis(inputlist)
print inputlist


# Basic Iterative Solution for LIS

def basic_lis(seq):
  t1 = time.time()       
  L = [1] * len(seq)
  for cur, val in enumerate(seq):
    for pre in range(cur):
      if seq[pre] <= val:
        L[cur] = max(L[cur], 1 + L[pre])
  t2 = time.time()
  return max(L),  "Time it took to run the function: " + str((t2 - t1)) 


print basic_lis(inputlist)


from bisect import bisect

def lis(seq):
  end = []
  for val in seq:
    idx = bisect(end, val)
    if idx == len(end):
      end.append(val)
    else:
      end[idx] = val
    return len(end)

print 'with bisect'
print lis(inputlist)    


def gLis(arr):
  t1 = time.time()   
  n = len(arr)
  lis = [1] * n
  for i in range(1, n):
    for j in range(0, i):
      if arr[i] > arr[j] and lis[i] < lis[j] + 1:
        lis[i] = lis[j]+ 1
        # print lis
  t2 = time.time()      
  return max(lis), "Time it took to run the function: " + str((t2 - t1)) 

print 'gLis'
print gLis(inputlist)



def subsequence(seq):
    t1 = time.time() 
    if not seq:
        return seq
    M = [None] * len(seq)    # offset by 1 (j -> j-1)
    P = [None] * len(seq)

    # Since we have at least one element in our list, we can start by 
    # knowing that the there's at least an increasing subsequence of length one:
    # the first element.
    L = 1
    M[0] = 0

    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        # Binary search: we want the largest j <= L
        #  such that seq[M[j]] < seq[i] (default j = 0),
        #  hence we want the lower bound at the end of the search process.
        lower = 0
        upper = L

        # Since the binary search will not look at the upper bound value,
        # we'll have to check that manually
        if seq[M[upper-1]] < seq[i]:
            j = upper

        else:
            # actual binary search loop
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower    # this will also set the default value to 0

        P[i] = M[j-1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j+1)

    # Building the result: [seq[M[L-1]], seq[P[M[L-1]]], seq[P[P[M[L-1]]]], ...]
    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]
        res = result[::-1]
        t2 = time.time() 
    return len(res), res,  "Time it took to run the function: " + str((t2 - t1))

print 'O(NlogN)'
print subsequence(inputlist)