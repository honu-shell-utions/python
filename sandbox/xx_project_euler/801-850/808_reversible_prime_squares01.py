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
from sympy import primerange
#  -----------------------------------------------------------------------------
def make_square_primes(n):
    primes = list(primerange(2,n+1))
    square_primes = [p**2 for p in primes]
    return square_primes
#  -----------------------------------------------------------------------------
def euler_808(n,target):
    total = 0
    count = 0
    square_primes = make_square_primes(n)
    for sp in square_primes:
        str_sp = str(sp)
        rev_sp = str_sp[::-1]
        if str_sp == rev_sp:
            continue
        if int(rev_sp) in square_primes:
            total += sp
            count += 1
            print(f'{count:2} {sp:18} {total:18}')
        if count == target:
            break
    return total
#  -----------------------------------------------------------------------------
print(euler_808(5*10**7,50))
#  -----------------------------------------------------------------------------
#  solution: 3807504276997394
#  -----------------------------------------------------------------------------
