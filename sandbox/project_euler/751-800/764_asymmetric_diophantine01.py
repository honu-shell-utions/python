#  -----------------------------------------------------------------------------
#  Asymmetric Diophantine Equation
#  Problem 764
#  https://projecteuler.net/problem=764
#  -----------------------------------------------------------------------------
from time import time
from math import isqrt, sqrt, gcd
import numpy as np
#  -----------------------------------------------------------------------------
class euler_764:
    def __init__(self,limit,mod,show=False):
        self.limit = limit
        self.mod = mod
        self.show = show
        self.solution = self.compute_solution()
    #  ------------------------------------------------------------------------
    def get_solution(self):
        return self.solution
    #  ------------------------------------------------------------------------
    def compute_solution(self):
        total = 0
        for A,B,C in self.gen_all_pyth_trips():
            yn,x,y,z = self.ok(A,B,C)
            if yn:
                total += x + y + z
                if self.show:
                    print((x,y,z))
        return total % self.mod
    #  ------------------------------------------------------------------------
    def gen_prim_pyth_trips(self):
        A = [[1,2,2],[-2,-1,-2],[2,2,3]]
        B = [[1,2,2],[2,1,2],[2,2,3]]
        C = [[-1,-2,-2],[2,1,2],[2,2,3]]
        ABC = np.array([A, B, C])
        m = np.array([3, 4, 5])
        while m.size:
            m = m.reshape(-1, 3)
            if self.limit:
                m = m[m[:, 2] <= self.limit]
            yield from m
            m = np.dot(m, ABC)
    #  ------------------------------------------------------------------------
    def gen_all_pyth_trips(self):
        for prim in self.gen_prim_pyth_trips():
            i = prim
            for _ in range(self.limit//prim[2]):
                yield i
                i = i + prim
    #  ------------------------------------------------------------------------
    def ok(self,A,B,C):
        z = C
        if A % 4 == 0:
            x = A // 4
            if sqrt(B) == isqrt(B):
                y = isqrt(B)
            else:
                y = 0
        elif B % 4 == 0:
            x = B // 4
            if sqrt(A) == isqrt(A):
                y = isqrt(A)
            else:
                y = 0
        else:
            return False, 0,0,0
        
        if 16*x**2 + y**4 == z**2 and gcd(x,y,z) == 1:
            if self.show:
                print((x,y,z))
            return True,x,y,z
        else:
            return False,0,0,0
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
