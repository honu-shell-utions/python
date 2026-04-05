#  -----------------------------------------------------------------------------
#  π sequences
#  Problem 609
#  https://projecteuler.net/problem=609
#  -----------------------------------------------------------------------------
import time
from sympy import primerange
#  -----------------------------------------------------------------------------
class Problem():
    def __init__(self):
        self.res = 1
        self.n = 10**8
        self.mod = 1000000007
        self.primes_list = None
        self.primes_set = None
        self.bound = 0
        self.p_list = None
        self.pi_memo = {1: 0}
    #  ------------------------------------------------------------------------
    def init_primes_and_p_lists_and_bound(self):
        self.primes_list = list(primerange(2,self.n))
        self.primes_set = set(self.primes_list)
        self.bound = len(self.primes_list)
        self.p_list = [0 for _ in range(self.bound)]
    #  ------------------------------------------------------------------------
    def pi(self, x):
        if x in self.pi_memo:
            return self.pi_memo[x]
        right = self.bound
        left = 0
        median = (left+right)//2
        while (left != right) and (right != (left+1)):
            if self.primes_list[median] > x:
                right = median
            else:
                left = median
            median = (left+right)//2
        self.pi_memo[x] = right
        return right
    #  ------------------------------------------------------------------------
    def get_res(self):
        u_1 = 0
        for u_0 in range(2, self.n+1):
            c = 0
            if u_0 not in self.primes_set:
                c += 1
            else:
                u_1 += 1
            u_n = u_1
            while u_n >= 1:
                if u_n not in self.primes_set:
                    c += 1
                self.p_list[c] += 1
                u_n = self.pi(u_n)
        for k in self.p_list:
            if k > 0:
                k = k % self.mod
                self.res = (self.res * k) % self.mod
    #  ------------------------------------------------------------------------
    def solve(self):
        self.init_primes_and_p_lists_and_bound()
        self.get_res()
        print(self.res)
#  -----------------------------------------------------------------------------
def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('Run-Time:', time.perf_counter() - start, 'sec')
#  -----------------------------------------------------------------------------
main()
#  solution: 172023848
#  -----------------------------------------------------------------------------
