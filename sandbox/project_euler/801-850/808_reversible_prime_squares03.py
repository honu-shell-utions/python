#  -----------------------------------------------------------------------------
#  Reversible prime squares
#  Problem 808
#  https://projecteuler.net/problem=808
#  
#  Both 169 and 961 are the square of a prime. 169 is the reverse of 961.
#  
#  We call a number a reversible prime square if:
#  
#  It is not a palindrome, and
#  It is the square of a prime, and
#  Its reverse is also the square of a prime.
#  169 and 961 are not palindromes, so both are reversible prime squares.
#  
#  Find the sum of the first 50 reversible prime squares.
#  -----------------------------------------------------------------------------
from math import isqrt
from sympy import sieve
from time import time
#  -----------------------------------------------------------------------------
def reverse(n):
    m = 0
    while n:
        m = 10*m + n%10
        n //= 10
    return m
#  -----------------------------------------------------------------------------
start = time()
candidates = []
for p in sieve:
    pp = p*p
    qq = reverse(pp)
    q = isqrt(qq)
    if qq == q*q and qq != pp and q in sieve:
        candidates.append(pp)
        if len(candidates) == 50:
            break
print(f'Solution: {sum(candidates)}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 3807504276997394
#  -----------------------------------------------------------------------------
