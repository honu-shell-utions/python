#  --------------------------------------------------------------------------------
#  https://projecteuler.net/problem=60
#  --------------------------------------------------------------------------------
from time import time
from sympy import primerange, isprime
#  --------------------------------------------------------------------------------
def ok(a,b):
    first = str(a)
    second = str(b)
    if isprime(int(first+second)) and isprime(int(second+first)):
        return True
    else:
        return False
#  --------------------------------------------------------------------------------
def euler_060():
    primes = list(primerange(13,10**4))
    for a in primes:
        for b in primes:
            if b < a:
                continue
            if ok(a, b):
                for c in primes:
                    if c < b:
                        continue
                    if ok(a, c) and ok(b, c):
                        for d in primes:
                            if d < c:
                                continue
                            if ok(a, d) and ok(b, d) and ok(c, d):
                                for e in primes:
                                    if e < d:
                                        continue
                                    if ok(a, e) and ok(b, e) and ok(c, e) and ok(d, e):
                                        return a,b,c,d,e
#  --------------------------------------------------------------------------------
start = time()
solution = euler_060()
print(f'Solution: {solution}, {sum(solution)}, Run-Time: {time()-start}')
#  --------------------------------------------------------------------------------
#Solution: 26033
#  --------------------------------------------------------------------------------
