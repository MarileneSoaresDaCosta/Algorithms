# https://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
# chapter 5.12 The Quick Sort

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last

   done = False
   while not done:
       # as long as leftm <= rightm and leftmvalue <= pivotvalue
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1  # increment leftmark

       # as long as rightm >= leftm and rightmvalue >= pivotvalue    
       while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
           rightmark = rightmark -1   # decrement rightmark

       if rightmark < leftmark: # when leftm and rightm switch, we're done
           done = True

       else: # when items are 'out of place', switch them
           alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

   # switch pivot with rightmark (where the split point is)        
   alist[first], alist[rightmark] = alist[rightmark], alist[first]
   return rightmark  # the split point

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)


