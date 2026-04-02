################################################################################
##Prime power triples
##Problem 87
##
##The smallest number expressible as the sum of a prime square, prime cube,
##and prime fourth power is 28. In fact, there are exactly four numbers below
##fifty that can be expressed in such a way:
##
##28 = 2^2 + 2^3 + 2^4
##33 = 3^2 + 2^3 + 2^4
##49 = 5^2 + 2^3 + 2^4
##47 = 2^2 + 3^3 + 2^4
##
##How many numbers below fifty million can be expressed as the sum of
##a prime square, prime cube, and prime fourth power?
################################################################################
from sympy import primerange
import numpy as np
import time
import math

start = time.time()
below = 50_000_000
# below = 50
st = set()

primes = np.array(list(primerange(2, int(math.sqrt(below)))))
squares = np.array([p**2 for p in primes if p**2 + 2**3 + 2**4 < below], dtype=int)
cubes = np.array([p**3 for p in primes if p**3 + 2**2 + 2**4 < below], dtype=int)
quartic = np.array([p**4 for p in primes if p**4 + 2**2 +2**3 < below], dtype=int)


for q in quartic:
    for c in cubes:
        for s in squares:
            if q + c + s < below:
                st.add(q + c + s)

print('ans:', len(st))
print(time.time()-start)
################################################################################
#solution: 1097343
################################################################################
