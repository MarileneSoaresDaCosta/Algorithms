# chapter 1
count = 10**5
# print count

nums =[]
for i in range(count):
  nums.append(i)

nums.reverse()
# print nums

#  a similar program, but with much worse time complexity
nums2 = []
for i in range(count):
  nums2.insert(0, i)  # it shifts the entire array to insert on zero
  
