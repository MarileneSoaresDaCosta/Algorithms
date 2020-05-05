# testing regex

import re

s = '(?i)(caterpillar)'
comp_s = re.compile(s)
longS = "the cat and the CatErpiLlar met"
longS2 = "there is nothing like that here..."
print "test 1"
if re.search(comp_s, longS):
	print 'ok'
else:
	print 'not found'

print "test 2"
if re.search(comp_s, longS2):
	print 'ok'
else:
	print 'not found'