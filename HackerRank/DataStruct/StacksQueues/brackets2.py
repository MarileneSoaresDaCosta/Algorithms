# hackerrank balanced brackets

def brackets(symbolStr):
  s = []
  balanced = True
  index = 0
  while index < len(symbolStr) and balanced:
    symbol = symbolStr[index]
    if symbol in "{[(":  # if it is an opening symbol
      s.append(symbol)     # add it to the stack
    else:
      if len(s) == 0:    # 'closing symbol', but stack is empty 
        balanced = False
      else:
        openers = "([{"
        closers = ")]}"
        top = s.pop()    # closing symbol does not match open on top
        if openers.index(top) != closers.index(symbol):
          balanced = False
    index += 1
  if balanced and len(s) == 0:
    return "YES"
  else:
    return "NO"


  


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
