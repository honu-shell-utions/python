#  -----------------------------------------------------------------------------
#  The Ackermann function
#  Problem 282
#  https://projecteuler.net/problem=282
#  -----------------------------------------------------------------------------
from math import gcd, lcm
from sympy import factorint
from time import time
#  -----------------------------------------------------------------------------
def factor(n):
    factors = []
    for f in factorint(n):
        factors.append(f)
    return factors
#  -----------------------------------------------------------------------------
def tot(n):
    for p in factor(n):
        n -= n // p
    return n
#  -----------------------------------------------------------------------------
def ack(m, n):
    if m <= 3:
        if m == 0:
            return n + 1
        if n == 0:
            return ack(m - 1, 1)
        else:
            return ack(m - 1, ack(m, n - 1))
    if m == 4:
        return tet(2, n + 3) - 3
    else:
        return tet(2, cycle) - 3
#  -----------------------------------------------------------------------------
def tet(a, b):
    x = 1
    y = 1
    for i in range(b):
        x = pow(a, x, m)
        if y == x:
            return x
        y = x
    return x
#  -----------------------------------------------------------------------------
start = time()
mod = 14**8
m = lcm(mod, tot(mod))
cycle = 0
mm = m
while mm != 1:
    mm = tot(mm)
    cycle += 1

solution = sum(ack(n, n) for n in range(7)) % mod
print(f'Solution: {solution}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 1098988351
#  -----------------------------------------------------------------------------
