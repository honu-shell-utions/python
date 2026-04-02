from functools import lru_cache
import numpy as np
from time import time

@lru_cache
def euler655(LL=32,MOD=10000019):
  res = 0
  Lp = 0
  z = MOD
  while z:
    z //= 10
    Lp += 1
  v = np.empty(MOD, dtype=np.int64)
  w = np.empty(MOD, dtype=np.int64)
  for L in range(Lp,LL+1):
    cLst = []
    for i in range(L//2):
      cLst += [(pow(10,L-1-i,MOD) + pow(10,i,MOD)) % MOD]
    if L % 2:
      cLst += [pow(10,L//2,MOD)]
    v[:] = 0
    c = cLst[0]
    for d in range(1,10):
      v[c*d % MOD] += 1
    for i in range(1,len(cLst)):
      v, w = w, v
      v[:] = 0
      c = cLst[i]
      for d in range(0,10):
        x = c*d % MOD
        for k in range(MOD):
          v[x] += w[k]
          x += 1
          if x >= MOD:
            x -= MOD
    res += v[0]
  return res

start = time()
print(f'Solution: {euler655()}, Run-Time: {time()-start}')
# 2000008332
