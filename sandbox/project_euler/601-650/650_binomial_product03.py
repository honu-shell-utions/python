from sympy import factorint, mod_inverse, primerange
from time import time

start = time()
MOD = 10**9+7
N = 2*10**4

S = 0
V, W = {}, {}

m = {p:mod_inverse(p-1,MOD) for p in primerange(1,N)}

for k in range(1, N+1):
    f = factorint(k)
    for p in f:
        if p not in V: V[p] = 0
        if p not in W: W[p] = 0
        V[p] += f[p]*k
        W[p] += f[p]
    for p in W: V[p] -= W[p]
    s = 1
    for p in V: s = (s*(pow(p,V[p]+1,MOD)-1)*m[p])% MOD
    S = (S+s) % MOD
        
print(f'Solution: {S}, Run-Time: {time()-start}')
# 538319652
