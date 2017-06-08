# https://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
"""
an empty binary heap has a single zero as the first element 
of heapList: this zero is not used, but is there so that simple
integer division can be used in later methods.

"""
class BinHeap:
    def __init__(self):
        self.heapList = [0] # the entire bin heap can be repr by a list
        self.currentSize = 0  # keep track of current size
    
    # If the newly added item is less than its parent, then we can swap the item with its parent
    def percUp(self,i): 
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2
          
    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)
  
    def percDown(self,i): # when called, i is equal to 1 initially
      while (i * 2) <= self.currentSize: # until to the lowest level possible
          mc = self.minChild(i) # find the child of lowest value
          # print 'index mc', mc, ' of value ', self.heapList[mc]
          if self.heapList[i] > self.heapList[mc]: # if node > minChild
              tmp = self.heapList[i]   # swap - pushing node down
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc  # update i a level down
          # print 'perc Down i', i

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:  # if there is no right child
          return i * 2      # return the left child       
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]: # if leftC < rightC
              return i * 2  # return leftC
          else:
              return i * 2 + 1 # return rightC
          
    def delMin(self):
      retval = self.heapList[1]  # save rootVal (min)
      self.heapList[1] = self.heapList[self.currentSize] # copy last item to root
      self.currentSize = self.currentSize - 1  # adjust list size
      self.heapList.pop()  # delete last item from the end of the list
      self.percDown(1)   # push down node at root to proper place
      return retval  # return saved min
  
    def buildHeap(self,alist):
      """
      Because the heap is a complete binary tree, any nodes past the 
      halfway point will be leaves and therefore have no children.
      """ 
      i = len(alist) // 2   # starting in the middle of the list
      # print 'i', i
      self.currentSize = len(alist)   
      self.heapList = [0] + alist[:]  # create a heaplist with an added zero
      while (i > 0):
          # print 'i', i
          self.percDown(i)
          # print self.heapList
          i = i - 1
      print self.heapList 
              
bh = BinHeap()
bh.buildHeap([9,5,6,2,3])


newb = BinHeap()
newb.buildHeap([27, 17, 33, 18, 14, 19, 21, 11, 9, 5])
print bh.__dict__
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print


