################################################################################
## Perfect Square Collection 
## Problem 142
## Find the smallest x + y + z with integers x > y > z > 0
## such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.
################################################################################
from math import sqrt
################################################################################
def is_square(n):
    root = sqrt(n)
    if (int(root+0.5))**2 == n:
        return True
    else:
        return False
################################################################################
limit = 10**6
for z in range(1,limit):
    for y in range(z+1,limit):
        if not is_square(y + z) or not is_square(y - z):
            continue
        for x in range(y+1,limit):
            if not is_square(x + y) or\
               not is_square(x - y) or\
               not is_square(x + z) or\
               not is_square(x - z):
                continue
                print(x+y+z,x,y,z)
################################################################################
#solution: I think this program is logically correct but would run until the
#          heat death of the universe
################################################################################
