# ----------------------------------------------------------------------------
from fractions import Fraction
from time import time
# ----------------------------------------------------------------------------
def gen(m, n):
    x = m
    r = set()
    for i in range(m + 1, n):
        for a in cache[(m, i)]:
            for b in cache[(i, n)]:
                r.add(a + b)
                r.add(a - b)
                r.add(a * b)
                if b:
                    if isinstance(a, int) and isinstance(b, int) and a % b == 0:
                        r.add(a // b)
                    else:
                        r.add(Fraction(a, b))
        x = x * 10 + i
    r.add(x)
    return r
# ----------------------------------------------------------------------------
start = time()
nmax = 10
cache = {}

for j in range(1, nmax + 1):
    for k in range(1, nmax - j + 1):
        cache[(k, k + j)] = gen(k, k + j)

s = sum(x for x in cache[(1, nmax)]
        if x > 0 and (isinstance(x, int) or x.denominator == 1))

print(f'Solution: {s}, Run-Time: {time()-start}')
# ----------------------------------------------------------------------------
# solution: 20101196798
# ----------------------------------------------------------------------------
