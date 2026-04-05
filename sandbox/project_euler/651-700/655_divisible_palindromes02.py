import numpy as np
from time import time

def p655():
    # counts palindromes divisible by "MOD" with k, k-2, k-4,... digits
    def f(k, MOD):
        A = [10**i % MOD for i in range(k)]
        B = [(A[i] + A[-(i+1)]) % MOD for i in range(k//2)]
        if k % 2 == 1:
            B.append(A[k//2])
        V = np.zeros(MOD, dtype=np.uint32)
        V[0] = 1
        for x in B:
            W = np.copy(V)
            for d in range(1, 10):
                i = x*d % MOD
                if i > 0:
                    V[:i] += W[-i:]
                    V[i:] += W[:-i]
                else:
                    V += W
        return V[0] - 1

    def main(k, MOD):
        return f(k, MOD) + f(k-1, MOD)

    print(main(32, 10000019))

start = time()
p655()
print(time()-start)

#  solution: 2000008332
