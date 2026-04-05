#  -----------------------------------------------------------------------------
#  Biclinic Integral Quadrilaterals
#  Problem 311
#  https://projecteuler.net/problem=311
#  -----------------------------------------------------------------------------
from math import gcd
from time import time
#  -----------------------------------------------------------------------------
def euler_311(n):
    b_max = int(n**0.5) // 2   # factor of // 2 found empirically, not exact bound
    triangles = [[0] * (b_max + 1) for _ in range(b_max + 1)]
    for b in range(2, b_max + 1):
        d_start = 1 if b % 2 else 2    # differing parity b and d will always produce odd x
        d_max = min(b - 1, int((n - b**2)))
        for d in range(d_start, d_max + 1, 2):
            p, q = b - d, b + d
            g = gcd(p, q)
            a, c = p // g, q // g
            i_min = d // a
            if i_min * a < d:
                i_min += 1
            i_min_2 = (b - d) // (c - a)
            if i_min_2 * (c - a) <= b - d:
                i_min_2 += 1
            i_min = max(i_min, i_min_2)
            if (a + c) % 2:
                i_delta = 2
                if i_min % 2:
                    i_min += 1
            else:
                i_delta = 1
            for i in range(i_min, int(n**0.5) + 1, i_delta):
                A, B = a * i + b, c * i + d
                if A**2 + B**2 > n // 2:
                    break
                x = (c - a) * i + (b + d)
                C = (a + c) * i + (b - d)
                triangles[C // 2][x // 2] += 1
    total = 0
    for row in triangles:
        for v in row:
            total += v * (v - 1)
    total //= 2
    return total
#  -----------------------------------------------------------------------------
for exp in [4,6,8,10]:
    start = time()
    n = 10**exp
    print(f'Solution for n = 10^{exp:2}: {euler_311(n):10}, Run-Time: {time()-start:.3f}') 
#  -----------------------------------------------------------------------------
#  solution: 2466018557
#  -----------------------------------------------------------------------------
