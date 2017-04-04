# recursion exercises

# recursive function to reverse a list
"""

def rev(l):
  if len(l) == 0:
    return []
  return [l[-1]] + rev(l[:-1])



mylist = [1, 2, 3, 4]

print rev(mylist)

"""
# Problem Solving with Algorithms and Data Structures - ch4 - recursion
"""
Write a program to solve the following problem: You have two jugs: a 4-gallon jug and a 3-gallon jug. Neither of the jugs have markings on them. There is a pump that can be used to fill the jugs with water. How can you get exactly two gallons of water in the 4-gallon jug?
Generalize the problem above so that the parameters to your solution include the sizes of each jug and the final amount of water to be left in the larger jug

"""

# 0 < m < n i.e. jug n is greater than jug m


def jugs(m, n, maxm, maxn, d):
  print 'maxm, maxn', maxm, maxn
  if m == d or n == d:
    return m, n

  if n == 0:
    n = maxn
  if m == maxm:
    m = 0

  for i in range(maxm):
    if n >= 1 and m < maxm:
      m += 1
      n -= 1
  print m, n
  m, n = jugs(m, n, maxm, maxn, d)     
  return m, n
  


print jugs(0, 0, 3, 5, 4)
