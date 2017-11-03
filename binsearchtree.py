"""
does not contain iterator
"""


class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
    def __iter__(self):
        """The standard inorder traversal of a binary tree."""
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
        
    def put(self,key,val):
        if self.root:   # if the tree already has a root
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)  # create a new treeNode, install it as root
        self.size = self.size + 1

    def _put(self,key,val,currentNode): # private recursive helper function to search the tree
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                   
    def __setitem__(self,k,v): 
      """
       overload the [] operator for assignment by having the
       __setitem__ method call the put method. 
       
       This allows us to write Python statements like 
       myZipTree['Plymouth'] = 55446, like a Python dict.

      """
      self.put(k,v)
       
    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
      """
      accessing the tree like a python dict
      z = mytree['Fargo'] assigns the obj to z 
      """
      return self.get(key)

    def __contains__(self,key):
      """
      overloads the 'in' operator.
      We can write
      if 'Northfield' in mytree: ...
      """
      if self._get(key,self.root):
           return True
      else:
           return False

    def delete(self,key):
      if self.size > 1:
        nodeToRemove = self._get(key,self.root)
        if nodeToRemove:
          self.remove(nodeToRemove)
          self.size = self.size-1
        else:
            raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
        self.root = None
        self.size = self.size - 1
      else:
        raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def spliceOut(self):
      if self.isLeaf():
        if self.isLeftChild():
          self.parent.leftChild = None
        else:
          self.parent.rightChild = None
      
      # the successor is guaranteed to have no more than 1 child!
      elif self.hasAnyChildren(): 
        if self.hasLeftChild():
          if self.isLeftChild():
             self.parent.leftChild = self.leftChild
          else:
             self.parent.rightChild = self.leftChild
          self.leftChild.parent = self.parent
        else:
          if self.isLeftChild():
             self.parent.leftChild = self.rightChild
          else:
             self.parent.rightChild = self.rightChild
          self.rightChild.parent = self.parent

    def findSuccessor(self):
      succ = None
      if self.hasRightChild():
        succ = self.rightChild.findMin()
      else:
        if self.parent:
          if self.isLeftChild():
            succ = self.parent
          else:
            self.parent.rightChild = None
            succ = self.parent.findSuccessor()
            self.parent.rightChild = self
      return succ

    def findMin(self):
      current = self
      while current.hasLeftChild():
        current = current.leftChild
      return current

    def remove(self,currentNode):
      if currentNode.isLeaf(): # if leaf, change ref of parent node
        if currentNode == currentNode.parent.leftChild: # ?why not if currentNode.isLeftChild():
          currentNode.parent.leftChild = None
        else:
          currentNode.parent.rightChild = None
      elif currentNode.hasBothChildren(): #interior
        succ = currentNode.findSuccessor()
        succ.spliceOut()
        currentNode.key = succ.key
        currentNode.payload = succ.payload

      else: # this node has one child
        if currentNode.hasLeftChild():
          if currentNode.isLeftChild():
            currentNode.leftChild.parent = currentNode.parent
            currentNode.parent.leftChild = currentNode.leftChild
          elif currentNode.isRightChild():
            currentNode.leftChild.parent = currentNode.parent
            currentNode.parent.rightChild = currentNode.leftChild
          else:
            currentNode.replaceNodeData(currentNode.leftChild.key,
                                currentNode.leftChild.payload,
                                currentNode.leftChild.leftChild,
                                currentNode.leftChild.rightChild)
        else:
          if currentNode.isLeftChild():
            currentNode.rightChild.parent = currentNode.parent
            currentNode.parent.leftChild = currentNode.rightChild
          elif currentNode.isRightChild():
            currentNode.rightChild.parent = currentNode.parent
            currentNode.parent.rightChild = currentNode.rightChild
          else:
            currentNode.replaceNodeData(currentNode.rightChild.key,
                                currentNode.rightChild.payload,
                                currentNode.rightChild.leftChild,
                                currentNode.rightChild.rightChild)

               
mytree = BinarySearchTree()
mytree[4]="red"
mytree[2]="blue"
mytree[6]="yellow"
mytree[1]="green"
mytree[5]="pink"
mytree[8]="white"
mytree[3]="purple"

# print(3 in mytree)
# print(mytree[6])
# del mytree[2]
# print(mytree[2])

for key in mytree:
    print(key,mytree[key])


print('root key = ', mytree.root.key)
print('left = ', mytree.root.leftChild.key)
print('left left = ', mytree.root.leftChild.leftChild.key) 
print('left right = ', mytree.root.leftChild.rightChild.key) 

print('right = ', mytree.root.rightChild.key)
print('right left = ', mytree.root.rightChild.leftChild.key)  
print('right right = ', mytree.root.rightChild.rightChild.key) 




