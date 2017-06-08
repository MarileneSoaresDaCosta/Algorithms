import sys
# n = int(raw_input().strip())
# arr = map(int,raw_input().strip().split(' '))



# def sumLarge(list):
#   sum = 0
#   for num in list:
#     # print num
#     sum = sum + num
#     # print sum
#   return sum

# n = 5
# myl = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
# print sumLarge(arr)



# def arraySum(a):
#     sum = 0
#     for elem in a:
#         sum = sum + elem
#     return sum
    
# print arraySum(arr)

# from sys import stdout
# from time import sleep

# for i in range(1,10):
#     stdout.write("\r%d" % i)
#     stdout.flush()
#     sleep(1)
# stdout.write("\n") # move the cursor to the next line


# for i in range(1,10):
#   print i,


# a0,a1,a2 = raw_input().strip().split(' ')
# a0,a1,a2 = [int(a0),int(a1),int(a2)]
# b0,b1,b2 = raw_input().strip().split(' ')
# b0,b1,b2 = [int(b0),int(b1),int(b2)]
# A = a0,a1,a2
# B = b0,b1,b2 



# def compareTriples(arrayA, arrayB):
#     resA = 0
#     resB = 0
#     for i in range(0, 3):
#         if arrayA[i] > arrayB[i]:
#             resA += 1
#         if arrayA[i] < arrayB[i]:
#             resB += 1
    
#     print resA, resB
        
# compareTriples(A, B)



# n = 4
# matrix = [[11, 2,  4,  0],
#           [4,  5,  6,  1],
#           [10, 8, -12, 2],
#           [0,  1,   2, 3]]


# n = int(raw_input().strip())
# a = []
# for a_i in xrange(n):
#     a_temp = map(int,raw_input().strip().split(' '))
#     a.append(a_temp)

# def diag(matrix):
#   sump = 0

#   for i in range(0, n):
#     sump = sump + matrix[i][i]

#   sums = 0
#   i = n - 1
#   j = 0

#   for row in matrix:
#     sums = sums + matrix[i][j]
#     i -= 1
#     j += 1

#   return abs(sump - sums)

# print diag(a)

""" plusminus """ 

# n = int(raw_input().strip())
# arr = map(int,raw_input().strip().split(' '))

# def plusMinus(N, arrayN):
#   positives = 0
#   negatives = 0
#   zeroes = 0
#   for elem in arrayN:
#     if elem > 0:
#       positives += 1
#     elif elem < 0:
#       negatives += 1
#     else:
#       zeroes += 1

#   fpos = positives/float(N)  
#   fneg = negatives/float(N)
#   fzer = zeroes/float(N)

#   print '%.6f' %fpos
#   print '%.6f' %fneg
#   print '%.6f' %fzer

# plusMinus(n, arr)


""" staircase """

# n = int(raw_input().strip())

# def Staircase(n):
#   i = 1
#   sOut = ''
#   while i <= n:
#     for sp in range(0, n-i):
#       sys.stdout.write(" ")

#     for sy in range(1, i+1):
#       sys.stdout.write("#")
      
#     i +=1 
#     print 

# Staircase(n)


""" time-conversion"""

# time = raw_input().strip()

# def timeConv(time):
#   hh = time[:2]
#   mm = time[3:5]
#   ss = time[6:8]
#   Mer = time[8:]
#   strout = ''
#   newhh = int(hh)+12

#   if Mer == 'AM':
#     if hh != '12':
#       newhh = hh
#     else:
#       newhh = '00'


#   if Mer == 'PM':
#     if hh != '12':
#       newhh = str(int(hh) + 12)
#     else:
#       newhh = '12'
    
#   strout = newhh+":"+mm+":"+ss
#   return strout

# print timeConv(time)


""" circular array rotation"""

n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))

def rotation(n, k, arr):
  b =[]
  for rot in range(0, k):
    temp = arr.pop()
    arr.insert(0, temp)
  b = arr
  return b

newarr = rotation(n, k, a)

mtest = []
for a0 in xrange(q):
  m = int(raw_input().strip())
  mtest.append(m)


for elem in mtest:
  print newarr[elem]









