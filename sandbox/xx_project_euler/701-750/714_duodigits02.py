#  -----------------------------------------------------------------------------
#  Duodigits
#  Problem 714
#  https://projecteuler.net/problem=714 
#  -----------------------------------------------------------------------------
from itertools import product
from time import time
#  -----------------------------------------------------------------------------
def euler_714(N):
    candidates = set(range(1,N+1))
    minimal = {n:0 for n in range(1,N+1)}
    length = 1
    while len(candidates) > 0:
      for i in range(1,10):
        for j in range(i):
          for n in product(str(10*i+j), repeat=length):
            m = int(''.join(tuple(n)))
            if m == 0:
              continue
            for c in candidates:
              if (minimal[c]==0 or m<minimal[c]) and m%c==0:
                minimal[c] = m

      candidates = {c for c in candidates if minimal[c]==0}
      length += 1
    return sum(minimal[n] for n in range(1,N+1))
#  -----------------------------------------------------------------------------
for N in [110,150,500,50*10**3]:
    start = time()
    ans = euler_714(N)
    print(f'Solution for N = {N:6}: {ans:.12e}, Run-Time:{time()-start:.4f}')
#  -----------------------------------------------------------------------------
#  solution: 2.452767775565e20
#  -----------------------------------------------------------------------------

