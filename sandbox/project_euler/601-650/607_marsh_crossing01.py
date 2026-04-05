#  -----------------------------------------------------------------------------
#  Marsh Crossing
#  Problem 607
#  https://projecteuler.net/problem=607
#  -----------------------------------------------------------------------------
from time import time
from random import uniform
from math import sqrt
#  -----------------------------------------------------------------------------
def time_between_pts(x1,y1,x2,y2,rate):
    d = sqrt( (x2-x1)**2 + (y2-y1)**2 )
    return d/rate
#  -----------------------------------------------------------------------------
start = time()
exp = 8
N = 10**exp
BETWEEN_A_AND_B = 100
HALF_WAY = BETWEEN_A_AND_B // 2
x0,y0 = -HALF_WAY,0
x7,y7 = HALF_WAY,0
FSQRT = 5*sqrt(2)
MIN_TIME = 10**7
for exp in range(2,10):
    N = 10**exp
    for _ in range(N):
        x1 = uniform(-HALF_WAY,HALF_WAY)
        y1 = x1 + 5*FSQRT
        x2 = uniform(x1,HALF_WAY)
        y2 = x2 + 3*FSQRT
        x3 = uniform(x2,HALF_WAY)
        y3 = x3 + FSQRT  
        x4 = uniform(x3,HALF_WAY)
        y4 = x4 - FSQRT
        x5 = uniform(x4,HALF_WAY)
        y5 = x5 - 3*FSQRT
        x6 = uniform(x5,HALF_WAY)
        y6 = x6 - 5*FSQRT
        
        t1 = time_between_pts(x0,y0,x1,y1,10)
        t2 = time_between_pts(x1,y1,x2,y2,9)
        t3 = time_between_pts(x2,y2,x3,y3,8)
        t4 = time_between_pts(x3,y3,x4,y4,7)
        t5 = time_between_pts(x4,y4,x5,y5,6)
        t6 = time_between_pts(x5,y5,x6,y6,5)
        t7 = time_between_pts(x6,y6,x7,y7,10)
        
        t = t1+t2+t3+t4+t5+t6+t7
        if t < MIN_TIME:
            MIN_TIME = t
            x_values = [x0,x1,x2,x3,x4,x5,x6,x7]
            y_values = [y0,y1,y2,y3,y4,y5,y6,y7]
            
    print(f'Minimum Time for 10^{exp} trials: {MIN_TIME:7.4f} days, Run-Time: {time()-start:8.3f}')
#  -----------------------------------------------------------------------------
#  solution: 13.1265108586
#  -----------------------------------------------------------------------------
