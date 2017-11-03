m =  [[0,1,0,0],
      [1,0,1,1],
      [0,1,0,1],
      [0,1,1,0]]

edges = 0

for r in range(len(m)-1):
  edges += m[r][r+1]

print edges
