## -----------------------------------------------------------------------------
## Angular Bisectors
## Problem 257
## Given is an integer sided triangle ABC with sides a ≤ b ≤ c.
## (AB = c, BC = a and AC = b).
## The angular bisectors of the triangle intersect the sides
## at points E, F and G (see picture).
## 
## The segments EF, EG and FG partition the triangle ABC into
## four smaller triangles: AEG, BFE, CGF and EFG.
## It can be proven that for each of these four triangles the
## ratio area(ABC)/area(subtriangle) is rational.
## However, there exist triangles for which some or all of
## these ratios are integral.
## 
## How many triangles ABC with perimeter ≤ 100,000,000 exist so
## that the ratio area(ABC)/area(AEG) is integral?
## -----------------------------------------------------------------------------
## NOTES:
##  (a+b)(a+c)/bc = n where 2<=n<=4 (a=b=c for n=4) like everyone
##  else. From n=2 I observed that
##  [a, b, c] = [ pq, p(2p+q), q(p+q) ] for co-prime p, q.
##  Assuming n=3 result should have similar form, I also
##  found that [a, b, c] = [ 2pq, p(3p+q), q(p+q) ] but
##  divide by 2 when GCD(a, b, c) = 2 to get
##  primitive triplet. Triplets with GCD(a, b, c) > 2 are
##  not primitive.
## -----------------------------------------------------------------------------
from math import gcd, isqrt
from time import time
## -----------------------------------------------------------------------------
def euler_257(limit, n):
    count = 0
    for p in range(1,isqrt(limit//2) + 1):
        for q in range(p + 1, limit):
            a = (n - 1) * p * q
            b = p * (q + n * p)
            c = q * (p + q)
            if c >= a + b:
                break
            g = gcd(a, b, c)
            if g > 2:
                continue
            a, b, c = a//g, b//g, c//g
            b, c = min(b, c), max(b, c)
            if c >= a + b:
                continue
            if a + b + c > limit:
                continue
            count += limit // (a + b + c)
    return count
## -----------------------------------------------------------------------------
start = time()
limit = 10**8
solution = euler_257(limit, 2) // 2 + euler_257(limit, 3) + limit // 3
print(f'Solution: {solution}, Run-Time: {time()-start}')          
## -----------------------------------------------------------------------------
## solution: 139012411
## -----------------------------------------------------------------------------
