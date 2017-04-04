def insertionSort(lst):
  # pick item to be inserted starting with index 1
  for pivot in range(1, len(lst)):    
    pivotValue = lst[pivot]
    # position where we COULD insert pivot
    pos = pivot    
    # finding where to insert
    while pos > 0 and lst[pos - 1] > pivotValue:
      # shift item right
      lst[pos] = lst[pos - 1]
      pos = pos - 1
    lst[pos] = pivotValue


alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)