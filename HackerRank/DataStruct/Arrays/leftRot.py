import sys

n,d = raw_input().strip().split(' ')
n,d = [int(n),int(d)]


arr = map(int, raw_input().strip().split(' '))

for rot in range(d):
  t = arr.pop(0)
  arr.append(t)

# output format: single line o n space-sep. integers of updated array

for elem in arr:
  print elem,

