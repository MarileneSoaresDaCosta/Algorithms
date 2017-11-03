# generates a string, and compares with one phrase until 100% correct
import random
import string

phrase = 'we'

def gen():
  L = []
  for k in range(len(phrase)):
    c = random.choice(string.ascii_lowercase)
    L.append(c)
    new_string = "".join(str(x) for x in L)
  return new_string
  #return c



def grade(new_string):
  g = 0
  for c in range(len(phrase)):
    if new_string[c] == phrase[c]:
      g += 1
  #print new_string
  #if new_string == phrase:
   # g = 1
  return g


#print grade(gen())


def weasel():
  for k in range(10000): 
    s = gen()
    G = grade(s)
    if G == 2:
      return G, s

  return 'nope'

print weasel()



