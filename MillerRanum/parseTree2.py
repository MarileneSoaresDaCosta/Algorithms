class BinTree:
  def __init__(self, value):
    self.root = value
    self.left = None
    self.right = None


# transforms math expression in string into a list of items
def filterString(mathExp):
  prevch = ""
  arr = []
  num = ""
  for ch in mathExp:
    if ch == " ":
      prevch = " "
      continue 

    if ch.isdigit() :
      num += ch

    else:
      if len(num) > 0:
        arr.append(num) 
        num = ""

      arr.append(ch) 
    prevch = ch
  return arr




def buildParseTree(eList):
  pStack = []
  eTree = BinTree('')
  pStack.append(eTree)
  current = eTree

  for item in eList:
    
    if item == '(':
      # print item
      newNode = BinTree('')
      current.left = newNode
      pStack.append(current)
      current = current.left
      # print 'pStack: ', len(pStack)

    elif item.isdigit(): 
      # print item
      current.root = int(item)
      current = pStack.pop()
      # print 'pStack: ', len(pStack)

    elif item in ['+', '-', '*', '/']:
      # print item
      current.root = item
      newNode = BinTree('')
      current.right = newNode
      pStack.append(current)
      current = current.right
      # print 'pStack: ', len(pStack)

    elif item == ')':  
      # print item        
      current = pStack.pop()

    else:                           
      raise ValueError
  return eTree


e = "( ( 10 + 5 ) * 3 )"

pt = buildParseTree(filterString(e))


def inorder(tree):
    if tree != None:
        inorder(tree.left)
        print tree.root,
        inorder(tree.right)
    return 'end of tree'
print inorder(pt)


import operator 

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.left
    rightC = parseTree.right

    if leftC and rightC:
        fn = opers[parseTree.root]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.root

x = evaluate(pt)
print x











