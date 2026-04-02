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
from sympy import nextprime, isprime
from time import time
#  -----------------------------------------------------------------------------
def euler_808(N):
    L = []
    s = 0
    while len(L) < N:
        s = nextprime(s)
        p = s ** 2
        q = int(str(p)[::-1])
        r = q ** .5
        if p != q and r == int(r) and isprime(int(r)):
            L += [p]
    return sum(L)
#  -----------------------------------------------------------------------------
start = time()
print(f'Solution: {euler_808(50)}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 3807504276997394
#  -----------------------------------------------------------------------------
