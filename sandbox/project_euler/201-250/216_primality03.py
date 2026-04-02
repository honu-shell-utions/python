#-------------------------------------------------------------------------------
## Investigating the primality of numbers of the form 2n^2-1
## Problem 216
## Consider numbers t(n) of the form t(n) = 2n^2-1 with n > 1.
## The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
## It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
## For n ≤ 10000 there are 2202 numbers t(n) that are prime.
## 
## How many numbers t(n) are prime for n ≤ 50,000,000 ?
#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
start = time()
N = 5*10**7
cnt = 0
gr=[2*n*n-1 for n in range(N+1)]
for i in range(2,N+1):
    p = gr[i]
    if p == 2*i*i-1:
        cnt += 1
    if p > 1:
        for j in range(i+p,N+1,p):
            while gr[j] % p == 0:
                gr[j] //= p
        for j in range(i+(-i % p -i) % p,N+1,p):
            while gr[j] % p == 0:
                gr[j] //= p
print(f'Solution: {cnt}, Run-Time: {time()-start:.3f}')
#-------------------------------------------------------------------------------
# solution: 5437849
#-------------------------------------------------------------------------------
