# testing string properties

# s = 'abcde'
# n = len(s)
# print n
# s[0], s[4] = s[4], s[0]
# print s

def revStr(s):
  arr = []
  for ch in s:
    arr.append(ch)

  n = len(arr)
  l = 0
  r = n-1

  while l < r:
    if not arr[l].isalpha():
      l += 1
    elif not arr[r].isalpha():
      r -= 1
    else:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
      r -= 1
  res = ''.join(arr)    
  return res



import unittest

class testRev(unittest.TestCase):
  """
  Our basic test class
  """

  def test_rev(self):
    """
    The actual test. Any method which starts with ``test_`` will  be considered a test case.
    """
    res = revStr("a!!!b.c.d,e'f,ghi")
    self.assertEqual(res, "i!!!h.g.f,e'd,cba")


if __name__ == '__main__':
    unittest.main()




