from sympy import primerange
from time import time

start = time()
k = 10000
s = 0
n = 10**12
for p in primerange(2*10**9,2*10**9+2000):
  ss = 0
  for i in range(1,500*p-n):
    ss += pow(i,k,p)*(n+1+i)
  s = s + (-ss) % p

print(f'Solution: {s}, Run-Time: {time()-start}')
#  solution: 106650212746
