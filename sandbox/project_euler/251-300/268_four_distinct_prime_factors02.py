#  -----------------------------------------------------------------------------
from sympy import binomial, primerange
from time import time
#  -----------------------------------------------------------------------------
def make_F(N):
    # compute possible divisors
    D = [(1, 0)]
    for p in P:
        D += [(p * d, v + 1) for d, v in D if p * d < N]

    # use a dictionary to sum up the divisible numbers
    F = dict()
    for d, v in D:
        if v > 3:
            t = (N - 1) // d
            if v in F:
                F[v] += t
            else:
                F[v] = t
    return F
#  -----------------------------------------------------------------------------
P = list(primerange(2,100))
for exp in range(3,17):
    start = time()
    total = 0
    s = 1
    F = make_F(10**exp)
    for f in F:
        total += s * binomial(f-1, f-4) * F[f]
        s *= -1
    print(f'Solution for n = 10^{exp:<2}: {int(total):16}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
# 10^3:  23
# 10^4:  811
# 10^5:  9280
# 10^6:  77579
# 10^7:  768778
# 10^8:  7881475
# 10^16: 785478606870985 (solution)
#  -----------------------------------------------------------------------------
