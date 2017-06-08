# linked lists
class Node:
  def __init__(self, initdata):
    self.data = initdata
    self.next = None  # reference to next node

  def getData(self):
    return self.data

  def getNext(self):
    return self.next

  def setData(self, newdata):
    self.data = newdata

  def setNext(self, newnext):
    self.next = newnext

  

# testing the creation of a node:
# temp = Node(93)
# print temp.getData()

""" unordered list """

class UnorderedList:
  def __init__(self):
    self.head = None

  def isEmpty(self):
    return self.head == None

  def add(self, item):
    # creates a new node and places the item as its data
    temp = Node(item)   
    # links the new node to the existing structure:
    
    #... sets the next ref of the new node to point at the old  first node of the list 
    temp.setNext(self.head)
    #...  now the rest of the list is attached to the new node, so we modify the head of the list to refer to the new node
    self.head = temp

  def size(self):
    current = self.head
    count = 0
    while current != None:
      count = count + 1
      current = current.getNext()
    return count

  def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()
    return found

  def remove(self, item):
    current = self.head
    previous = None
    found = False
    while not found:
      if current.getData() == item:
        found = True
      else:
        previous = current
        current = current.getNext()

    if previous == None:  # special case: beginning of list
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())  

  def append(self, item):
    current = self.head
    while current.getNext() != None:
      current = current.getNext()

    # now that we traversed the list...
    temp = Node(item)
    temp.setNext(None) # the last item points to None
    current.setNext(temp)  # and the current points to temp

  def insert(self, item, pos):
    current = self.head
    previous = None
    count = 0
    while count < pos:
      previous = current
      current = current.getNext()
      count += 1

    if pos > count:  # item to be inserted at the end of the list
      self.append(item)

    if previous == None:  # item to be inserted in the head
      self.add(item)

    else:
      temp = Node(item)
      temp.setNext(current)
      previous.setNext(temp)

    # assuming the the item is in the list          
  def index(self, item):
      current = self.head
      count = 0
      while current.getData() != item:
          count = count + 1
          current = current.getNext()
      return count

  def pop(self, pos):
    current = self.head
    previous = None
    count = 0
    while count != pos:
      count += 1
      previous = current
      current = current.getNext()
           
    if previous == None:                 # special case: item to be removed is first in the list
      self.head = current.getNext()    # ... so we change the head of the list
    else:
      previous.setNext(current.getNext()) 

  def removeHead(self):
    currenthead = self.head
    newhead = currenthead.getNext()
    self.head = newhead

  def printList(self):
    current = self.head
    while current != None:
      print current.getData()
      current = current.getNext()
    print 'end of list'
    
  def printnext(self, node):
    if node == None:
      return
    else:
      next = node.getNext()
      self.printnext(next)
    print node.getData()

#http://stackoverflow.com/questions/21529359/reversing-a-linked-list-in-python
  def reverse(self):
    current = self.head   # set current to head(start of node)
    previous = None       #  no node at previous
    while current !=None: # While current node is not null, loop
      nextt =  current.getNext()  # create a pointing var to next node(will use later)
      current.setNext(previous)   # current node(or head node for first time loop) is set to previous(ie NULL), now we are breaking the link of the first node to second node, this is where nextt helps(coz we have pointer to next node for looping)
      previous = current  # just move previous(which was pointing to NULL to current node)
      current = nextt     #  just move current(which was pointing to head to next node)
    self.head = previous   # after looping is done, (move the head to not current coz current has moved to next), move the head to previous which is the last node.

  def __str__(self):
    s = '['
    current = self.head
    count = 1
    while current != None and count < self.size():
        s = s + str(current.getData()) + ','
        current = current.getNext()
        count += 1
        
    s = s + str(current.getData()) + ']'
    return s


mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print 'initial list'
mylist.printList()
print 'initial list using str'
print str(mylist)
print 'appending new item (100)'
print(mylist.append(100))
mylist.printList()
print 'index of 54'
print mylist.index(54)
print "remove head"
print mylist.removeHead()
print 'updated list:'
mylist.printList()
print mylist.size()
print mylist.reverse()
print
print ("mylist.printList()")
mylist.printList()

print
print ("mylist.printnext(mylist.head)")
mylist.printnext(mylist.head)

print
print 'append'
mylist.append(120)
mylist.printList()


""" 3.22 Ordered List ADT """

class OrderedList:
  def __init__(self):
    self.head = None
      
  def isEmpty(self):
    return self.head == None

  def size(self):
    current = self.head
    count = 0
    while current != None:
      count += 1
      current = self.getNext()
    return count

  def search(self, item):
    current = self.head
    found = False
    stop = False
    while current != None and not found and not stop:
      if current.getData() == item:
        found = True
      else:
        if current.getData() > item:
          stop = True
        else:
          current = current.getNext()
    return found
              
  def add(self, item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
      if current.getData() > item:
        stop = True
      else:
        previous = current
        current = current.getNext()
    temp = Node(item)
    if previous == None:         # special case: adding to the head
      temp.setNext(self.head)  # here the self.head refers to the item who will no longer be the head
      self.head = temp         # and the head points to the newly created node
    else:
      temp.setNext(current)
      previous.setNext(temp)

  # here append will be used in merging two sorted lists, so no need to check if items are being appended in order:    
  def append(self, item):
    current = self.head
    # in the case of first item being added to the list:
    if current == None:
      temp = Node(item)   
      temp.setNext(self.head)
      self.head = temp
    else:
      while current.getNext() != None:
        current = current.getNext()
      temp = Node(item)
      temp.setNext(None)      # the last item points to None
      current.setNext(temp)   # and the current points to temp

  def mergeSorted(self, list1, list2):
    c1 = list1.head
    c2 = list2.head
    while c1 and c2:
      # print c1.getData(), c2.getData()
      if c1 < c2:
        self.append(c1.getData())
        c1 = c1.getNext()
      else:
        self.append(c2.getData())
        c2 = c2.getNext()
    # reached the end of 1 or 2 lists (2 is the 'empty lists case')
    if c1 == None and c2 == None:  # both are empty
      return 
    elif c1 == None:        # list1 reached end
      while c2 != None:
        self.append(c2.getData())
        c2 = c2.getNext()
    else:                   # list2 reached end
      while c1 != None:       
        self.append(c1.getData())
        c1 = c1.getNext()
    return

  def printList(self):
    current = self.head
    while current != None:
      print current.getData()
      current = current.getNext()
    return

  def merge(self, list1, list2):
    if not list1.isEmpty():
      current = list1.head
      while current != None:
        self.add(current.getData())
        current = current.getNext()
    if not list2.isEmpty():
      current = list2.head
      while current != None:
        self.add(current.getData())
        current = current.getNext()
    return

alist = OrderedList()
alist.add(1)
alist.add(3)
alist.add(5)

blist = OrderedList()
blist.add(2)
blist.add(4)
blist.add(6)

print
print 'ordered lists:'
alist.printList()
print
blist.printList()
print
blist.append(10)
blist.printList()

ablist = OrderedList()
ablist.mergeSorted(alist, blist)
ablist.printList()
print
print 'testing efficient merge'

xlist = OrderedList()
xlist.add(10)
xlist.add(3)
xlist.add(-1)

ylist = OrderedList()
ylist.add(2)
ylist.add(4)
ylist.add(6)
print
print 'ordered lists x and y:'
xlist.printList()
print
ylist.printList()
print
print 'merge'
xylist = OrderedList()
xylist.merge(xlist, ylist)
xylist.printList()






