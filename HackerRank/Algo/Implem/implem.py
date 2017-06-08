# hackerrank implementation challenges
import sys
import math

""" mini max sum """
"""
a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
arr = []

for el in a,b,c,d,e:
  arr.append(el)

min = arr[0]
max = arr[0]

for item in arr:
  if item < min:
    min = item
  if item > max:
    max = item

sum = 0
for item in arr:
  sum = sum + item

minsum = sum - max
maxsum = sum - min

print minsum, maxsum
"""

""" designer pdf viewer """
"""
h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()

alpha = []
wordl = []
for height in h:
  alpha.append(height)

for char in word:
  wordl.append(char)

maxh = 0

for char in wordl:
  if alpha[ord(char)-97] > maxh:
    maxh = alpha[ord(char)-97]

area = maxh * len(wordl)
print area
"""

""" apple and orange """
"""
s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

apple_house = 0
orange_house = 0

for d in apple:
  if a + d >= s and a + d <= t:
    apple_house += 1

for d in orange:
  if b + d >= s and b + d <= t:
    orange_house += 1

print apple_house
print orange_house
"""


""" kangaroo """ 

"""
x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]


def kangaroo(x1,v1,x2,v2):
  meet = 'NO'
  if v2 >= v1 and x2 > x1:
    return meet

  while meet == 'NO':
    x1 += v1
    x2 += v2
    if x1 == x2:
      meet = 'YES'
  return meet

# print kangaroo(x1,v1,x2,v2)

def kangaroo2(x1,v1,x2,v2):
  
  if v2 >= v1:
    return 'NO'

  if ((x2 - x1) / (v1 - v2)) < 0:
    return 'NO'

  else:
    return 'YES'

print kangaroo2(x1,v1,x2,v2)

# this is the winner!!
def kangaroo3(x1,v1,x2,v2):
  
if v2 >= v1 and x2 > x1:
    return 'NO'

  else:
        if v1 != v2 and ((x2 - x1) % (v1 - v2)) == 0:
            return 'YES'

        else:
            return 'NO'

print kangaroo3(x1,v1,x2,v2)
"""

""" Utopian Tree """
"""
def utopia(N):
  h = 1
  while N > 0:
    if N % 2 == 0:
      h = (2 * h) + 1
      N -= 2
    else:
      if N == 1:
        h = 2*h
        N -= 1
      else:
        h = 2*h + 1
        N -= 2

  return h

t = int(raw_input().strip())
reslist = []

for a0 in xrange(t):
  n = int(raw_input().strip())
  reslist.append(utopia(n))

for item in reslist:
  print item
"""

""" Angry Professor """
"""

def countPres(l, k):
  count = 0
  for item in l:
    if item <= 0:
      count +=1
  if count < k:
    return 'YES'  # fewer than k, cancel class
  else:
    return 'NO'


t = int(raw_input().strip())
res = []
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    res.append(countPres(a, k))

for item in res:
  print item

"""

""" Beautiful Day at the Movies """
"""
def reverse(num):
  return int(str(num)[::-1])

i, j, k = raw_input().strip().split(' ')
i, j, k = [int(i), int(j), int(k)]

count = 0

for day in range(i, j+1):
  if abs(day - reverse(day)) % k == 0:
    count += 1

print count
"""

""" Viral Advertising """
"""
import math

def viral(n):
  r = 5
  count = 0
  for day in range(1, n+1):
    liked = int(math.floor(r/2))
    shared = liked * 3
    # print 'day', day, 'liked', liked
    count += liked
    r = shared
    # print 'day', day, 'r', r
  return count

n = int(raw_input().strip())

print viral(n)
"""

""" Find Digits """
"""
def dig(N):
  count = 0
  n = str(N)
  for digit in n:
    if int(digit) > 0 and N % int(digit) == 0:
      # print digit
      count += 1
  return count

res = []
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    res.append(dig(n))

for item in res:
  print item
"""

""" extra long factorials """
"""
def fact(n):
  if n == 1:
    return 1
  else:
    return n * fact(n-1)
print fact(1)
# print fact(3)
# 
print fact(100)
"""

""" append and delete """
"""
def appDel(s, t, k):

  if s == t:
    if k%2 == 0 or k == len(s) + len(t) + 1:  
      return 'Yes'
    else:
      return 'No'

  if len(s) - len(t) > k:
    return 'No'

  if len(s) + len(t) < k:
    return 'Yes'

  else:
    equal = 0
    if len(s) > len(t):
      for i in range(0, len(t)):
        if s[i] == t[i]:
          equal += 1
        else:
            break

    else:
      for i in range(0, len(s)):
        if s[i] == t[i]:
          equal += 1
        else:
            break


    delchars = len(s) - equal
    addchars = len(t) - equal
    mink = delchars + addchars
    print 'equal', equal, 'min k', mink
    if k == mink:
      return 'Yes'
    if k > mink and k%2 == mink%2:
      return 'Yes'
    else:
      # print k%2
      # print mink%2
      # print k%2 == mink%2
      return 'No'


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

print appDel(s, t, k)
"""

""" sherlock and squares """

"""
def checkSqr(a, b):
  beg = int(math.ceil(math.sqrt(a)))
  end = int(math.floor(math.sqrt(b)))
  dif = end - beg + 1
  return dif
  



t = int(raw_input().strip())
res = []
for j in xrange(t):
    a,b = raw_input().strip().split(' ')
    a,b = [int(a),int(b)]
    
    res.append(checkSqr(a, b))

for item in res:
  print item
"""

""" cut the sticks """
"""
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


def sticks(arr):
    arr.sort(reverse=True)
    while len(arr) > 0:
        print len(arr)
        lowest = arr.pop()
        # print lowest
        while len(arr) > 0 and arr[-1] <= lowest:
            arr.pop()
        print 'len(arr)', len(arr)

sticks(arr)
"""
# reviewing slicing...
"""
a = ['p', 'y', 't', 'h', 'o', 'n']
print a[-1]

s = 'python'
print s[-1]
"""

""" Repeated Strings """
"""
# print 10%3
# s2 = 'abacaxi'
# print 'r2', s2[:2]

# s = 'aba'
# n = 10

def repString(s, n):
  acount = 0
  for ch in s:
    if ch == 'a':
      acount += 1
  # print 'acount', acount

  complWords = (n / len(s)) * acount  
  # print 'complWords', complWords

  rcount = 0
  r = n%len(s)
  for ch in s[:r]:
    if ch == 'a':
      rcount += 1
  # print 'rcount', rcount

  output = complWords + rcount
  return output



s = raw_input().strip()
n = long(raw_input().strip())
print repString(s, n)

"""

""" Equalize the Array """ 
"""
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

d = {}
# for each item, how many would have to be deleted to keep item unique
for item in arr:
  d[item] = len(arr) - arr.count(item)

# sort the array so that first element has lowest 'to delete'
sortd = sorted(d.items(), key=lambda x: x[1])
print sortd[0][1]
"""

""" ACM ICPC Team """ 
"""
4 5
10101
11100
11010
00101
"""

# n,m = raw_input().strip().split(' ')
# n,m = [int(n),int(m)]
# topic = []
# topic_i = 0
# for topic_i in xrange(n):
#    topic_t = str(raw_input().strip())
#    topic.append(topic_t)


# pairs = []
# maxtop = 0
# p1 = 0
# p2 = 0
# j = 0
# attempt 1 - works for small n and m
# for p1 in range(n-1):
#   for p2 in range(p1 + 1, n):
#     for j in range(m):
#       # print 'pair', p1, p2, 'j ',j, 'maxtop', maxtop
#       # print pairs
#       if topic[p1][j] == '1' or topic[p2][j] == '1':
#         maxtop += 1
#         j += 1
#       else:
#         j +=1
#       # print 'maxtop', maxtop
#     pairs.append(maxtop)
#     maxtop = 0
#     p2 += 1
#   p1 += 1
# # print pairs

# finalMax = max(pairs)
# print finalMax
# print pairs.count(finalMax)


# attempt 2 from http://codereview.stackexchange.com/questions/112432/hackerrank-acm-icpc-team
import random
import itertools
import time

# n number of people
# m number of topics

# n = 5
# m = 5

"""
binary_string(n) and random_list(n_people, n_topic) just help
to generate test cases, irrelevant otherwise.
"""
"""
def binary_string(n):
    my_string = "".join(str(random.randint(0, 1)) for _ in range(n))
    return my_string    

def random_list(n_people, n_topic):
    my_list = [binary_string(n_topic) for _ in range(n_people)]
    return my_list    

"""
"""
the essential part is item_value(e1, e2)
and find_couples(comb_list)
"""

"""
def item_value(e1, e2): # e1 and e2 are the strings repr persons' skills
    c = bin(int(e1, 2) | int(e2, 2))
    print 'c', c
    return c[2:].count('1')

def find_couples(comb_list):
    max_value = 0
    counter = 0      

    for pair in itertools.combinations(comb_list, 2):
        value = item_value(pair[0], pair[1])
        print value
        if value == max_value:
            counter += 1
        elif value > max_value:
            max_value = value
            counter = 1

    print(max_value)
    print(counter)
    return    

topic = random_list(n, m)

print(topic)    

start = time.time()
find_couples(topic)
end = time.time()
print(end - start)

# base = ['10101', '11100', '11010', '00101']
# print find_couples(base)

x = bin(1|0)

print bin(1)
print bin(0)
print x

# attempt 3 - using algo from above: This one works!
"""
"""
test case:

4 5
10101
11100
11010
00101
"""
"""
# import random
import itertools
# import time

# getting input from user:
n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
   topic_t = str(raw_input().strip())
   topic.append(topic_t)

# given a team, generates max num of topics
def teamValue(s1, s2): 
    comb_str = bin(int(s1, 2) | int(s2, 2))
    return comb_str[2:].count('1')   

def eval_teams(skill_list):
    max_value = 0
    counter = 0      

    for team in itertools.combinations(skill_list, 2):
      temp = teamValue(team[0], team[1])
      if temp == max_value:
          counter += 1
      elif temp > max_value:
          max_value = temp
          counter = 1

    print(max_value)
    print(counter)
    return    

eval_teams(topic)

# playing with binary... 

s1 = '1001010101010000011110000'
c = bin(int(s1,2))
print s1
print c

print sys.getsizeof(s1)
print sys.getsizeof(c)
"""
"""
L = 54

l1 = math.floor(math.sqrt(L))
print l1
l2 = math.ceil(math.sqrt(L))
print l2
s = 'if man was meant to stay on the ground god would have given us roots'
s = s.strip().split(' ')
sf = ''.join(s)
print len(sf)
"""

""" Encryption """


"""
trouble = []
L = 0
for L in range (1, 81):
  row = math.floor(math.sqrt(L))
  col = math.ceil(math.sqrt(L))
  if row*col < L:
    print 'L', L, 'row', row, 'col', col
    trouble.append(L)
print trouble



s = raw_input().strip()

L = len(s)


row = int(math.floor(math.sqrt(L)))
col = int(math.ceil(math.sqrt(L)))

if row * col < L:
  row = col

# print 'row, col', row, col
f = ''
i = 0
for word in range(0, col):
  
  for ch in range(i, L, col):
    f = f + s[ch]

  f = f + ' '
  word += 1
  i += 1

print f 
"""

""" bigger is greater """

# explanation at 
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

def lex(word):
    arr = list(word)
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return 'no answer'

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    final_str = ''.join(arr)
    return final_str
  

t = raw_input().strip()
t = int(t)
words = []
word_i = 0
for word_i in xrange(t):
   word = str(raw_input().strip())
   words.append(word)

for word in words:
  print lex(word)