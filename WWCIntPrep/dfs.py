# http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/
# Python program to print DFS traversal for complete graph
from collections import defaultdict
 
# This class represents a directed graph using adjacency
# list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # A function used by DFS
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited and print it
        visited[v]= True
        print v,
 
        # Recur for all the vertices adjacent to
        # this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
 
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self):
        V = len(self.graph)  #total vertices
 
        # Mark all the vertices as not visited
        visited =[False]*(V)
 
        # Call the recursive helper function to print
        # DFS traversal starting from all vertices one
        # by one
        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def dfs(self, v):
        path = []
        stack = [v]
        while stack:
            s = stack.pop()
            if s not in path:
                path.append(s)
            for w in reversed(self.graph[s]):
                if w not in path:
                    stack.append(w)
        return path
 
 
# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print "Following is Depth First Traversal"
g.DFS()
print
print 'using stack'
print g.dfs(0)
print
print g.dfs(2)



# j = defaultdict(list)
# for u in range(5):
#     for v in range(3):
#         j[u].append(v)

# print j

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

words = buildGraph(l1)
print 'words graph'
print words.dfs('fool')


