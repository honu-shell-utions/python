################################################################################
## Perfect Square Collection 
## Problem 142
## Find the smallest x + y + z with integers x > y > z > 0
## such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.
################################################################################
from math import sqrt
from time import time
################################################################################
def is_square(n):
    root = sqrt(n)
    if (int(root+0.5))**2 == n:
        return True
    else:
        return False
################################################################################
def euler142(limit):
    for i in range(4,limit):
        a = i * i
        j = 3
        for j in range(3,limit):
            c = j * j
            f = a - c
            if f <= 0 or not is_square(f):
                j += 1
                continue
            if j % 2 == 1:
                kstart = 1
            else:
                kstart = 2
            for k in range(kstart,j,2):
                d = k * k
                e = a - d
                b = c - e 
                if b <= 0 or e <= 0 or not is_square(b) or not is_square(e):
                    continue
                x = (d + c) / 2
                y = (e + f) / 2
                z = (c - d) / 2
                return int(x + y + z)           
################################################################################
start = time()
limit = 10**3
print('The solution:',euler142(limit),'Run Time:',time()-start)
################################################################################
#solution: 1006193
################################################################################
