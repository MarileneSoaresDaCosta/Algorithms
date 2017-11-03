from collections import deque
"""
queue = deque(["Eric", "John", "Michael"])
print queue
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print queue.popleft()           # The first to arrive now leaves
print queue.popleft()           # The second to arrive now leaves
print queue                     # Remaining queue in order of arrival
print                 


d = deque('ghi')   # make a new deque with three items
print d
d.append('j')      # add a new entry to the right side
d.appendleft('f')  # add a new entry to the left side
print d

d.pop()            # return and remove the rightmost item
print 'after d.pop():', d

d.popleft()        # return and remove the leftmost item
print 'after d.popleft():', d
print

print 'list(d): ', list(d)  # list the contents of the deque
print
print 'list(reversed(d))', list(reversed(d)) # list the contents of a deque in reverse

print 'h in d:',  'h' in d  # search the deque


d.extend('jkl')             # add multiple elements at once
print "after d.extend('jkl'): ", d  


# right rotation
d.rotate(1)
print "after right rotation ", d

# left rotation
d.rotate(-1)
print "after left rotation ", d
print

# make a new deque in reverse order
e = deque(reversed(d))               
print 'new deque in reverse order ', e

print 'clear deque and asks for pop -> error message'
e.clear()                        # empty the deque
# e.pop()                          # cannot pop from an empty deque

# extendleft() reverses the input order
e.extendleft('abc')              
print 
print e 

"""
""" Recipes """

# Return the last n lines of a file

def tail(filename, n): 
  return deque(open(filename), n)

# print tail('sonnetSh.txt', 5)



# to maintain a sequence of recently added elements by appending to the right and popping to the left:

# moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
import itertools

def moving_average(iterable, n):
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))  # ...islice(iterable, stop)
    d.appendleft(0)     # add 0 to initial deque so loop always work
    s = sum(d)          # initial sum of first 2 elem
    for elem in it:
        s += elem - d.popleft()   # eliminate first, add next elem
        d.append(elem)            # now bring next elem into slice
        print s / float(n)        # calculate moving average

print moving_average([40, 30, 50, 46, 39, 44], 3)



def delete_nth(d, n):
  d.rotate(-n)
  d.popleft()
  d.rotate(n)


b = deque('abcdefghijklmnop')
delete_nth(b, 3) 
print b








