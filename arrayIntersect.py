def foo(a1, a2):
  return set(a1) & set(a2)


a1 = [2, 0, 1, 3, 2, 0, 5, 6, 7]

a2 = [2, 0, 5, 7, 7, 7, 7, 0]

print foo(a1, a2)