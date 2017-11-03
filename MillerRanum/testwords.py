# testing python features

# reversing a list
l = [1, 3, 5, 6, 9]

# reversing a string
s = 'abcdefg'


# rl = l[::-1]
# print rl

# rs = s[::-1]
# print rs

# li = [9, 4, 13, 1, 2]
# print li
# li.reverse()
# print li
# li.sort()
# print li

import itertools

s = 'abcd'

p = itertools.product(s, repeat = 2)

pe = itertools.permutations(s, 2)

c = itertools.combinations(s, 2)

# print p
# print pe
# print c

# for el in p:
#   print el,
# print


# for el in pe:
#   print el,
# print

# for el in c:
#   print el,

for c in reversed(range(0, 5)):
  print c

