import sys

N,M = raw_input().strip().split(' ')
N,M = [int(N),int(M)]


arr = [0] * (N)

# # reading and immediately adding k
# for op in range(M):
#   a, b, k = raw_input().strip().split(' ')
#   a, b, k = [int(a),int(b), int(k)]

#   for i in range(a-1, b):
#      arr[i] += k
#   # print arr

# print max(arr)



# reading and immediately adding k
for op in range(M):
  a, b, k = raw_input().strip().split(' ')
  a, b, k = [int(a),int(b), int(k)]
  arr[a-1] += k
  
  if (b-1) <= len(arr):
    arr[b-1] -= k
  # print arr

maxv = temp = 0
for i in arr:
  temp = temp + i
  # print 'temp', temp
  if maxv < temp: 
    maxv = temp

print maxv






# operations = []

# for i in xrange(M):
#   op_temp = map(int,raw_input().strip().split(' '))
#   operations.append(op_temp)

# for i in range(M):
#   for j in range(operations[i][0] - 1, operations[i][1]):
#     arr[j] = arr[j] + operations[i][2]



# print max(arr)



"""
solution from site


n, inputs = [int(n) for n in input().split(" ")]
list = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list[x-1] += incr
    if((y)<=len(list)): list[y] -= incr;
max = x = 0
for i in list:
   x=x+i;
   if(max<x): max=x;
print(max)
"""