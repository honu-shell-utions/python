#  -----------------------------------------------------------------------------
#  Divisible Palindromes
#  Problem 655
#  https://projecteuler.net/problem=655
#  -----------------------------------------------------------------------------
from itertools import count
from time import time
#  -----------------------------------------------------------------------------
def palindrome_gen():
    yield 0
    for digits in count(1):
        first = 10 ** ((digits - 1) // 2)
        for s in map(str, range(first, 10 * first)):
            yield int(s + s[-(digits % 2)-1::-1])
#  -----------------------------------------------------------------------------
start = time()
factor = 10000019
hits = 0
for p in palindrome_gen():
    if p > 10**32:
        break
    if p < factor:
        continue
    if p % factor == 0:
        hits += 1
    if hits > 100:
        break
print('01',time()-start)
#  -----------------------------------------------------------------------------
#  solution: 2000008332
#  -----------------------------------------------------------------------------
