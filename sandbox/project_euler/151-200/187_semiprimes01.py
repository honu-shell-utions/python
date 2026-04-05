from sympy import factorint
from time import time

start = time()
total = 0
for k in range(2,10**8):
    x = factorint(k).values()
    if sum(x) == 2:
        total += 1

		
print(f'Solution: {total}, Run-Time: {time()-start}')
#solution: 17427258
