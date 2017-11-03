# hackerrank balanced brackets

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

def brackets(symbolStr):
  s = Stack()
  balanced = True
  index = 0
  while index < len(symbolStr) and balanced:
    symbol = symbolStr[index]
    if symbol in "{[(":  # if it is an opening symbol
      s.push(symbol)     # add it to the stack
    else:
      if s.isEmpty():    # 'closing symbol', but stack is empty 
        balanced = False
      else:
        top = s.pop()    # closing symbol does not match open on top
        if not matches(top, symbol):
          balanced = False
    index += 1
  if balanced and s.isEmpty():
    return "YES"
  else:
    return "NO"

def matches(open, close):
  openers = "([{"
  closers = ")]}"
  return openers.index(open) == closers.index(close)  
  


import sys

bracketlist = []
t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    bracketlist.append(s)

# print 'bracketlist'
# print bracketlist

for string in bracketlist:
  print brackets(string)
