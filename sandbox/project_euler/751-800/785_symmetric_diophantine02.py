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
I reduced the equation to Pythagorean triples

p2 = d2 + 19z2, where p = (x+y+17z)/4 and d = y-x. Then
a2 + b2 = c2 where
a = 19z, b = 9p+10d, c = 10p+9d

Thus p = (10c - 9b)/19, d = (10b - 9c)/19

I enumerated the triples as z = r*2uv, b = r(u2 - v2),
c = r(u2 + v2) for an even z  or z = r*uv, b = r(u2 - v2)/2,
c = r(u2 + v2)/2 for an odd z. 0 < x <= y <= z is satisfied if
and only if u/5 < v < u/sqrt(19).

The code can be optimized by considering separately the case
when u is a multiple of 19. If it is, r = 2 or = 1, respectively.
If it isn't, r = 38 or r = 19 respectively.

"""
#  -----------------------------------------------------------------------------
from time import time
from math import sqrt, gcd
#  -----------------------------------------------------------------------------
def euler_785(N):
    N2 = round(sqrt(N))
    inv_rt19 = 1/sqrt(19)
    total = 0

    # 1. u % 19 == 0, u % 2 != v % 2, r = 2
    for u in range(19, int(sqrt(N*95)) + 1, 19):
        u2 = u * u
        vMin = int(u/5) + 1
        vMin += 1 - abs(vMin % 2 - u % 2)
        vMax = int(u*inv_rt19)
        for v in range(vMin, vMax+1, 2):
            uv = u * v
            if gcd(u, v) > 1:
                continue
            k = u//19
            kv = k * v
            if 4 * kv <= N:
                S = 8*(u*k - 8*kv + v*v)
                total += S
            else:
                break
                
    # 2. u % 19 == 0, u odd, v odd, r = 1
    for u in range(19, int(sqrt(N*95)) + 1, 38):
        vMin = int(u/5) + 1
        vMin += 1 - vMin % 2
        vMax = int(u*inv_rt19)
        for v in range(vMin, vMax+1, 2):
            if gcd(u, v) > 1:
                continue
            k = u//19
            kv = k*v
            if kv <= N:
                S = 2*(u*k - 8*kv + v*v)
                total += S
            else:
                break

    # 3. u % 19 != 0, u % 2 != v % 2, r = 38
    for u in range(1, int(sqrt(N*5)) + 1):
        if u % 19 == 0:
            continue
        u2 = u*u
        vMin = int(u/5) + 1
        vMin += 1 - abs(vMin%2 - u%2)
        vMax = int(u*inv_rt19)
        for v in range(vMin, vMax+1, 2):
            uv = u*v
            if gcd(u, v) > 1:
                continue
            if 4 * uv <= N:
                S = 8*(u2 - 8*uv + 19*v*v)
                total += S
            else:
                break

    # 4. u % 19 != 0, u odd, v odd, r = 19
    for u in range(1, int(sqrt(N*5)) + 1, 2):
        if u % 19 == 0:
            continue
        u2 = u * u
        vMin = int(u/5) + 1
        vMin += 1 - vMin % 2
        vMax = int(u * inv_rt19)
        for v in range(vMin, vMax+1, 2):
            uv = u * v
            if gcd(u, v) > 1:
                continue
            if uv <= N:
                S = 2*(u2 - 8*uv + 19*v*v)
                total += S
            else:
                break

    return total
#  -----------------------------------------------------------------------------
for exp in range(2,10):
    start = time()
    N = 10**exp
    print(f'Answer for N = 10^{exp:2}: {euler_785(N):17}, Run-Time: {time()-start:0.3f}')
#  -----------------------------------------------------------------------------
#N = 100  # Answer: 184
#N = 1000  # Answer: 28176
#N = 10**9  # Answer: 29526986315080920
#  -----------------------------------------------------------------------------
