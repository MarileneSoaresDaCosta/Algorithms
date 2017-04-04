import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)


test_arr = [[ 1, 1, 1, 0, 0, 0],
            [ 0, 1, 0, 0, 0, 0],
            [ 1, 1, 1, 0, 0, 0],
            [ 0, 0, 2, 4, 4, 0],
            [ 0, 0, 0, 2, 0, 0],
            [ 0, 0, 1, 2, 4, 0]]

def hourglass(arr, r, c):
  i = r
  j = c
  hgsum = 0

  #top line
  hgsum = arr[i][j]  # starting point
  j +=1
  hgsum += arr[i][j] 
  j += 1
  hgsum += arr[i][j]  

  # middle item
  i += 1
  j -= 1
  hgsum += arr[i][j] 

  # bottom line
  i += 1
  j -= 1
  hgsum += arr[i][j] 
  j +=1
  hgsum += arr[i][j] 
  j += 1
  hgsum += arr[i][j]  

  return hgsum

# print hourglass(test_arr, 3, 3)

res = []

for r in range(4):
  for c in range(4):
    res.append(hourglass(arr, r, c))  

print max(res_sum)



  