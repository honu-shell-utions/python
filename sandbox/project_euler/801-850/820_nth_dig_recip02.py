#  -----------------------------------------------------------------------------
#  Nth digit of Reciprocals
#  Problem 820
#  https://projecteuler.net/problem=820
#  https://www.xarg.org/puzzle/codesignal/reciprocal/
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def S(n):
    solution = 0
    for pos in range(1,n+1):
        res = pow(10, n, 10*pos) // pos
        solution += res
    return solution
#  -----------------------------------------------------------------------------
start = time()
print('-'*70)
print(f'Solution for n = {7:5}, {S(7):9}, Run-Time: {time()-start:8.2f}')
for exp in range(1,10):
    start = time()
    if exp == 7:
        print('-'*70)
    print(f'Solution for n = 10^{exp:2}, {S(10**exp):9}, Run-Time: {time()-start:8.2f}')
    if exp == 7:
        print('-'*70)
#  -----------------------------------------------------------------------------
#  solution: 44967734
#  -----------------------------------------------------------------------------
#  suppose you have 1/7 and want the 7th digit
#  1/7 = 0.14285714285714285
#  so the 7th digit is 1
#  10**7 = 10,000,000
#  10*7 = 70
#  10,000,000 mod 70 = 10
#  10 // 7 = 1 <--- this is the 7th digit
#  -----------------------------------------------------------------------------
