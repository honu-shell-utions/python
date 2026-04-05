"""
835_supernatural_triangles.py
https://projecteuler.net/problem=835

Supernatural Triangles
A Pythagorean triangle is called supernatural if two of its three sides are
consecutive integers.

Let S(N) be the sum of the perimeters of all distinct supernatural triangles
with perimeters less than or equal to N.
For example, S(100) = 258 and S(10000) = 172004.

Find S(10^10^10). Give your answer MODulo 1234567891
==============================================================================
"""
#  -----------------------------------------------------------------------------
import math
from time import time
#  -----------------------------------------------------------------------------
# emulate a + b sqrt 2 (MOD m)
class lin:
    x, y = 0, 0
    def __init__(self, x, y=0):
        self.x, self.y = x % MOD, y % MOD
    def __mul__(self, other):
        return lin(
            (self.x * other.x + 2 * self.y * other.y) % MOD, 
            (self.x * other.y + self.y * other.x) % MOD)
    def __add__(self, other):
        return lin((self.x + other.x) % MOD,
                   (self.y + other.y) % MOD)
    def __sub__(self, other):
        return lin((self.x - other.x) % MOD,
                   (self.y - other.y) % MOD)
    def __repr__(self):
        return str((self.x, self.y))
    def __pow__(self, k):
        k %= MOD**2-1
        t = self
        ans = lin(1)
        while k:
            if k & 1:
                ans *= t
            t = t*t
            k >>= 1
        return ans
    def __truediv__(self, other):
        return self * other**(-1)
#  -----------------------------------------------------------------------------
# sum for <= 10^n
def sum1(n):
    # (1+sqrt 2)^(2k+2) / (2 sqrt 2) <= 10^(10^10)
    t = int((n + math.log10(2 * math.sqrt(2))) / (2 * math.log10(1 + math.sqrt(2))))
    def geom_sum(a, l, r):
        return (a**l - a**r) / (a**0 - a**1)
    return ((geom_sum(lin(1, 1)**2, 3, t+1) - geom_sum(lin(1, -1)**2, 3, t+1)) / lin(0, 2)).x
#  -----------------------------------------------------------------------------
def sum2(n):
    # (2k+1)(2k+2) <= 10^n
    t = lin(10)**(n//2) / lin(2)
    return (t*(t+lin(1))*(lin(4)*t-lin(1)) / lin(3) - lin(2)).x
#  -----------------------------------------------------------------------------
MOD = 1234567891
for exp in range(2,11):
    start = time()
    N = 10**exp
    res = sum1(N)+sum2(N)
    print(f'Solution for N = 10^10^{exp:2}: {res:11}, Run-Time: {time()-start:0.3f}')    
#  -----------------------------------------------------------------------------
#  solution: 1050923942
#  -----------------------------------------------------------------------------

