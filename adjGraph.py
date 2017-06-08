#
#  adjGraph
#
#  Created by Brad Miller on 2005-02-24.
#  Copyright (c) 2005 Brad Miller, David Ranum, Luther College. All rights reserved.
#

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
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id

class adjGraphTests(unittest.TestCase):
    def setUp(self):
        self.tGraph = Graph()
        
    def testMakeGraph(self):
        gFile = open("test.dat")
        for line in gFile:
            fVertex, tVertex = line.split('|')
            fVertex = int(fVertex)
            tVertex = int(tVertex)
            self.tGraph.addEdge(fVertex,tVertex)
        for i in self.tGraph:
            adj = i.getAdj()
            for k in adj:
                print(i, k)

        
# if __name__ == '__main__':
#     unittest.main()

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


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

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')



w = buildGraph(l1)


print 'num of vertices', w.numVertices
# print 'the vertices list', w.getVertices()
print

# for v in w:
#   print v
print 'calling bfs'
print bfs(w, w.getVertex('fool'))
print

print 'calling traverse'
traverse(w.getVertex('sage'))           
