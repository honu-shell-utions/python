#  -----------------------------------------------------------------------------
#  Sum of Squares
#  Problem 273
#  https://projecteuler.net/problem=273
#  -----------------------------------------------------------------------------
import math
from time import time
#  -----------------------------------------------------------------------------
start = time()
primes = [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113, 137, 149]
answer = 0
squares = []

for p in primes:
    found = False
    for a in range(1, 13):
        for b in range(a, 13):
            if a**2 + b**2 == p:
                found = True
            if a**2 + b**2 >= p:
                break
        if found:
            break
    answer += min(a, b)
    z = [(a,b)]
    for s in squares:
        c, d = a*s[0]+b*s[1], abs(a*s[1]-b*s[0])
        answer += min(c, d)
        z += [(c,d)]
        c, d = a*s[1]+b*s[0], abs(a*s[0]-b*s[1])
        answer += min(c, d)
        z += [(c,d)]
    squares += z
       
print(f'Solution: {answer}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 2032447591196869022
#  -----------------------------------------------------------------------------
