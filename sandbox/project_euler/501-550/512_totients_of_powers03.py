from math import floor
from sympy.ntheory.factor_ import totient
from time import time

def g(n):
    total = 0
    for i in range(1,floor((n+1)/2)+1):
        total += totient(2*i-1)
    return total
    
for exp in [2,3,4,5,6,7,8]:
    start = time()
    limit = 10**exp
    if exp == 8:
        limit *= 5
    print(f'Solution for n = {limit:10}: {g(limit):18}, Run-Time: {round(time()-start,2)} seconds.')
    

    
    
