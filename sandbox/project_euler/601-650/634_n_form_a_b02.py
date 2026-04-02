#  -----------------------------------------------------------------------------
#  Numbers of the form a^2*b^3
#  Problem 634
#  https://projecteuler.net/problem=634
#  -----------------------------------------------------------------------------
from math import sqrt
from sympy import isprime
from time import time
#  -----------------------------------------------------------------------------
def euler_634(N):
    b_max = int((N/4)**(1/3))
    squares = set([x**2 for x in range(2,int(sqrt(b_max)))])
    blacklist = set()
    r = 0
    for b in range(2,b_max+1):
        if not b in blacklist:
            if b in squares:
                k = int(sqrt(b))
                x = 2 * b
                while x < b_max+1:
                    blacklist.add(x)
                    x += b
                l_up = int((N)**(1/6)/k)
                temp = set()
                for l in range(k+1,l_up+1):
                    if isprime(l):
                        v_max = int(sqrt(N)/k**3/l**3)
                        for v in range(1,v_max+1):
                            temp.add(v*l**3)
                r -= len(temp)
            a_max = int(sqrt(N/b**3))
            r += a_max - 1
    return r
#  -----------------------------------------------------------------------------
for txt,limit in [('10^2',10**2),('2*10^4',2*10**4),('3*10^6',3*10**6),('9*10^18',9*10**18)]:
    start = time()
    powerful = euler_634(limit)
    print(f'Solution for n = {txt:>8} -----> {powerful:11}, Run-Time: {round(time()-start,5)}')
#  -----------------------------------------------------------------------------
#  solution: 4019680944
#  -----------------------------------------------------------------------------
