#  -----------------------------------------------------------------------------
#  Polynomials with at least one integer root
#  Problem 269
#  https://projecteuler.net/problem=269
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def euler_269(N):
    x = {(0,0,0,0,0,0,0,0,0,0): 1}
    for n in range(N):
        y = x
        x = {}
        for a in y:
            for d in range(10):
                b = tuple((None if d else 0) if i == 0
                          else None if a[i] is None
                          else (d - a[i]) // i if (d - a[i]) % i == 0
                          else None
                          for i in range(10))
                if b in x:
                    x[b] += y[a]
                else:
                    x[b] = y[a]

    return (sum(x[a] for a in x.keys() if any(aa == 0 for aa in a)))
#  -----------------------------------------------------------------------------
for exp in range(1,17):
    start = time()
    count = euler_269(exp)
    print(f'Solution for n = 10^{exp:2}: {count:17}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 1311109198529286
#  -----------------------------------------------------------------------------
