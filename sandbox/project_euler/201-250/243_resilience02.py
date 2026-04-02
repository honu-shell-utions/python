# p243_resilience.py
#
# Resilience
# A positive fraction whose numerator is less than its denominator is called
# a proper fraction.
#
# For any denominator, d, there will be d-1 proper fractions; for example,
# with d = 12:
# 1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12
#
# We shall call a fraction that cannot be cancelled down a resilient fraction.
# Furthermore, we shall define the resilience of a denominator, R(d), to be
# the ratio of its proper fractions that are resilient;
# for example, R(12) = 4/11
#
# In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10
#
# Find the smallest denominator d, having a resilience R(d) < 15499/94744
# ----------------------------------------------------------------------------
from sympy.ntheory.factor_ import totient
from time import time
from sympy import primerange
# ----------------------------------------------------------------------------
def resilient(numer, denom, maxPrime):
    primes = list(primerange(2,maxPrime))
    target = numer/denom
    i = 1
    d = 2

    while (totient(d) / (d - 1)) >= target:
        d *= primes[i]
        i += 1

    d //= primes[i - 1]
    i = 1

    while i:
        i += 1
        if totient(d*i)/(d*i - 1) < target:
            return d*i
# ----------------------------------------------------------------------------
start = time()
print(f'Solution: {resilient(15499, 94744, 30)}, Run-Time: {time()-start}')
# ----------------------------------------------------------------------------
# Solution: 892371480
# ----------------------------------------------------------------------------
