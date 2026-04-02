#  -----------------------------------------------------------------------------
from sympy import primefactors, isprime
from time import time
#  -----------------------------------------------------------------------------
def I(n):
    if isprime(n):
        return 1
    for i in range(n,0,(-1*max(primefactors(n)))):
        m = i+1
        if m*m%n==1 and m<=n-2:
            return m
        m = i-1
        if m*m%n==1 and m<=n-2:
            return m
    return 1
#  -----------------------------------------------------------------------------
def do_demo():
    for n in [7,15,100]:
        print('n =',n,'--->',I(n))
#  -----------------------------------------------------------------------------
do_demo()
for exp in range(1,8):
    start = time()
    limit = 2*10**exp
    total = 0
    for n in range(2,limit):
        total += I(n)
    print(f'Solution for n: 2*10^{exp} = {total:15}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------    
# 153651073760956
#  -----------------------------------------------------------------------------
