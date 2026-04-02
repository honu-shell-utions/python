#-------------------------------------------------------------------------------
##Rational zeros of a function of three variables 
##Problem 180
##For any integer n, consider the three functions
##
##f(1,n)(x,y,z) = x^(n+1) + y^(n+1) − z^(n+1)
##f(2,n)(x,y,z) = (xy + yz + zx)*(x^(n-1) + y^(n-1) − z^(n-1))
##f(3,n)(x,y,z) = xyz*(x^(n-2) + y^(n-2) − z^(n-2))
##
##and their combination
##
##f(n)(x,y,z) = f(1,n)(x,y,z) + f(2,n)(x,y,z) − f(3,n)(x,y,z)
##
##We call (x,y,z) a golden triple of order k if x, y, and z are
##all rational numbers of the form a / b with
##0 < a < b ≤ k and there is (at least) one integer n,
##so that f(n)(x,y,z) = 0.
##
##Let s(x,y,z) = x + y + z.
##Let t = u / v be the sum of all distinct s(x,y,z) for
##all golden triples (x,y,z) of order 35.
##
##All the s(x,y,z) and t must be in reduced form.
##
##Find u + v.
#-------------------------------------------------------------------------------
# x,y,z are rational a/b with 0 < a < b <= 35
#-------------------------------------------------------------------------------
from fractions import Fraction
from time import time
#-------------------------------------------------------------------------------
start = time()
K = 35
rats = set()
for b in range(1, K+1):
  for a in range(1, b):
    rats.add(Fraction(a, b))
rats = sorted(rats)
#print (len(rats))

ans_set = set()
for x in rats:
  for y in rats:
    for n in [-1, -2, 1,2]:
      val = (x**n + y**n)**(1.0/n)
      z = Fraction(val).limit_denominator(K)
      if 0 < z.numerator < z.denominator <= K and x**n + y**n == z**n:
        ans_set.add(x+y+z)

ans = sum(ans_set)
print (f'Solution: {ans.numerator+ans.denominator},Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#solution: 285196020571078987
#-------------------------------------------------------------------------------
