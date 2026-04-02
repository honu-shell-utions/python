#  -----------------------------------------------------------------------------
#  Asymmetric Diophantine Equation
#  Problem 764
#  https://projecteuler.net/problem=764
#  -----------------------------------------------------------------------------
from math import gcd
from time import time
#  -----------------------------------------------------------------------------
class euler_764:
    def __init__(self,limit,mod,show = False):
        self.limit = limit
        self.mod = mod
        self.show = show
        self.solution = self.compute_odds() + self.compute_all()
    #  ------------------------------------------------------------------------
    def get_solution(self):
        return self.solution % self.mod
    #  ------------------------------------------------------------------------
    def compute_odds(self):
        total = 0
        for a in range(1,10**6, 2):
            for b in range(1, a, 2):
                if a**4 + b**4 > 2*self.limit:
                    break
                if gcd(a, b) > 1:
                    continue
                if self.show:
                    print((a**4-b**4)//8, a*b, (a**4+b**4)//2)
                total += (a**4-b**4)//8 + a*b + (a**4+b**4)//2
        return total
    #  ------------------------------------------------------------------------
    def compute_all(self):
        total = 0
        for a in range(1,10**6, 2):
            for b in range(1,10**6):
                if 4*a**4 + 16*b**4 > self.limit:
                    break
                if gcd(a, b) > 1:
                    continue
                    if self.show:
                        print(abs(a**4-4*b**4), 4*a*b, 4*a**4 + 16*b**4)
                total += abs(a**4-4*b**4) + 4*a*b + 4*a**4 + 16*b**4
        return total
    #  ------------------------------------------------------------------------
#  -----------------------------------------------------------------------------
MOD = 10**9
for exp in range(4,17):
    start = time()
    N = 10**exp
    instance = euler_764(N,MOD,False)
    ans = instance.get_solution()
    print(f'Solution for n = 10^{exp:2}: {ans:10}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 255228881
#  -----------------------------------------------------------------------------

