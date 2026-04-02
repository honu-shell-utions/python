#  -----------------------------------------------------------------------------
#  Pythagorean Polygons
#  Problem 292
#  https://projecteuler.net/problem=292
#  -----------------------------------------------------------------------------
# A "polygon" is equivalent to a bunch of vectors
# <ka, kb> whose sum is <0, 0> and the sum of the lengths <= N
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def update(counts, a, b, c):
    newcounts = {}
    for t in counts:
        x, y, p = t
        cnt = counts[t]
        kMax = (N - p)//c
        for k1 in range(kMax+1):
            for k2 in range(kMax - k1 + 1):
                s, d = k1 + k2, k1 - k2
                t1 = (x1, y1, p1) = (x + d*a, y + d*b, p + s*c)
                if x1*x1 + y1*y1 <= (N-p1)**2:
                    if t1 in newcounts:
                        newcounts[t1] += cnt
                    else:
                        newcounts[t1] = cnt
    return newcounts
#  -----------------------------------------------------------------------------
triples = ((3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29),
            (12, 35, 37), (9, 40, 41), (28, 45, 53))

for N in [4,30,60,120]:
    start = time()
    vectors = [(1, 0, 1), (0, 1, 1)]
    for a, b, c in triples:
        if c <= N//2:
            vectors += [(a, b, c), (a, -b, c), (b, a, c), (b, -a, c)]
    counts = {(0, 0, 0): 1}
    cnt2 = 0
    for a, b, c in vectors:
        counts = update(counts, a, b, c)
        cnt2 += N//(2*c)   # counts two-sided "polygons"
        print(a, b, c, len(counts))

    ans = sum(counts.get((0, 0, p), 0) for p in range(1, N+1)) - cnt2
    print(f'For N = {N:d}, Solution: {ans}, Time = {time()-start:.1f}')
#  -----------------------------------------------------------------------------
#  solution for N = 120: 3600060866
#  -----------------------------------------------------------------------------
