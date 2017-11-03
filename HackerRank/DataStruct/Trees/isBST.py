# is the tree a bst?

INT_MAX = 4294967296
INT_MIN = -4294967296
def check_binary_search_tree_(root):
    return (isBST(root, INT_MIN, INT_MAX))
 
def isBST(root, mini, maxi):
    if root == None:
        return True
    
    if root.data < mini or root.data > maxi:
        return False
    
    return (isBST(root.left, mini, root.data -1) and
          isBST(root.right, root.data +1 , maxi))
