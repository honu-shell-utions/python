#-------------------------------------------------------------------------------
from fractions import Fraction
from time import time
from math import log
#-------------------------------------------------------------------------------
def euler_207():
    good_count = 0
    a = 1
    while True:
        if log(a+1,2) == int(log(a+1,2)):
            good_count += 1
        if Fraction(good_count,a) < Fraction(1,12345):
            print(a*(a+1), Fraction(good_count,a))
            break
        a += 1
#-------------------------------------------------------------------------------
start = time()
print(f'Solution: {euler_207()}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
