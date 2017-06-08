# testFour2.py

import sys
import os
import unittest

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __str__(self):
        return str(self.items)



class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices
    
    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                nv = self.addVertex(f)
            if t not in self.vertices:
                nv = self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
    
    def getVertices(self):
        return list(self.vertices.keys())
        
    def __iter__(self):
        return iter(self.vertices.values())

    def bfs(self, vert):
      start = self.getVertex(vert)
      start.setDistance(0)
      start.setPred(None)
      vertQueue = Queue()
      vertQueue.enqueue(start)
      for item in vertQueue:
        print 'in the queue:', item
      while (vertQueue.size()>0):
        currentVert = vertQueue.dequeue()
        print 'currVert', currentVert
        for nbr in currentVert.getConnections():
          if nbr.getColor() == 'white':
            nbr.setColor('gray')
            nbr.setDistance(currentVert.getDistance()+1)
            nbr.setPred(currentVert)
            vertQueue.enqueue(nbr)
        currentVert.setColor('black')

    # def traverse(self, y):
    #   x = self.getVertex(y)
    #   print x.getPred()
    #   while x.getPred():
    #     print x.getId()
    #     x = x.getPred()
    #   print x.getId()


                
class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ": color " + self.color + ": disc " + str(self.disc) + ": fin " + str(self.fin) + ": dist " + str(self.dist) + ": pred \n\t[" + str(self.pred)+ "]\n" + str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo]) + "]\n"
    
    def getId(self):
        return self.id





l1 = ['fail', 'fall', 'foil', 'foul', 'fool', 'cool', 'pool', 'poll', 'pall', 'pole', 'pope', 'pale', 'sale', 'page', 'sage']

def buildGraph(wordList):
  d = {}
  g = Graph()
  # create buckets of words that differ by one letter
  for word in wordList:
    for i in range(len(word)):
      bucket = word[:i] + '_' + word[1+i:]
      if bucket in d:
        d[bucket].append(word)
      else:
        d[bucket] = [word]
  # add vertices and edges for words in the same bucket
  for bucket in d.keys():
    for word1 in d[bucket]:
      for word2 in d[bucket]:
        if word1 != word2:
          g.addEdge(word1, word2)
  return g



g = buildGraph(l1)
print g.numVertices

print g.getVertices()


# for v in g:
#   print v

a = g.bfs('fool')
print a



























