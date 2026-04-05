#  -----------------------------------------------------------------------------
#   The millionth number with at least one million prime factors
#   Problem 615
#   https://projecteuler.net/problem=615
#   
#   Consider the natural numbers having at least 5 prime factors,
#   which don't have to be distinct.
#   Sorting these numbers by size gives a list which starts with:
#   
#   32=2⋅2⋅2⋅2⋅2
#   48=2⋅2⋅2⋅2⋅3
#   64=2⋅2⋅2⋅2⋅2⋅2
#   72=2⋅2⋅2⋅3⋅3
#   80=2⋅2⋅2⋅2⋅5
#   96=2⋅2⋅2⋅2⋅2⋅3
#     ...
#   So, for example, the fifth number with at least 5 prime factors is 80.
#   
#   Find the millionth number with at least one million prime factors.
#   Give your answer modulo 123454321.

#    As the base case I considered the number 2^1,000,000. I then worked through
#    recursively replacing 2s with larger prime factors.  In that way we get a list
#    of numbers with exactly one million prime factors.  To get numbers with more
#    than one million prime factors we can simply multiply those numbers by powers of two.
#
#    To make this efficient I found an upper limit (through trial and error) for
#    the value of the desired number.
#  -----------------------------------------------------------------------------
from fractions import Fraction
from time import time
from sympy import primerange
#  -----------------------------------------------------------------------------
def compute_set(val=Fraction(1,1),ind=1):
    res = [val]
    m = 2
    while val*m <= lim:
        res.append(val*m)
        m *= 2
    for i in range(ind,len(primes)):
        temp = val*Fraction(primes[i],2)
        if temp <= lim:
            res += compute_set(temp,i)
        else:
            break
    return res
#  -----------------------------------------------------------------------------
start = time()
MOD = 123454321
primes = list(primerange(2,18*10**4))
lim = Fraction(primes[-1],2)	

# sort values                                                                   
values = sorted(compute_set())

# compute the numerical value of the solution                                   
frac = values[10**6-1]
num = frac.numerator
den = frac.denominator

# compute the number of 2s that have been removed                               
while den % 2 == 0:
    den //= 2

solution = (num*pow(2,10**6-den,MOD)) % MOD        
print(f'Solution: {solution}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 108424772
#  -----------------------------------------------------------------------------
