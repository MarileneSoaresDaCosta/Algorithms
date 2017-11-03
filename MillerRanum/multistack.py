# https://github.com/careercup/CtCI-6th-Edition-Python/blob/1b46e7759f6e5a0e35f0bcb968581ca60f53ee9a/Chapter3/31ThreeInOne.py

class MultiStack:

    def __init__(self, stacksize):
        self.numstacks = 3 # creates stacks 0, 1 and 2
        self.array = [0] * (stacksize * self.numstacks) # array of zeroes
        self.sizes = [0] * self.numstacks  # counter, used to check if full/empty
        self.stacksize = stacksize

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1   # update the counter
        self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize   # first index of stack
        return offset + self.sizes[stacknum] - 1


def ThreeInOne():
    newstack = MultiStack(6)
    # print 'newstack 1 empty', newstack.IsEmpty(1)
    # print 'newstack 1 empty', newstack.IsEmpty(2)
    newstack.Push(1, 1)
    newstack.Push(2, 1)
    # newstack.Push(3, 1)
    # newstack.Push(4, 1)
    # newstack.Push(5, 1)
    newstack.Push(10, 2)
    newstack.Push(20, 2)
    # newstack.Push(30, 2)
    # newstack.Push(40, 2)
    # newstack.Push(50, 2)
    newstack.Push(100, 0)
    newstack.Push(200, 0)
    # newstack.Push(300, 0)
    # newstack.Push(400, 0)
    # newstack.Push(500, 0)

    print 'index of top s1' , newstack.IndexOfTop(1)
    print 'index of top s2' , newstack.IndexOfTop(2)
    print 'index of top s0' , newstack.IndexOfTop(0)

    print 'peek s1', newstack.Peek(1)
    print 'peek s2', newstack.Peek(2)
    print 'peek s3', newstack.Peek(0)

    # print 'stack 1 empty:', newstack.IsEmpty(1)
    # newstack.Push(2, 1)
    # newstack.Push(4, 2)
    
    # print 's1 pop', newstack.Pop(1)
    # print 's1 peek', newstack.Peek(1)
    # newstack.Pop(1)
    # newstack.Push(5, 1)
    # newstack.Push(6, 1)
    # print 'index of top s1' , newstack.IndexOfTop(1)
    # print 's1 peek', newstack.Peek(1)
    

ThreeInOne()