#  -----------------------------------------------------------------------------
#  Polynomials with at least one integer root
#  Problem 269
#  https://projecteuler.net/problem=269
#  -----------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
from time import time
#  -----------------------------------------------------------------------------
def P(n):
    coef = list(map(int,str(n)))
    return np.poly1d(coef)
#  -----------------------------------------------------------------------------
def is_root(n,x):
    if n % (10-x):
        return False
    value = 0
    for coef in map(int, str(n)):
        value *= x
        value += coef
    return value == 0
#  -----------------------------------------------------------------------------
def graph_poly(n,roots):
    poly = P(n)
    for x in range(-11,1):
        y = np.polyval(poly,x)
        plt.plot(x,y,'.')
    plt.plot([-12,1],[0,0])
    if len(roots) > 1:
        plt.title(f'For n = {n}: roots = {roots}')
    else:
        plt.title(f'For n = {n}: root = {roots}')
    plt.show()
#  -----------------------------------------------------------------------------
graphics = True
for exp in range(1,17):
    start = time()
    count = 0
    for n in range(1,10**exp+1):
        found_root = False
        roots = []
        for x in [0,-1,-2,-3,-4,-5,-6,-7,-8,-9]:
            if is_root(n,x):
                roots.append(x)
                found_root = True
        if graphics and found_root:
            graph_poly(n,roots)
            count += 1
     
    print(f'Solution for n = 10^{exp:2}: {count:17}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 1311109198529286
#  -----------------------------------------------------------------------------
