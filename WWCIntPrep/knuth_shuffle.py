from numpy import *
a = [1,2,3,4,5]
i = len(a)-1
for i in range(1, i):
    j= random.randint(0,i)
    a[i], a[j] = a[j], a[i]
print a