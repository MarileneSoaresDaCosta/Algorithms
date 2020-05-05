# comparing dicts
d1 = {'a': 1, 'b':2, 'c':3, 'd': 0}
d2 = {'d':0,'a': 1, 'b':2, 'c':3}
d3 = {'a': 1, 'b':2}

print 'testing d1 == d2:'
if d1 == d2:
	print 'ok, d1 == d2'
else:
	'oops... d1 should be == to d2'

print 'testing d1 != d3'
if d1 == d3:
	print 'oops... d1 should be != to d3'
else:
	print 'ok, d1 != d3'