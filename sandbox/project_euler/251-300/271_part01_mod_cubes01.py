#  -----------------------------------------------------------------------------
#  Modular Cubes, part 1
#  Problem 271
#  
#  For a positive number n, define S(n) as the sum of the integers x,
#  for which 1<x<n and x^3 ≡ 1 mod n.
#  
#  When n=91, there are 8 possible values for x, namely :
#      9, 16, 22, 29, 53, 74, 79, 81.
#      
#  Thus, S(91)=9+16+22+29+53+74+79+81 = 363.
#  
#  Find S(13082761331670030).
#  
#  https://projecteuler.net/problem=271
#  https://en.wikipedia.org/wiki/Chinese_remainder_theorem
#  https://www.ivl-projecteuler.com/overview-of-problems/60-difficulty/problem-271
#  -----------------------------------------------------------------------------
from sympy import primefactors
from itertools import product
from math import gcd
#  -----------------------------------------------------------------------------
def egcd(a, b):
    x, y, u, v, bb = 0, 1, 1, 0, b
    while b != 0:
        q = a // b
        a, b = b, a % b
        x, u = u - q * x, x
        y, v = v - q * y, y
    return u if u > 0 else u + bb
#  -----------------------------------------------------------------------------
def chinese(m, factors, x):
    e = [m // f * egcd(m // f, f) for f in factors]
    return sum(x * y for (x, y) in zip(e, x)) % m
#  -----------------------------------------------------------------------------
m = 13082761331670030
factors = primefactors(m)
r = [[a for a in range(1, f) if a ** 3 % f == 1] for f in factors]
solution = sum(chinese(m, factors, x) for x in product(*r)) - 1
print(solution)
#  -----------------------------------------------------------------------------
#  solution: 4617456485273129588
#  -----------------------------------------------------------------------------
