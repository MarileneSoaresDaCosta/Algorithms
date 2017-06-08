# https://www.hackerrank.com/challenges/fibonacci-modified

from functools import wraps


def memo(func):
  cache = {}                      # stored subproblem solutions
  @wraps(func)                    # make wrap look like func
  def wrap(*args):                # the memoized wrapper
    if args not in cache:         # not already computed?
      cache[args] = func(*args)   # compute & cache solution
    return cache[args]            # return the cached solution
  return wrap                     # return the wrapper

@memo
def mFib(t1, t2, n):
  if n == 1: 
    return t1
  if n == 2:
    return t2
  if n == 3:
    return t1 + t2**2
  return mFib(t1, t2, n-2) + (mFib(t1, t2, n-1)**2)

print 'with recursion'
print mFib(0, 1, 10)
# print mFib(0, 1, 4)
print

print 'without recursion'

# t1,t2,n = map(int, raw_input().split(" "))
t1 = 0
t2 = 1
n = 10
array = [t1, t2]
for i in range(2,n):
  item = array[i-2] + (array[i-1])**2
  array.append(item)
print array[n-1]
