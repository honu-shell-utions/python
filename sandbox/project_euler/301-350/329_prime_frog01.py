# 329_prime_frog.py
#
# Susan has a prime frog.
#
# Her frog is jumping around over 500 squares numbered 1 to 500. He can only
# jump one square to the left or to the right, with equal probability, and he
# cannot jump outside the range [1, 500].
# (if it lands at either end, it automatically jumps to the only available
# square on the next move.)
# 
# When he is on a square with a prime number on it, he croaks 'P' (PRIME) with
# probability 2/3 or 'N' (NOT PRIME) with probability 1/3 just before jumping
# to the next square.
#
# When he is on a square with a number on it that is not a prime he croaks 'P'
# with probability 1/3 or 'N' with probability 2/3 just before jumping to the
# next square.
# 
# Given that the frog's starting position is random with the same probability
# for every square, and given that she listens to his first 15 croaks, what is
# the probability that she hears the sequence PPPPNNPPPNPPNPN?
# 
# Give your answer as a fraction p/q in reduced form.
# -----------------------------------------------------------------------------
# ans == 199740353/29386561536000
# -----------------------------------------------------------------------------
from fractions import Fraction
from sympy import isprime
from time import time
# -----------------------------------------------------------------------------
def calc_prob(i, string):
    if (i, string) in d:
        return d[(i, string)]
    if (i == 1):
        prob = d[(i, string[0])] * calc_prob(i + 1, string[1:])
    elif (i == limit):
        prob = d[(i, string[0])] * calc_prob(i - 1, string[1:])
    else:
        prob = d[(i, string[0])] * (calc_prob(i + 1, string[1:]) * Fraction(1, 2) + calc_prob(i - 1, string[1:]) * Fraction(1, 2))
    d[(i, string)] = prob
    return prob
# -----------------------------------------------------------------------------
start = time()
limit = 500
d = {}

for i in range(1, limit+1):
    if isprime(i):
        d[(i, 'P')] = Fraction(2, 3)
        d[(i, 'N')] = Fraction(1, 3)
    else:
        d[(i, 'P')] = Fraction(1, 3)
        d[(i, 'N')] = Fraction(2, 3)

for i in range(1, limit+1):
  calc_prob(i, 'PPPPNNPPPNPPNPN')

prob = Fraction(0,1)
for k,v in d.items():
    if k[1] == 'PPPPNNPPPNPPNPN':
        prob += v

print(f'Solution: {prob / limit}, Run-Time: {time()-start}')
# -----------------------------------------------------------------------------
