#  https://interactivepython.org/runestone/static/pythonds/Trees/ListofListsRepresentation.html


def BinaryTree(r):
    return [r, [], []]    # implement a list with two sublists

def insertLeft(root,newBranch):
    t = root.pop(1)  # pick up the existing left child
    # print t
    if len(t) > 1:   # if the left child is currently occuppied
        root.insert(1,[newBranch,t,[]])  # move old left child as the left child of the new one
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
print r
insertLeft(r,4)
print 'after insertLeft 4', r
insertLeft(r,5)
print 'after insertLeft 5', r
insertRight(r,6)
print 'after insertRight 6',r
insertRight(r,7)
print 'after insertRight 7',r
l = getLeftChild(r)
print 'getLeftChild(r)', l


setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))

a = BinaryTree('a')
insertLeft(a, 'b')
insertRight(a, 'c')
b = getLeftChild(a)
insertRight(b, 'd')
c = getRightChild(a)
insertLeft(c, 'e')
insertRight(c, 'f')
print
print ' a tree'
print a




def buildTree():
    a = BinaryTree('a')
    insertLeft(a, 'b')
    insertRight(a, 'c')
    b = getLeftChild(a)
    insertRight(b, 'd')
    c = getRightChild(a)
    insertLeft(c, 'e')
    insertRight(c, 'f')
    return a



ttree = buildTree()
if getRootVal(getRightChild(ttree)) == 'c':
    print 'pass 1'
if getRootVal(getRightChild(getLeftChild(ttree))) == 'd':
    print 'pass 2'
if getRootVal(getRightChild(getRightChild(ttree))) == 'f':
    print 'pass 3'



