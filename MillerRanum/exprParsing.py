class expTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None



# util function that checks if c is an operator

def isOperator(c):
  if c in ['+', '-', '*', '/', '^']:
    return True
  else:
    return False


# util function to do inorder traversal - t is the pointer to root

def inorder(t):
  if t != None:
    inorder(t.left)
    print t.value
    inorder(t.right)


def constructTree(expr):
  stack = []
  for char in expr:
    if not isOperator(char): # is an operand
      t = expTree(char)
      stack.append(t)

    else:
      t = expTree(char)
      t1 = stack.pop()
      t2 = stack.pop()

      t.right = t1
      t.left = t2

      stack.append(t)
  t = stack.pop()
  return t


mathExp = '10+5*3'
r = constructTree(mathExp)
print 'exp is: ',
inorder(r.root)













