# problems suggested at https://adriann.github.io/programming_problems.html

# prob 1: a function that returns the largest elem in a list

def largest(alist):
  if len(alist) == 0:
    return 'empty list'
  else:
    largest = alist[0]
    for i in range(1, len(alist)):
      if alist[i] > largest:
        largest = alist[i]
  return largest

lst = [1, 2, 3, 5, 7, 11, 13, 17]
lst2 = [-45, -6, -1, 'a']
lst3 = []
print 'prob 1'
print largest(lst)
print largest(lst2)
print largest(lst3)
print

# 2. function that reverses a list, preferably in place

def rev(alist):
  n = len(alist)
  if n < 2:
    return alist
  else:
    for i in range(n//2):
      alist[i], alist[n - 1 - i] = alist[n - 1 - i], alist[i]
  return alist


print 'prob 2'
print rev(lst)
print rev(lst2)
print rev(lst3)
print


# 3. a function that checks whether an element occurs in a list.
def inList(elem, alist):
  found = False
  if len(alist) == 0:
    return found
  else:
    for item in alist:
      if item == elem:
        found = True
        break
  return found

print 'prob 3'
print inList(7, lst)
print inList(-98, lst2)
print inList('a', lst2)
print inList(1, lst3)
print



# 4. Write a function that returns the elements on odd positions in a list. 
# OBS: Here, by 'odd position', I interpreted indexes 1, 3, etc for a list starting with zero.

def oddIndex(alist):
  res = []
  if len(alist) < 2:
    return res
  else:
    for i in range(1, len(alist), 2):
      res.append(alist[i])
  return res

print 'prob 4'
print lst, oddIndex(lst)
print lst2, oddIndex(lst2)
print lst3, oddIndex(lst3)
print


# 5. Write a function that computes the running total of a list.

def total(alist):
  if len(alist) == 0: return 0
  if len(alist) == 1: return alist[0]
  else:
    total = alist[0]
    for i in range(1, len(alist)):
      total += alist[i]
  return total

print 'prob 5'
lst2noString = [-1, -6, -45, -99]
print lst,  'total is: ' , total(lst)
print lst2noString, 'total is: ' , total(lst2noString)
print lst3, 'total is: ' , total(lst3)
print


# 6. check if a string is a palindrome.
import string

def remove_punctuations(astring):
    return "".join(i.lower() for i in astring if i in string.ascii_letters)

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    text = remove_punctuations(text)
    return text == reverse(text)

s = "Rise to vote, sir."
t = "Valar morghulis... valar dohaeris"
print 'prob 6'
print 'the string ', s, 'is a palindrome... ', is_palindrome(s)
print 'the string ', t, 'is a palindrome... ', is_palindrome(t)
print 

# s3 = 'fox %$ jump'
# print remove_punctuations(s3)
# print 

# 7. compute the sum of numbers in a list using 
#    a. a for loop
#    b. a while loop
#    c. recursion
print 'prob 7'

alist = [1, 2, 3, 4, 5, -3]

# for loop
sum_for = alist[0]
for i in range(1, len(alist)):
  sum_for += alist[i]
print 'sum_for', sum_for

# while loop
j = 1
sum_wh = alist[0]
while j < len(alist):
  # print alist[j]
  sum_wh += alist[j]
  j += 1
print 'sum_wh', sum_wh

# recursion - http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsCalculatingtheSumofaListofNumbers.html
def listsum(alist):
   if len(alist) == 1:
        return alist[0]
   else:
        return alist[0] + listsum(alist[1:])

print 'rec sum', listsum(alist)

# 8. function on_all prints first 20 perfect squares

def on_all(n):
  ls = []
  for i in range(1, n+1):
    ls.append(i)
  # print ls
  squares = []
  for item in ls:
    squares.append(item * item)
  return squares

print on_all(20)
print

# prob 9. a function that concatenates two strings
print 'prob 9'
print 'first a simple way...'
a = 'cat and'
b = 'dog'
print a, b
print  'simple version', a + b

def concaten(a, b):
  newstring = ''
  for ch in a:
    newstring = newstring + ch 
  for ch in b:
    newstring = newstring + ch 
  return newstring

print 'function', concaten(a, b)

# same problem with lists:
ls_a = ['a', 'b', 'c']
ls_b = [1, 2, 3]
ls_c = ls_a + ls_b
print ls_a, "+", ls_b, "=", ls_c
print 

# prob 10 function combines two lists by alternatingly taking elements
print 'prob 10'
print 'different from zip: '
print  zip(ls_a, ls_b)

def altern(ls1,ls2):
  # assuming both lists have the same length
  ls = []
  for i in range(len(ls1)):
    ls.append(ls1[i])
    ls.append(ls2[i])
  return ls

print altern(ls_a, ls_b)

def altern2(ls1, ls2):
  if len(ls1) == 0 and len(ls2) == 0:
    return []
  elif len(ls1) == 0:
    return ls2
  elif len(ls2) == 0:
    return ls1
  else:
    ls = []
    i = 0
    j = 0
    while i < len(ls1) and j < len(ls2):
      ls.append(ls1[i])
      i += 1
      ls.append(ls2[j])
      j += 1

    if i == len(ls1): 
      for j in range(j, len(ls2)):
        ls.append(ls2[j])
    elif j == len(ls2):
      for i in range(1, len(ls1)):
        ls.append(ls1[i:])

  return ls

lsa = [1, 2, 3]
lsb = [10, 20, 30, 40, 50]

print altern2(lsa, lsb)
print 

# prob 11. merge 2 sorted lists into a new sorted list

def ms(ls1, ls2):
  # assuming no empty lists
  newls = []
  i = 0
  j = 0
  while i < len(ls1) and j < len(ls2):
    if ls1[i] < ls2[j]:
      newls.append(ls1[i])
      i += 1
    else:
      newls.append(ls2[j])
      j += 1

  if i == len(ls1): 
    for j in range(j, len(ls2)):
      newls.append(ls2[j])
  elif j == len(ls2):
    for i in range(1, len(ls1)):
      newls.append(ls1[i:])
  return newls
print 'prob 11'
print ms(lsa, lsb)
print 

# prob 12 Rotates a list k times

def rotations(k, ls):
  for rotation in range(k):
    t = ls.pop(0)
    ls.append(t)
  return ls

mylist = [1, 2, 3, 4, 5, 6]
print 'prob 12'
print rotations(2, mylist)
print

# prob 13 first 100 fib - not using recursion
print 'prob 13'

Fib = [1, 1]
for i in range(2, 99):
  Fib.append(Fib[i-1] + Fib[i-2])

# print Fib

print len(Fib)
print 

# prob 14
# print '702%10', 702%10
# print '702/10', 702/10
# print '70%10', 70%10
# print '7%10', 7%10
# print '7/10', 7/10

def digits(num): # assumes num is an integer
  ls = []
  while abs(num) > 0:
    ls.append(num%10)
    num = abs(num) / 10
  return ls[::-1]

print 'prob 14'
print digits(702)

print digits(1234567890)

print digits(0)

print digits(-170)


def digitsStr(num):
  ls = []
  for d in str(num):
    ls.append(d)
  return ls

print 'transforming into string'
print digitsStr(702)
print digitsStr(1234567890)
print digitsStr(-170)
print

# prob 15: add, subtract and multiply numbers in their digit list representation
print 'prob 15'

lsa = [7, 0, 2]
lsb = [1, 4, 2, 9]

def addDigitList(ls1, ls2):
  ls1 = ls1[::-1]
  ls2 = ls2[::-1]
  # print ls1, ls2
  ls3 = []
  i = 0
  j = 0

  while i < len(ls1) and j < len(ls2):
    ls3.append(ls1[i] + ls2[j])
    i += 1
    j += 1

  if i == len(ls1):
    for j in range(j, len(ls2)):
      ls3.append(ls2[j])
  elif j == len(ls2):
    for i in range(i, len(ls1)):
      ls3.append(ls1[i])
  print ls3

  r = 0
  for d in range(len(ls3)):
    if d == (len(ls3) - 1): # if digit is last, simply add r
      ls3[d] += r
     
    else:
      ls3[d] += r           
      if r > 0:
        r -= 1 
      
      if ls3[d] > 9:        # add 10 to next number
        ls3[d] -= 10
        r += 1

  return int("".join(str(d) for d in ls3[::-1]))

# testing
l1 = [9, 5, 6]
l2 = [2, 4, 6]

print addDigitList(l1, l2)


x = [4, 5, 6, 7, 8]
y = [4, 6, 5, 7, 8, 6, 6]

print addDigitList(x, y)





def subDigitList(ls1, ls2):
  # comparing values
  num1 = int("".join(str(d) for d in ls1))
  num2 = int("".join(str(d) for d in ls2))

  return num1 - num2 

print subDigitList(y, x)

print subDigitList(x, y)

m = [9, 5, 6]
n = [1, 2, 4, 6]

print subDigitList(m, n)
print


# prob 19
print 'prob 19'

def frameWords(str_list):
  max = 0       # length of the longest word
  r_spaces = 0  # num of spaces after each word
  top = ''      # top (or bottom) of frame

  # finding the largest word:
  for word in str_list:
    if len(word) > max:
      max = len(word)

  # calc length of top / bottom. The constant 4 is det by problem
  for i in range(max + 4):
    top = top + '*'
  print top
  
  # print each word followed by correct num of spaces
  for word in str_list:
    r_spaces = len(top) - len(word) - 4
    print '*'+' '+ word,
    for spaces in range(r_spaces):
      print '',
    print '*'

  # print bottom
  print top
  return 'end of frame' 


alist = ["Hello", "World", "in", "a", "frame"]
print frameWords(alist)

blist = ["This", "is", "a", "new", "more", "sophisticated", "test"]
print frameWords(blist)


# prob 20: pig latin
print 'prob 20'

def toPig(text):
  final_str = ''
  pig = 'ay'
  ltext = text.lower().strip().split(" ") # create a list of words

  for word in ltext:
    w = '' + word[1:] + word[0] + 'ay'
    final_str = final_str + w + ' '
    pig_latin = final_str[0].upper() + final_str[1:] # cap first ch
  return pig_latin
print 'to Pig Latin'
print toPig('The quick brown fox')
print

def fromPig(text):
  final_str = ''
  ltext = text.lower().strip().split(" ") # create a list of words

  for word in ltext:
    w = '' + word[-3] + word[0:-3]
    final_str = final_str + w + ' '
    normal_text = final_str[0].upper() + final_str[1:] # cap first ch
  return normal_text
print 'from Pig Latin'
print fromPig('Hetay uickqay rownbay oxfay')
print

