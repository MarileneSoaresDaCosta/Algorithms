from sys import stdout
# n = int(raw_input().strip())
# arr = map(int,raw_input().strip().split(' '))

# def arraySum(a):
#     sum = 0
#     for elem in a:
#         sum = sum + elem
#     return sum
    
# print arraySum(arr)

from sys import stdout
from time import sleep

# for i in range(1,10):
#     stdout.write("\r%d" % i)
#     stdout.flush()
#     sleep(1)
# stdout.write("\n") # move the cursor to the next line


# for i in range(1,10):
#   print i,


a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
A = a0,a1,a2
B = b0,b1,b2 



def compareTriples(arrayA, arrayB):
    resA = 0
    resB = 0
    for i in range(0, 3):
        if arrayA[i] > arrayB[i]:
            resA += 1
        if arrayA[i] < arrayB[i]:
            resB += 1
    
    print resA, resB
        
compareTriples(A, B)





