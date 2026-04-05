#  -----------------------------------------------------------------------------
#  47-smooth triangular numbers
#  Problem 581
#  https://projecteuler.net/problem=581
#  A number is p-smooth if it has no prime factors larger than p.
#  Let T be the sequence of triangular numbers, ie T(n)=n(n+1)/2.
#  Find the sum of all indices n such that T(n) is 47-smooth.
#  https://www.ivl-projecteuler.com/overview-of-problems/30-difficulty/problem-581
#  -----------------------------------------------------------------------------
from sympy import primefactors
from time import time
#  -----------------------------------------------------------------------------
def is_p_smooth(n,p):
    if n == 1:
        return True
    pf = primefactors(n)
    return p >= max(pf)
#  -----------------------------------------------------------------------------
def get_tri(n):
    return n*(n+1)//2
#  -----------------------------------------------------------------------------
def euler_581(p,lim):
    index_sum = 0
    for index in range(1,lim):
        if is_p_smooth(get_tri(index),p):
            #print(t,primefactors(t))
            index_sum += index
    return index_sum
#  -----------------------------------------------------------------------------
for p,lim in [(2,9),(3,81),(5,9801),(7,336141),(11,1611308700),\
              (13,63927525376),(17,20628591204481),(19,31887350832897)]:
    start = time()
    print(f'Solution for p = {p:3}, {euler_581(p,lim):20}, Run-Time: {time()-start:12.2f}')
#  -----------------------------------------------------------------------------
#  -----------------------------------------------------------------------------
#  solution: 2227616372734
#  -----------------------------------------------------------------------------
