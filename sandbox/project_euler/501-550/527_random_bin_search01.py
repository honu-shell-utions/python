#  -----------------------------------------------------------------------------
#  Randomized Binary Search
#  Problem 527
#  https://projecteuler.net/problem=527
#  -----------------------------------------------------------------------------
from random import randint, choice
from math import log
from fractions import Fraction
from math import log
#  -----------------------------------------------------------------------------
def H(n):
    return log(n) + GAMMA + 1/(2*n)

def R(n):
    return 2*H(n)*(1+1/n)-3

def L(n):
    return int(log(n,2))

def B(n):
    return 1+((n+1)*L(n)-2*(2**L(n)-1))/n 

#  -----------------------------------------------------------------------------
GAMMA = 0.57721566490153286060651209

for limit in [6,10**6,10**8,10**10]:
    ev_bin = B(limit)
    print(f'The EV for a standard binary search with array length\
     = {limit:,} is {round(ev_bin,8)}.')

    ev_rand = R(limit)
    print(f'The EV for a random binary search with array length\
       = {limit:,} is {round(ev_rand,8)}.')

    print(f'The difference is: {round(ev_rand-ev_bin,8)}.\n')
#  -----------------------------------------------------------------------------
#  solution: 11.92412011
#  -----------------------------------------------------------------------------
