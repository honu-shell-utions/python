import numpy as np
from sympy import mod_inverse, primerange
import time

def problema_650(n, mod):
    start = time.time()
    primes = primerange(1, n +1)
    divs = np.ones(n + 1, dtype=np.int64)
    for p in primes:
        suma = 0
        for x in range(p, n + 1):
            a = 0
            m = x
            while m:
                m //= p
                a += m
            e = (x - 1) * a - 2 * suma
            divs[x] *= (pow(p, e + 1, mod) - 1) * mod_inverse(p-1, mod) % mod
            divs[x] %= mod
            suma += a
    return (np.sum(divs) - 1) % mod, time.time() - start


if __name__ == "__main__":
    print(problema_650(n=20000, mod=1000000007))
