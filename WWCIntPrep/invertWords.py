# invert words

def reverse(astring, lo, hi):
  arr = astring.split()
  print arr
  while lo < hi:
    print lo, hi
    arr[lo], arr[hi] = arr[hi], arr[lo]
    lo += 1
    hi -= 1

def reverse_words(arr):
  lo = 0
  reverse(arr, 0, len(arr)-1)
  for index, letter in enumerate(arr):
    if index == ' ':
      reverse(arr, lo, index-1)
      lo = index + 1
  reverse(arr, lo, len(arr - 1))


a = 'hello world'
# print reverse_words(a)
print reverse(a, 0, 10)