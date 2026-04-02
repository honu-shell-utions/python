##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##Find the sum of all the primes below two million.
#jim.mccleery, November, 2021
###############################################################################
from sympy import isprime
from time import time
###############################################################################
def lucy_hedgehog_prime_sum(n):
    r = int(n**0.5)
    assert r*r <= n and (r+1)**2 > n
    V = [n//i for i in range(1,r+1)]
    V += list(range(V[-1]-1,0,-1))
    S = {i:i*(i+1)//2-1 for i in V}
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2: break
                S[v] -= p*(S[v//p] - sp)
    return S[n]
###############################################################################
start = time()
total = 0
max = 2*10**6
for i in range(2,max+1):
    if isprime(i):
        total += i
print(f'Solution using isprime     : {total}, Run-Time: {time()-start}')

start = time()
total = lucy_hedgehog_prime_sum(max)
print(f'Solution using LucyHedgehog: {total}, Run-Time: {time()-start}')
###############################################################################
#solution: 142913828922
###############################################################################
