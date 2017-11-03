# Queue using Two Stacks - https://www.hackerrank.com/challenges/queue-using-two-stacks

import sys

queries = []
q = int(raw_input().strip())  # number of queries
for query in xrange(q):
  line = map(int,raw_input().strip().split(' '))
  queries.append(line)

# print queries

S1 = []
S2 = []
for query in queries:
  if query[0] == 1:
    S1.append(query[1])

  elif query[0] == 2:
    if S2 == []:
      while S1 != []:
        S2.append(S1.pop())
      S2.pop()
    else:
      S2.pop()

  else:
    if S2 != []:
      print S2[-1]
    else:
      print S1[0]



"""
Sample Input

10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2


10
1 76
1 33
2
1 23
1 97
1 21
3
3
1 74
3

expected output:
33
33
33

"""