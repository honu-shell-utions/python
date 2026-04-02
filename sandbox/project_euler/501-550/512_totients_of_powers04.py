from time import time
from sympy import primefactors
from decimal import Decimal

start=time()
result=Decimal(0)
def phi(n1):
    n=Decimal(n1)
    prod = n
    for i in primefactors(n): 
        prod -= prod // i
    return prod%(n+1)

def g(n1):
    n=Decimal(n1)
    return Decimal(((n*n-1)/2)%(n+1)+phi(n))
       
for exp in [2,3,4,5,6,7,8]:
    start = time()
    limit = 10**exp
    if exp == 8:
        limit *= 5
    result= sum(g(i) for i in range(1,limit+1,2))
    print(f'Solution for n = {limit:10}: {result:18}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 50660591862310323
#  -----------------------------------------------------------------------------
