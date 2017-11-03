#  https://interactivepython.org/runestone/static/pythonds/Trees/ParseTree.html

"""
rules 
    1. If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.

    2. If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.

    3. If the current token is a number, set the root value of the current node to the number and return to the parent.

    4. If the current token is a ')', go to the parent of the current node.
"""
import operator
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


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


def buildParseTree(fpexp): # parseTree of an expression string
    fplist = fpexp.split()  # split the string into characters
    pStack = Stack() 
    eTree = BinaryTree('')
    pStack.push(eTree)      # add tree to the stack
    currentTree = eTree     # shows 'where we are' as we move
    for i in fplist:
        if i == '(':            
            currentTree.insertLeft('')   # add new node as leftC
            pStack.push(currentTree)     # save the path 
            currentTree = currentTree.getLeftChild() #descend to leftC
        
        elif i.isdigit(): 
            currentTree.setRootVal(int(i))  # assign value
            parent = pStack.pop()           # get path (parent)
            currentTree = parent            # go up to parent
        
        elif i in ['+', '-', '*', '/']:       
            currentTree.setRootVal(i)       
            currentTree.insertRight('')     # add new node as rightC
            pStack.push(currentTree)        # save path
            currentTree = currentTree.getRightChild() #desc. to rightC
        
        elif i == ')':          
            currentTree = pStack.pop()      # go up to parent
        
        else:                    # error checking if invalid character
            raise ValueError
    
    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
# print pt
# pt2 = buildParseTree("( ( 10 + j ) * 3 )")

s = "((10+j)*3)"
print s.split()

j = "( ( 10 + 5 ) * 3 )"
print j.split()
# pt.postorder()

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

x = evaluate(pt)
print x

def preorder(tree):
    if tree:
        print tree.getRootVal()
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print tree.getRootVal()

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print tree.getRootVal()
        inorder(tree.getRightChild())

def printexp(tree): # recovers fully parenthesized version 
    sVal = ''
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal

print
print 'preorder traversal'
preorder(pt)

print
print 'postorder traversal'
postorder(pt)

print
print 'inorder traversal'
inorder(pt)

print
print 'printexp function'
print printexp(pt)



def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None

    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()
