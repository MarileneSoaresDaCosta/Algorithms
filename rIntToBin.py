# 4.5 Converting an Integer to a String in any base (up to hexa)


# implementation of a Stack ADS 
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


rStack = Stack()

def toString(n, base):
  convertString = '0123456789ABCDEF'
  while n > 0:
    if n < base: # base case
      rStack.push(convertString[n])
    else:
      rStack.push(convertString[n%base])
    n = n // base
  res = ""
  while not rStack.isEmpty():
    res = res + str(rStack.pop())
  return res


# num = raw_input().strip()

# base = raw_input().strip()

# num, base = int(num), int(base)

# print toString(num, base)



def getSum(l):
    if len(l)==0:
        return 0
    else:
        return l[0] + getSum(l[1:]) 

# print 'getSum([1, 3, 4, 2, 5])', getSum([1, 3, 4, 2, 5])

# print 'getSum([1])', getSum([1])

# print 'getSum([])', getSum([])


def isPal(string):
  string = string.lower()
  pStack = Stack()
  for ch in string:
    pStack.push(ch)
  ps = ''
  while not pStack.isEmpty():
    ps = ps + pStack.pop()
  return ps == string

print isPal('abc')

print isPal('kayak')

print isPal('Kanakanak')

print isPal('something')











