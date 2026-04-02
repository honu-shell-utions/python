"""
785_symmetric_diophantine.py
https://projecteuler.net/problem=785

Symmetric Diophantine Equation
Consider the following Diophantine equation:
15(x^2 + y^2 + z^2) = 34(xy + yz + zx) where x, y and z are positive
integers.

Let S(N) be the sum of all solutions, (x, y, z), of this equation such that,
1 ≤ x ≤ y ≤ z ≤ N and gcd(x, y, z) = 1

For N = 10^2, there are three such solutions - (1, 7, 16), (8, 9, 39),
(11, 21, 72). So S(10^2) = 184

Find S(10^9)
==============================================================================
page 16
difficulty 55%
pe_ans = 29526986315080920
==============================================================================

"""
import sympy as sp
from math import gcd,sqrt
sp.init_printing(use_unicode=True)
x,y,z = sp.symbols('x,y,z')

f = sp.Eq(15*x**2 + 15*y**2 + 15*z**2, 34*x*y+34*y*z+34*x*z)
sp.pprint(f)
sols = sp.solve(f,z)
for s in sols:
    sp.pprint(s)

N = 10**2
sols = []
for x in range(1,N+1):
    for y in range(x,N+1):
        if gcd(x,y) != 1:
            continue
        temp1 = x**2 + 17*x*y  + y**2
        if sqrt(temp1) != int(sqrt(temp1)):
            continue
        temp2 = 17*x/15 + 17*y/15
        temp3 = 8*sqrt(temp1)/15
        if temp2 + temp3 != int(temp2 + temp3):
            continue
        z = int(temp2 + temp3)
        if y <= z <= N:
            sols.append((x,y,z))

        
print(sols)
total = 0
for x,y,z in sols:
    total += x + y + z
print(total)
