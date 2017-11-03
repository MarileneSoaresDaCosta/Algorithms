#!/usr/bin/env python
from sympy import *
a = Rational(1,2)
# print "a = Rational(1,2). So a = ", a
# print a
# print "pi ** 2 = ", pi**2

x = Symbol('x')
y = Symbol('y')
print 'x+y+x+y = ', x+y+x+y
print '(x+y)**2 = ', (x+y)**2

print 'expand((x+y)**3) = ', expand((x+y)**3)  
print "simplify((x+x*y)/x) = ", simplify((x+x*y)/x)

print "solve(x**4 - 1, x): ", solve(x**4 - 1, x)


'''
Another alternative in the case of polynomial equations 
is factor. 
factor returns the polynomial factorized into irreducible 
terms, and is capable of computing the factorization over 
various domains:
'''

f = x**4 - 3*x**2 + 1
print factor(f)

import numpy
print "numpy.roots([2,-6]): ", numpy.roots([2,-6])  


x, y, z = symbols('x, y, z')
init_printing(use_unicode=True)
print "simplify(sin(x)**2 + cos(x)**2): ", simplify(sin(x)**2 + cos(x)**2)

print "simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)): ", simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)) 

# limitations of simplify - compare the following case with factor

print simplify(x**2 + 2*x + 1)
#  this one results in x**2 + 2*x + 1

print factor(x**2 + 2*x + 1) 
#  this one results in (x + 1)**2, the result we expected
















