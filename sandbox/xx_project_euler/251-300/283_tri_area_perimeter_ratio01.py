"""
283_tri_area_perimeter_ratio.py
https://projecteuler.net/problem=283

Integer Sided Triangles for Which The Area/Perimeter Ratio is Integral
Consider the triangle with sides 6, 8 and 10. It can be seen that the
perimeter and the area are both equal to 24. So the area/perimeter ratio
is equal to 1.

Consider also the triangle with sides 13, 14 and 15. The perimeter equals
42 while the area is equal to 84. So for this triangle the area/perimeter
ratio is equal to 2.

Find the sum of the perimeters of all integer sided triangles for which the
area/perimeter ratios are equal to positive integers not exceeding 1000.
==============================================================================
page 6
difficulty 75%
pe_ans = 28038042525570324
==============================================================================
"""
#  -----------------------------------------------------------------------------
import itertools, operator, functools
from sympy import factorint
from math import gcd,sqrt
from time import time
#  -----------------------------------------------------------------------------
def ff(x):
    lf = [(k,v) for k,v in factorint(x).items()]
    for x in itertools.product(*(range(v + 1) for k, v in lf)):
        yield functools.reduce(operator.mul, (a ** b for a, b in zip((k for k, v in lf), x)), 1)
#  -----------------------------------------------------------------------------
def euler_283(nmax):
    s = 0
    for m in range(1, nmax + 1):
        for u in range(1, 2 * m + 1):
            if 2 * m % u == 0:
                for v in range(1, int(sqrt(3) * u) + 1):
                    if gcd(u, v) == 1:
                        t = 4 * m ** 2 * (u ** 2 + v ** 2)
                        for d1 in ff(t):
                            d2 = t // d1
                            if d1 <= d2 and (d1 + 2 * m * u) % v == 0 and \
                               (d2 + 2 * m * u) % v == 0 and \
                               (u >= v or d1 * u >= 2 * m * (v ** 2 - u ** 2)):
                                a = (d1 + 2 * m * u) // v + 2 * m * v // u
                                b = (d2 + 2 * m * u) // v + 2 * m * v // u
                                c = (d1 + d2 + 4 * m * u) // v
                                s += a + b + c
    return s
#  -----------------------------------------------------------------------------
start = time()
print(f'Solution: {euler_283(1000)}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  -----------------------------------------------------------------------------
