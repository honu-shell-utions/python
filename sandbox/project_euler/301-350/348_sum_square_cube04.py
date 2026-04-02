#  -----------------------------------------------------------------------------
#  Sum of a square and a cube
#  Problem 348
#  https://projecteuler.net/problem=348
#  -----------------------------------------------------------------------------
from collections import defaultdict
from time import time
from math import isqrt
#  -----------------------------------------------------------------------------
def is_pal(n):
    return str(n) == str(n)[::-1]
#  -----------------------------------------------------------------------------
start = time()
limit = 10**9
sq_max = isqrt(limit)+1
cu_max = int(limit**(1/3))+1
squares = set(i**2 for i in range(2,sq_max))
cubes = set(i**3 for i in range(2,cu_max))
numbers = {}

for xx in squares:
    for yyy in cubes:
        ndx = xx+yyy
        if is_pal(xx+yyy):
            a,b = isqrt(xx),round(yyy**(1/3))
            if ndx in numbers:
                numbers[ndx].append((a,b))
            else:
                numbers[ndx] = [(a,b)]

answer = 0
keys = sorted(numbers.keys())
print('-'*70)
for k in keys:
    if len(numbers[k]) == 4:
        print(f'{k:10} :',end='')
        for a,b in sorted(numbers[k]):
            print(f'({a:5},{b:<3})',end='')
        print()                       
        answer += k
print('-'*70)        
print(f'Solution: {answer}, Run-Time: {time()-start}')
print('-'*70)
#  -----------------------------------------------------------------------------
# Solution: 1004195061
#  -----------------------------------------------------------------------------
