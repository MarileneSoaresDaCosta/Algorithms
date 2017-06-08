
# coding: utf-8

# ## simulation - printing tasks

# In[1]:

class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):  # assumes that the 'rear' is at position zero
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    

# tracks whether it has a current task
class Printer:  
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    # decrements the internal timer and sets the printer to idle if the task is completed.
    def tick(self):  
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

        
import random

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    # retrieve the amount of time spent in the queue before printing begins.
    def waitTime(self, currenttime):
        return currenttime - self.timestamp


# In[ ]:

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
            
        # If the printer is not busy and if a task is waiting,
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            # Remove the next task from the print queue and assign it to the printer.
            nexttask = printQueue.dequeue()  # new instance of Task
            # print nexttask.__class__.__name__
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        
        labprinter.tick()
#         print waitingtimes
        
    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

    
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:  # this num reflect an expected value of 20 pages per hour (for 10 students)
        return True
    else:
        return False

    
"""  
run the simulation for a period of 60 minutes (3,600 seconds) 
using a page rate of five pages per minute. 
In addition, we will run 10 independent trials.     
"""

print 'ppm = 5'
for i in range(10):
    simulation(3600,5)


# In[13]:
print 'ppm = 10'
for i in range(10):
    simulation(3600,10)



