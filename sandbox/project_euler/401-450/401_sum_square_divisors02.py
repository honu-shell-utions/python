#  -----------------------------------------------------------------------------
#  Sum of squares of divisors
#  Problem 401
#  
#  The divisors of 6 are 1,2,3 and 6.
#  The sum of the squares of these numbers is 1+4+9+36=50.
#  
#  Let sigma2(n) represent the sum of the squares of the divisors of n.
#  Thus sigma2(6)=50.
#  
#  Let SIGMA2 represent the summatory function of sigma2, that is
#  SIGMA2(n)=∑ sigma2(i) for i=1 to n.
#  
#  The first 6 values of SIGMA2 are: 1,6,16,37,63 and 113.
#  
#  Find SIGMA2(10^15) modulo 10^9.
#
#  https://oeis.org/A064602
#  -----------------------------------------------------------------------------
from time import time
from math import isqrt
#  -----------------------------------------------------------------------------
class euler_401:
    def __init__(self,limit):
        self.n = limit
        self.mod = 10**9
    #  ------------------------------------------------------------------------
    def f(self,x):
        return x*(x+1)*(2*x+1) // 6
    #  ------------------------------------------------------------------------
    def SIGMA2(self):
        s = isqrt(self.n)
        temp = sum(self.f(self.n//k) + k*k*(self.n//k)\
                       for k in range(1, s+1)) - s*self.f(s)
        return temp % self.mod
#  -----------------------------------------------------------------------------
for limit in range(1,10):
    start = time()
    sol = euler_401(limit)
    res = sol.SIGMA2()
    print(f'Solution for n = {limit:5}: {res:10}, Run-Time: {round(time()-start,5)}')

for exp in range(1,16):
    start = time()
    limit = 10**exp
    sol = euler_401(limit)
    res = sol.SIGMA2()
    print(f'Solution for n = 10^{exp:2}: {res:10}, Run-Time: {round(time()-start,5)}')
#  -----------------------------------------------------------------------------
#  solution: 281632621
#  -----------------------------------------------------------------------------
