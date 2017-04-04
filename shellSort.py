def shellSort(alist):
    sublistcount = len(alist)//2  # sublist size, or gap
    
    while sublistcount > 0:
      for startposition in range(sublistcount):

        gapInsertionSort(alist,startposition,sublistcount)

      # print("After increments of size",sublistcount,
                                   # "The list is",alist)

      sublistcount = sublistcount // 2  # reduce size to next round

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):  
        pivotvalue = alist[i]   # starting with 2nd element of sublist     
        position = i            # initial 'potential' insertion pos
        # while we are not inserting in zero and 
        # ... the two compared items are not in order:
        while position>=gap and alist[position-gap]>pivotvalue: 
            alist[position]=alist[position-gap]   # shift right
            position = position-gap               # adjust pos

        alist[position]=pivotvalue  # insert on position found

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)




