"""
def hanoi(n, source, helper, target):
    # print "hanoi( ", n, source, helper, target, " called"
    if n > 0:
        print 'n = ', n
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        print 'called h (n-1, s, t, h)'
        # move disk from source peg to target peg
        if source[0]: # smart way to check if list is empty with no errors **
            print 'source[0] = ', source[0]
            disk = source[0].pop()
            print "moving " + str(disk) + " from " + source[1] + " to " + target[1]
            target[0].append(disk)
            print 'source[0] = ', source[0]
            print 'target[0] = ', target[0]
            print 'helper[0] = ', helper[0]
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        print 'called h (n-1, h, s, t)'
        
source = ([2,1], "source")  # ** by using a set where the first el is the list
target = ([], "target")
helper = ([], "helper")
hanoi(len(source[0]),source,helper,target)

print source, helper, target
"""
"""
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","B","C")

setA = ([], 'nameset')

if setA[0]:
  print 'zero works'
else:
  print 'no zero'


setB = ([], 'nameset')


"""
def hanoi(n, A, B, C):
    
    if n > 0:
        print 'n = ', n
        # move tower of size n - 1 to B:
        hanoi(n - 1, A, C, B)
        
        # move disk from source peg to target peg
        if A[0]: # smart way to check if list is empty with no errors **
            print 'A[0] = ', A[0]
            print 'B[0] = ', B[0]
            print 'C[0] = ', C[0]
            disk = A[0].pop()
            print "moving " + str(disk) + " from " + A[1] + " to " + C[1]
            C[0].append(disk)
          
        # move tower of size n-1 from B to C:
        hanoi(n - 1, B, A, C)
        
        
A = ([2,1], "A")  # ** by using a set where the first el is the list
C = ([], "C")
B = ([], "B")
hanoi(len(A[0]),A,B,C)

print A, B, C

