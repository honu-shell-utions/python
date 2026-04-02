#  -----------------------------------------------------------------------------
#  Inverse Digit Sum
#  Problem 684
#  https://projecteuler.net/problem=684
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
class euler_684:
    def __init__(self):
        self.mod = 10**9+7
    #  ------------------------------------------------------------------------
    def S(self,k):
        q = k // 9
        r = k % 9
        sum1 = (6*(pow(10, q, self.mod) - 1)) - (9*q % self.mod)
        sum2 = sum([i*pow(10, q, self.mod) - 1 for i in range(2, r+2)])
        return (sum1+sum2) % self.mod
    #  ------------------------------------------------------------------------
    def get_solution(self,n):
        total = 0
        fg = self.fibonacci_gen(0,1)
        temp = next(fg)
        temp = next(fg)
        for _ in range(2, n+1):
            total += self.S(next(fg))
        return total % self.mod
    #  ------------------------------------------------------------------------
    def fibonacci_gen(self,T1=1,T2=1):
        yield T1
        yield T2
        while True:
            yield T1+T2
            T1,T2 = T2,T1+T2
    #  ------------------------------------------------------------------------
#  -----------------------------------------------------------------------------
instance = euler_684()
for limit in range(10,101):
    start = time()
    sol = instance.get_solution(limit)
    if sol == 922058210:
        print('-'*70)
    print(f'Solution for n = {limit:>3}: {sol:10}, Run-Time: {time()-start}')
    if sol == 922058210:
        print('-'*70)
#  -----------------------------------------------------------------------------
#  solution: 922058210
#  -----------------------------------------------------------------------------
