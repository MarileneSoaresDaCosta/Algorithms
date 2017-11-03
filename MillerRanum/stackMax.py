# https://www.hackerrank.com/challenges/maximum-element

import sys

queries = []
n = int(raw_input().strip())
for query in xrange(n):
  line = map(int,raw_input().strip(). split())
  queries.append(line)

stack = []
maxvs = []
for q in queries:
  if q[0] == 1:   # push
    if stack == []:
      stack.append(q[1])
      maxvs.append(q[1])
    else:
      if q[1] >= maxvs[-1]:
        stack.append(q[1])
        maxvs.append(q[1])
      else:
        stack.append(q[1])

  elif q[0] == 2:   # pop
    if stack == []:
      raise Exception ('empty stack')
    else:
      if stack[-1] == maxvs[-1]:
        stack.pop()
        maxvs.pop()
      else:
        stack.pop()

  else:  # print max
    print maxvs[-1]

