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
from time import time
from math import sqrt,isqrt
#  -----------------------------------------------------------------------------
def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(isqrt(n) + 1):
        if result[i]:
            for j in range(2 * i, len(result), i):
                result[j] = False
    return result
#  -----------------------------------------------------------------------------
def is_not_palindrome(x):
    if x == x[::-1]:
        return False
    return True
#  -----------------------------------------------------------------------------
def is_quadratic(x):
    return sqrt(x) == isqrt(x)
#  -----------------------------------------------------------------------------
def euler_808(n, limit=5 * 10**7):
    is_prime = list_primality(limit)
    primes = tuple((i for (i, isprime) in enumerate(is_prime) if isprime))
    values = []
    for x in primes[4:]:
        sq = str(pow(x, 2))
        if is_not_palindrome(sq):
            rev = int(sq[::-1])
            if is_quadratic(rev):
                if is_prime[isqrt(rev)]:
                    values.append(int(sq))
                    values.append(rev)
    return sum(sorted(set(values))[:n]), len(sorted(set(values)))
#  -----------------------------------------------------------------------------
start = time()
ans, count = euler_808(50)
print(f'The first {count} reversible prime squares sum to: {ans:,}.\
\nRun-Time: {time()-start:6.3f} seconds.')
#  -----------------------------------------------------------------------------
#  solution: 3807504276997394
#  -----------------------------------------------------------------------------
