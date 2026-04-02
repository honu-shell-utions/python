# ----------------------------------------------------------------------------
# 256_tatami-free_rooms.py
#
# Tatami are rectangular mats, used to completely cover the floor of a room,
# without overlap.
#
# Assuming that the only type of available tatami has dimensions 1×2, there
# are obviously some limitations for the shape and size of the rooms that can
# be covered.
#
# For this problem, we consider only rectangular rooms with integer dimensions
# a, b and even size s = a·b.
#
# We use the term 'size' to denote the floor surface area of the room, and —
# without loss of generality — we add the condition a ≤ b.
#
# There is one rule to follow when laying out tatami: there must be no points
# where corners of four different mats meet.
#
# For example, consider the two arrangements below for a 4×4 room:
# (see pdf for pic)
#
# a red "X" in the middle, marks the point where four tatami meet in pic
# Because of this rule, certain even-sized rooms cannot be covered with
# tatami: we call them tatami-free rooms.
#
# Further, we define T(s) as the number of tatami-free rooms of size s.
#
# The smallest tatami-free room has size s = 70 and dimensions 7×10.
#
# All the other rooms of size s = 70 can be covered with tatami; they
# are: 1×70, 2×35 and 5×14.  Hence, T(70) = 1.
#
# Similarly, we can verify that T(1320) = 5 because there are exactly 5
# tatami-free rooms of size s = 1320: 20×66, 22×60, 24×55, 30×44 and 33×40.
#
# In fact, s = 1320 is the smallest room-size s for which T(s) = 5.
#
# Find the smallest room-size s for which T(s) = 200.
# see: A165764
# ----------------------------------------------------------------------------
import math, functools, itertools, operator
from time import time
from sympy import primerange
# ----------------------------------------------------------------------------
def tatami(m, n):
    if m <= 3:
        return True
    if m % 2:
        return n % (m - 1) <= n // (m - 1) * 2
    else:
        return (n + 1) % (m - 1) <= (n + 1) // (m - 1) * 2 + 2
# ----------------------------------------------------------------------------
def factor(x):
    factors = {}
    for p in primes:
        if p * p > x:
            break
        i = 0
        while x % p == 0:
            x //= p
            i += 1
        if i:
            factors[p] = i
    if x > 1:
        factors[x] = 1
    return factors
# ----------------------------------------------------------------------------
def ff(x):
    lf = [(k,v) for k,v in factor(x).items()]
    for x in itertools.product(*(range(v + 1) for k, v in lf)):
        yield functools.reduce(operator.mul, (a ** b for a, b in zip((k for k, v in lf), x)), 1)
# ----------------------------------------------------------------------------
def t(n):
    c = 0
    for m in ff(n):
        if m <= n // m:
            if not tatami(m, n // m):
                c += 1
    return c
# ----------------------------------------------------------------------------
start = time()
nmax = 10 ** 8
primes = list(primerange(2, math.sqrt(nmax)+1))

for n in range(0, nmax, 144):
    if t(n) == 200:
        print(f'Solution: {n}, Run-Time: {time()-start}')
        break
# ----------------------------------------------------------------------------
# solution: 85765680
# ----------------------------------------------------------------------------
