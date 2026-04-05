#  -----------------------------------------------------------------------------
#  Roots on the Rise
#  Problem 479
#  https://projecteuler.net/problem=479
#  -----------------------------------------------------------------------------
from numpy import roots
from time import time
#  -----------------------------------------------------------------------------
def S(n):
    total = 0
    for p in range(1,n+1):
        for k in range(1,n+1):
            coeff = [k, -k**2, 1,-k**3]
            a,b,c = roots(coeff)
            temp = (a + b)**p*(b + c)**p*(a + c)**p
            temp = round(temp.real+temp.imag)
            total += temp
            total %= MOD
    return total
#  -----------------------------------------------------------------------------
start = time()
MOD = 10**9 + 7
LIMIT = 4
print(f'Solution: {S(LIMIT)}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 191541795
#  -----------------------------------------------------------------------------
