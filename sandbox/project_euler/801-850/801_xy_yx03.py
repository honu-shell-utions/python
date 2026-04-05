#  -----------------------------------------------------------------------------
#  x**y = y**x (mod n)
#  Problem 801
#  https://projecteuler.net/problem=801
#  -----------------------------------------------------------------------------
from collections import defaultdict
from sympy import sieve, divisors
from time import time
from sympy.ntheory.factor_ import totient
#  -----------------------------------------------------------------------------
def S(M,N):
    ans = 0
    for p in sieve:
        if p < M:
            continue
        if p > N:
            break
        d = divisors(p-1)
        order_apperances = defaultdict(int)
        for order in d:
            for contained_order in d:
                if order % contained_order == 0:
                    order_apperances[contained_order] += ((p-1)//order)*totient(order)           
        ans += (p-1)**2
        for order in d:
            ans += totient(order) * (order_apperances[order]**2)
    return ans % MOD
#  -----------------------------------------------------------------------------
MOD = 993353399
for M,N in [(1,10**2),(1,10**5),(10**16,10**16 + 10**6)]:
    start = time()
    print(f'Answer for (M,N)= ({M},{N}): {S(M,N):10}')
    print(f'Run-Time        = {(time() - start)//60} minutes.')
#  -----------------------------------------------------------------------------
#  solution: 638129754
#  -----------------------------------------------------------------------------
