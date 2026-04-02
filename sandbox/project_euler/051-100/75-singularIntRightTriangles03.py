################################################################################
from itertools import count
from math import gcd
import time
################################################################################
def projectEuler75(LIMIT):
    generator = ((s, t) for s in count(3, 2) for t in range(1, s, 2) if gcd(s,t) == 1)
    for s, t in generator:
        a = s * t
        b = (s ** 2 - t ** 2) // 2
        c = (s ** 2 + t ** 2) // 2
        parimeter = a + b + c
        if t == 1 and parimeter >= LIMIT:
            return
        for par in range(parimeter, len(hitCount) + 1, parimeter):
            hitCount[par] += 1                     
################################################################################
start = time.time()
LIMIT = 1_500_000
hitCount = [0] * (LIMIT + 1)
projectEuler75(LIMIT)
print('The solution:',hitCount.count(1),'Run time:',time.time()-start)
#Solution: 161667
################################################################################

