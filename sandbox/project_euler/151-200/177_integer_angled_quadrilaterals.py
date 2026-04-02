#-------------------------------------------------------------------------------
from math import radians, degrees
from mpmath import sin, cot, acot
from time import time
#-------------------------------------------------------------------------------
def get_G(d1,c2,c1,b2,b1,a2,I):
    top = sin(radians(d1))*sin(radians(c1))*sin(radians(b1))
    bot = sin(radians(c2))*sin(radians(b2))*sin(radians(a2))*sin(radians(I))
    G = degrees(acot(top/bot + cot(radians(I))))
    if abs(G - int(G+0.5)) < 10**-9:
        return True, int(G+0.5)
    else:
        return False, -1
#-------------------------------------------------------------------------------
def unique(a1,a2,b1,b2,c1,c2,d1,d2):
    if (a1, a2, b1, b2, c1, c2, d1, d2) in sols: return False
    if (b2, b1, a2, a1, d2, d1, c2, c1) in sols: return False
    if (d2, d1, c2, c1, b2, b1, a2, a1) in sols: return False
    if (d1, d2, a1, a2, b1, b2, c1, c2) in sols: return False
    if (a2, a1, d2, d1, c2, c1, b2, b1) in sols: return False
    if (c2, c1, b2, b1, a2, a1, d2, d1) in sols: return False
    if (c1, c2, d1, d2, a1, a2, b1, b2) in sols: return False
    if (b1, b2, c1, c2, d1, d2, a1, a2) in sols: return False
    return True
#-------------------------------------------------------------------------------
start = time()
def euler_177():
    for I in range(1,91):
        J = 180 - I
        for d1 in range(1,J):
            for c1 in range(1,I//2+1):
                for b1 in range(d1,J):
                    c2 = 180 - I - d1
                    b2 = 180 - c1 - J
                    a2 = 180 - I - b1
                    success, a1 = get_G(d1,c2,c1,b2,b1,a2,I)
                    if success:
                        d2 = 180 - a1 - J
                        if unique(a1,a2,b1,b2,c1,c2,d1,d2):
                            sols.add((a1,a2,b1,b2,c1,c2,d1,d2))
    return len(sols)
#-------------------------------------------------------------------------------
sols = set()
print(f'Solution: {euler_177()},Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#solution: 129325
#-------------------------------------------------------------------------------



