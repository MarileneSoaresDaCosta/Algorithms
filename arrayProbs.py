# arrays

"""
# delete all zeroes from an array
arr = [2, 3, 56, 0 , -1, 5, 'o', True, -5, 0]

# creating a new array
newarr = filter(lambda x: x != 0, arr)

print 'newarr', newarr



if 0 in arr:
  for item in arr:
    if item == 0:
      arr.remove(item)


print 'arr' , arr

arr2 = [2, 3, 56 , -1, 5, 'o', True, -5]

# creating a new array
newarr2 = filter(lambda x: x != 0, arr2)
print 'newarr2', newarr2
"""

"""

# print even array items in backward order

arr = [0, 5, 10, 15, 8, 3,  6, 9.1, 4, 'a', 2]

for i in reversed(range(0, len(arr))):
  if type(arr[i]) == int and arr[i]%2 == 0 and arr[i] > 0:
    print arr[i]

print arr

# invert array in place:

print arr[::-1]
"""

# rotate an array by 3 positions to the right

arr = [1, 2, 3, 4, 5, 6]

for r in range(3):
  temp = arr.pop()
  arr.insert(0, temp)

print arr














