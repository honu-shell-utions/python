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
#  -----------------------------------------------------------------------------
from sympy import primefactors
from sympy.ntheory.modular import crt
from itertools import product
#  -----------------------------------------------------------------------------
facs = primefactors(13082761331670030)

findCubeRoots = lambda p:[n for n in range(1,p) if (n**3)%p==1]

res = sum([int(crt(facs,rems)[0]) for rems in product(*map(findCubeRoots,facs))])

print(res-1)
#  -----------------------------------------------------------------------------
#  solution: 4617456485273129588
#  -----------------------------------------------------------------------------
