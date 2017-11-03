# https://www.hackerrank.com/challenges/tree-preorder-traversal

"""
Tree: preorder traversal

Complete the preOrder function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.

Input Format: Our hidden tester code passes the root node of a binary tree to your preOrder function.

Output Format: Print the tree's preorder traversal as a single line of space-separated values.
"""

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    if root:
        print root.data,
        preOrder(root.left)
        preOrder(root.right)