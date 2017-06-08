import sys

words = []
queries = []

n = int(raw_input().strip())
for a0 in xrange(n):
  w = raw_input().strip()
  words.append(w)

q = int(raw_input().strip())
for a0 in xrange(q):
  x = raw_input().strip()
  queries.append(x)

for q in queries:
  print words.count(q)


