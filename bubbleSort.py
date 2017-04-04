def bubbleSort(alist):
  for passnum in range(len(alist)-1,0,-1):
    # print 'passnum', passnum
    for i in range(passnum):
      # print 'i', i
      if alist[i]>alist[i+1]:
        # temp = alist[i]
        # alist[i] = alist[i+1]
        # alist[i+1] = temp
        alist[i], alist[i+1] = alist[i+1], alist[i]

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

# short bubble modification 
# if there are no exchanges in a pass, the bubble sort stops
def shortBubbleSort(alist):
  exchanges = True
  passnum = len(alist)-1
  while passnum > 0 and exchanges:
    # print 'passnum, exchanges', passnum, exchanges
    exchanges = False   # here we set it False so that
    for i in range(passnum):
      # print 'i', i
      # print alist
      if alist[i]>alist[i+1]:
        # print 'i>i+1', alist[i], alist[i+1]
        exchanges = True    # when an exc occurs, it goes back to True
        temp = alist[i]
        alist[i] = alist[i+1]
        alist[i+1] = temp
    passnum = passnum-1

blist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(blist)
print(blist)









