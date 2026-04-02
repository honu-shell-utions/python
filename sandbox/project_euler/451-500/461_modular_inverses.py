#  -----------------------------------------------------------------------------
#  Modular inverses
#  Problem 451
#  Consider the number 15.
#  There are eight positive numbers less than 15 which are coprime to 15:
#  1, 2, 4, 7, 8, 11, 13, 14.
#  The modular inverses of these numbers modulo 15 are:
#  1, 8, 4, 13, 2, 11, 7, 14
#  because
#  1 · 1 mod 15=1
#  2 · 8=16 mod 15=1
#  4 · 4=16 mod 15=1
#  7 · 13=91 mod 15=1
#  11 · 11=121 mod 15=1
#  14 · 14=196 mod 15=1
#  
#  Let I(n) be the largest positive number m smaller than n-1 such that
#  the modular inverse of m modulo n equals m itself.
#
#  I(15)=11.
#  I(100)=51
#  I(7)=1.
#  
#  Find ∑ I(n) for 3≤n≤2×10^7
#  -----------------------------------------------------------------------------
from math import gcd
from time import time
#  -----------------------------------------------------------------------------
def get_coprimes(n):
    cp = []
    for k in range(1,n):
        if gcd(n,k) == 1:
            cp.append(k)
    return cp
#  -----------------------------------------------------------------------------
def mod_inv(n,cp):
    mi = []
    for c in cp:
        mi.append(pow(c,-1,n))
    return mi
#  -----------------------------------------------------------------------------
def I(cp,mi):
    for k in range(len(cp)-2,-1,-1):
        if cp[k] == mi[k]:
            return cp[k]
    return 0
#  -----------------------------------------------------------------------------
def do_demo():
    for n in [7,15,100]:
        cp = get_coprimes(n)
        mi = mod_inv(n,cp)
        print('n =',n,'--->',I(cp,mi))
#  -----------------------------------------------------------------------------
#do_demo()
for exp in range(1,8):
    start = time()
    limit = 2*10**exp
    total = 0
    for n in range(3,limit+1):
        cp = get_coprimes(n)
        mi = mod_inv(n,cp)
        total += I(cp,mi)
    print(f'Solution for n: 2*10^{exp} = {total:10}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 153651073760956
#  -----------------------------------------------------------------------------
