from sympy import primerange
from time import time

start = time()
limit = 10**8
print('loading primes')
primes = list(primerange(2,limit))
count01 = 0
count02 = 0
print('in nested loop')
for p1 in primes:
    for p2 in primes:
        if p1*p2 < limit:
            if p1 == p2:
                count01 += 1
            else:
                count02 += 1
        else:
            break

print(f'Solution: {count01 + count02//2}, Run-Time: {time()-start}')
#solution: 17427258
