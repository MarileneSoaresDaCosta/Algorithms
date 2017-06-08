# Ch 5 Sorting and Searching - Sequential Search

def seqSearch(alist, item):
  pos = 0
  found = False

  while pos < len(alist) and not found:
    if alist[pos] == item:
      found = True
    else:
      pos += 1
  return found


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print seqSearch(testlist, 3)
print seqSearch(testlist, 13)

testlist2 = sorted(testlist)
print testlist2

def orderedSeqSearch(alist, item):
  pos = 0
  found = False
  stop = False

  while pos < len(alist) and not found and not stop:
    if alist[pos] == item:
      found = True
    else:
      if alist[pos] > item:
        stop = True
      else:
        pos += 1
  return found

print orderedSeqSearch(testlist, 3)
print orderedSeqSearch(testlist, 42)



