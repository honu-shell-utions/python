################################################################################
## 143-toricelli_triangles.py
## Problem 143
################################################################################
from math import sqrt, gcd
from time import time
################################################################################
def triple(m, n):
    a = m ** 2 - n ** 2
    b = 2 * m * n + n ** 2
    c = m ** 2 + n ** 2 + m * n
    a, b = min(a, b), max(a, b)
    return a, b, c
################################################################################        
def gen_triples(limit = 120000):
    result = set()
    for m in range(2, int(limit ** 0.5)):
        for n in range(1, m):
            if gcd(m, n) != 1:
                continue
            a, b, c = triple(m, n)
            if c > limit:
                break
            for i in range(1, limit // c + 1):
                result.add((a * i, b * i, c * i))
    return list(result)
################################################################################
def prob143(n = 120000):
    result = set()
    triples = gen_triples(n)
    index = dict()
    for a, b, c in triples:
        if a not in index:
            index[a] = set()
        if b not in index:
            index[b] = set()
        index[a].add(b)
        index[b].add(a)
    for p, r, c in triples:
        for q in index[p].intersection(index[r]):
            if p + r + q <= n:
                result.add(p + r + q)
    return sum(result)
################################################################################
print(prob143())
################################################################################
#solution: 30758397
################################################################################
