#  -----------------------------------------------------------------------------
#  Sum of a square and a cube
#  Problem 348
#  https://projecteuler.net/problem=348
#  -----------------------------------------------------------------------------
from collections import defaultdict
from time import time
from math import isqrt
#  -----------------------------------------------------------------------------
def is_palindromic(n):
    return str(n) == str(n)[::-1]
#  -----------------------------------------------------------------------------
start = time()
limit = 10**9
sq_max = isqrt(limit)+1
cu_max = int(limit**(1/3))+1
squares = set(n**2 for n in range(1, sq_max))
cubes = set(n**3 for n in range(1, cu_max))
numbers = defaultdict(int)

for square in squares:
    for cube in cubes:
        if is_palindromic(square + cube):
            numbers[square + cube] += 1

answer = 0
for n,ct in numbers.items():
    if ct == 4:
        print(n)
        answer += n
        
print(f'Solution: {answer}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
# Solution: 1004195061
#  -----------------------------------------------------------------------------
