
# binary search - only whether item is in the list

def binarySearch(alist, item):
  first = 0
  last = len(alist) - 1
  found = False

  while first <= last and not found:
    midpoint = (first + last) // 2
    if alist[midpoint] == item:
      found = True
    else:
      if alist[midpoint] > item: # item may be in lower half
        last = midpoint - 1
      else:
        first = midpoint + 1

  return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

# binary search with recursion

def recBinarySearch(alist, item):
  if len(alist) == 0:
    return False
  else:
    midpoint = len(alist) // 2
    if alist[midpoint] == item:
      return True
    else:
      if item < alist[midpoint]:
        return recBinarySearch(alist[:midpoint], item)
      else:
        return recBinarySearch(alist[midpoint+1:], item)


print recBinarySearch(testlist, 3)
print recBinarySearch(testlist, 32)
"""
print '113' , 113%11
print '117', 117%11
print '97',  97%11
print '100', 100%11
print '114', 114%11
print '108', 108%11
print '116', 116%11
print '105', 105%11
print '99', 99%11
"""





