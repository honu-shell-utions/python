#  -----------------------------------------------------------------------------
#  Gozinta Chains
#  Problem 548
#  https://projecteuler.net/problem=548
#  -----------------------------------------------------------------------------
from sympy import divisors
from itertools import combinations, chain
#  -----------------------------------------------------------------------------
def g(n):
    divs = divisors(n)
    return chain(combinations(divs, r) for r in range(2, len(divs)+1))
#  -----------------------------------------------------------------------------
def process(s,n):
    if s[0] != 1 or s[-1] != n:
        return False
    for ndx in range(len(s)-1):
        if s[ndx+1] % s[ndx] != 0:
            return False
    return True
#  -----------------------------------------------------------------------------
for n in [12,48,120]:
    count = 0
    seqs = g(n)
    for seq in seqs:
        for s in seq:
            if process(s,n):
                #print(s,end= ' ')
                count += 1
    print(f'For n = {n:8} ----> {count:10}')
#  -----------------------------------------------------------------------------
#  solution: 12144044603581281
#  -----------------------------------------------------------------------------
