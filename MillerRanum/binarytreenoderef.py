# https://interactivepython.org/runestone/static/pythonds/Trees/NodesandReferences.html

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:  # if node is empty
            self.leftChild = BinaryTree(newNode)  
        else:  
            t = BinaryTree(newNode)  # create new node
            t.leftChild = self.leftChild   # insert a node and push the existing child down one level in the tree
            self.leftChild = t       # make new node the leftC

    def insertRight(self,newNode): # There will either be no right child, or we must insert the node between the root and an existing right child

        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key                


r = BinaryTree('a')
print '1'
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print
print '2'
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
print
print '3'
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
print
print '4'
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())

a = BinaryTree('a')
a.insertLeft('b')
a.getLeftChild().insertRight('d')
a.insertRight('c')
a.getRightChild().insertLeft('e')
a.getRightChild().insertRight('f')

if a.getRightChild().getRootVal() =='c':
    print 'pass 1'
if a.getLeftChild().getRightChild().getRootVal() == 'd':
    print 'pass 2'
if a.getRightChild().getLeftChild().getRootVal() == 'e':
    print 'pass 3'

