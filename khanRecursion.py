# Khan Academy - recursion

# factorial function using a loop

def factLoop(n):
  res = 1
  
  for i in range(1, n+1):
    res = res * i
  return res


# print factLoop(5)
# print factLoop(6)
# print factLoop(0)

def factRec(n):
  if n == 0:
    return 1
  elif n >= 1:
    return n*factRec(n-1)


# print factRec(5)
# print factRec(6)
# print factRec(0)

def isPalin(s):
  if len(s) <= 1:
    return True

  if s[0] == s[-1]:
    s = s[1:-1]
    return isPalin(s)

  return False


# print isPalin("string")
# print isPalin("rotor")
# print isPalin("madamimadam")
# print isPalin("s")


# computes  x raised to power of n
def power(x, n):
  if n == 0:
    return 1

  if n<0:
    return float(1/power(x, -n))

  if n%2 != 0:
    return float(x*power(x, n-1))

  y = power(x, n/2)
  return float(y*y)

print power(3, 0)
print power(3, 4)
print power(5, -2)
print power(2, 5)
