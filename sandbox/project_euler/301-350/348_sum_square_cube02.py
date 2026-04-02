#  -----------------------------------------------------------------------------
#  Sum of a square and a cube
#  Problem 348
#  https://projecteuler.net/problem=348
#  -----------------------------------------------------------------------------
from itertools import count
from time import time
#  -----------------------------------------------------------------------------
def pal_gen():
    yield 0
    for digits in count(1):
        first = 10 ** ((digits - 1) // 2)
        for s in map(str, range(first, 10 * first)):
            yield int(s + s[-(digits % 2)-1::-1])
#  -----------------------------------------------------------------------------
start = time()
ct, answer = 0, 0
pg = pal_gen()
while True:
    p = next(pg)
    n = 0
    x = 2
    while x**3 < p-1:
        s = p - x**3
        if int(s**0.5)**2 == s:
            n += 1
        x += 1
    if n == 4:
        ct += 1
        answer += p
    if ct == 5:
        break
    
print(f'Solution: {answer}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
# Solution: 1004195061
#  -----------------------------------------------------------------------------
