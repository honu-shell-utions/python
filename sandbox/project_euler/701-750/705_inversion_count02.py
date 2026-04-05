#  -----------------------------------------------------------------------------
#  Total Inversion Count of Divided Sequences
#  Problem 705
#  https://projecteuler.net/problem=705
#  -----------------------------------------------------------------------------
from time import time
from sympy import primerange
#  -----------------------------------------------------------------------------
def next_digit(N):
    for p in primerange(3, N):
        digs = str(p)
        for d in digs:
            if d != '0':
                yield int(d)
#  -----------------------------------------------------------------------------
def euler_705(N):
  n = 1
  num_strings = 2  # "1", "2"
  nums_d = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]  # nums_d[d] = the number of
                                           # occurences of d in all strings
  swaps = 0
  for d in next_digit(N):
      n += 1
      ds = DIVS[d]
      num_divs = len(ds)
      swaps = swaps * num_divs % MOD
      for dd in ds:
          swaps += sum(nums_d[j] for j in range(dd+1, 10))   
      nums_d = [dd*num_divs % MOD for dd in nums_d]
      for dd in ds:
          nums_d[dd] += num_strings   
      num_strings = num_strings * num_divs % MOD
  return(swaps % MOD)    
#  -----------------------------------------------------------------------------
MOD = 10**9 + 7
DIVS = [None, [1], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6],
        [1, 7], [1, 2, 4, 8], [1, 3, 9]]

for N in [20,50,10**8]:
    start = time()
    res = euler_705(N)
    print(f'Solution for N = {N:10}: {res:10}, Run-Time: {(time()-start)/60:6.3f} minutes.')
#  -----------------------------------------------------------------------------
#  solution: 480440153
#  -----------------------------------------------------------------------------
