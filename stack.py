# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#stack.py


class Stack:
    def __init__(self):
        self.items = []
        self.minvals = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.items == []:
            self.minvals.append(item)
        else:
            self.minvals[-1] = min(item, self.minvals[-1])
        self.items.append(item)

    def pop(self):
        if self.items == []:
            raise Exception('Stack is empty')    
        return self.items.pop()

    def peek(self):
        if self.items == []:
            raise Exception('Stack is empty')  
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def min(self):
        return self.minvals[-1]

    def printStack(self):
        for item in self.items:
            print item,

    def printMinvals(self):
        for item in self.minvals:
            print item,

s=Stack()

print(s.isEmpty())
s.push(5)
s.push(6)
s.push(2)
s.push(7)
s.push(14)
s.push(3)
print 'stack'
s.printStack()
print

print 'minvals'
s.printMinvals()

print s.min()
s.push(1)
s.push(4)
s.push(44)
s.push(2)
print s.min()
s.pop()
s.pop()
s.pop()
s.pop()
# print s.min()
print 'stack'
s.printStack()
print

print 'minvals'
s.printMinvals()








