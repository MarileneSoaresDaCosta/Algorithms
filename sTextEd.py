import sys

operations = []
Q = int(raw_input().strip())
for op in xrange(Q):
  line = raw_input().strip().split(' ')
  operations.append(line)


# print operations
# print

s = ''
history = []
history.append(s)

for line in operations:
  
  if line[0] == '1':
    for ch in line[1]:
      s = s + ch
    history.append(s)
    # print 's after adding', s
    # print 'history after adding', history


  elif line[0] == '2':
    k = int(line[1])
    del_index = len(s) - k
    s = s[0:del_index]
    history.append(s)
    # print 's after deleting', s
    # print 'history after deleting', history

  elif line[0] == '3':
    k = int(line[1])
    print s[k-1]

  else:
    history.pop()
    # print 'history after undo', history
    s = history[-1]
    # print 's after undo', s


""" sample input
8
1 abc
3 3
2 3
1 xy
3 2
4 
4 
3 1


alt
5
1 abc
2 3
1 xy
4 
4 

2
1 abc
3 3

3
1 abcdefghijklmnop
3 3
4



n = int(input())

mystring = ""
history = []

for i in range(n):
    myinput = input().strip().split(' ')
    
    if myinput[0] == '1':
        history.append(mystring)
        mystring = mystring + myinput[1]

    elif myinput[0] == '2':
        history.append(mystring)
        delpos = int(myinput[1])
        mypos = len(mystring) - delpos
        mystring = mystring[0:mypos]

    elif myinput[0] == '3':
        mypos = int(myinput[1]) - 1
        print(mystring[mypos])

    else:
        mystring = history.pop()

"""

   