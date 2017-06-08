class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None

    def __str__(self):
        return str(self.info) 



class BinarySearchTree:
    def __init__(self): 
        self.root = None


    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
            # self.level = 0
        else:
            current = self.root
            # curr_level = 0
            
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                        # curr_level += 1
                    else:
                        current.left = Node(val)
                        # curr_level += 1
                        # current.level = curr_level
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                        # curr_level += 1
                    else:
                        current.right = Node(val)
                        # curr_level += 1
                        # current.level = curr_level
                        break
                else:
                    break
            # print 'info:', current.info, 'level:', current.level
"""
The height is returned recursively "up" the tree from the longest root-to-leaf path. 
So:
If you are in the leaf, since it don't have any nodes (if root == None) it will receive -1 from max(self.getHeight(root.left), self.getHeight(root.right)) so it will return 0. That is correct since height of leaf is 0.
If our root have 1 leaf, it will return 1 + height of it's leaf (which is 0 as stated in point 1) so at the end it will return 1. That is correct since height of tree with 1 leaf is 1.
...and continue with this logic recursively

"""

def height(root):
    if root == None:
        return -1
    return 1 + max(height(root.left), height(root.right))



tree = BinarySearchTree()
t = int(raw_input())

for _ in xrange(t):
    x = int(raw_input())
    tree.create(x)

def preOrder(root):
    if root:
        print 'info:', root.info, "level", root.level
        preOrder(root.left)
        preOrder(root.right)


# print 'preOrder function: '
# preOrder(tree.root)
print 'function height: ', height(tree.root)



def isBST(root):
    prev = None
    if root:
        # print 'root.info:', root.info
        if isBST(root.left) == False:
            return False
        if prev != None and root.info <= prev.info:
            return False
        prev = root
        # print 'prev: ', prev.info
        return isBST(root.right)
    return True
print 'this a BST...'
print isBST(tree.root)


def get(root, val):
    if not root:
        return False
    else:
        currentNode = root
        if currentNode.info == val:
            return True
        elif currentNode.info > val:
            return get(currentNode.left, val)
        else:
            return get(currentNode.right, val)

print 'is there a node = 4 ? ', get(tree.root, 4)

print 'is there a node = 12 ? ', get(tree.root, 12)


"""
input 
7
3
2
5
1
4
6
7

"""
