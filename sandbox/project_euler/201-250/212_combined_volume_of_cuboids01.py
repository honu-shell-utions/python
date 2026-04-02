#-------------------------------------------------------------------------------
# 212_combined_volume_of_cuboids.py
#
# Combined Volume of Cuboids
# An axis-aligned cuboid, specified by parameters { (x0,y0,z0), (dx,dy,dz) },
# consists of all points (X,Y,Z) such that x0 ≤ X ≤ x0+dx, y0 ≤ Y ≤ y0+dy
# and z0 ≤ Z ≤ z0+dz.
#
# The volume of the cuboid is the product, dx × dy × dz. The combined volume
# of a collection of cuboids is the volume of their union and will be less
# than the sum of the individual volumes if any cuboids overlap.
#
# Let C1,...,C50000 be a collection of 50000 axis-aligned cuboids such that Cn
# has parameters
# x0 = S6n-5 modulo 10000
# y0 = S6n-4 modulo 10000
# z0 = S6n-3 modulo 10000
# dx = 1 + (S6n-2 modulo 399)
# dy = 1 + (S6n-1 modulo 399)
# dz = 1 + (S6n modulo 399)
#
# where S1,...,S300000 come from the "Lagged Fibonacci Generator":
# For 1 ≤ k ≤ 55, Sk = [100003 - 200003k + 300007k3] (modulo 1000000)
# For 56 ≤ k, Sk = [Sk-24 + Sk-55] (modulo 1000000)
#
# Thus, C1 has parameters {(7,53,183),(94,369,56)}, C2 has parameters
# {(2383,3563,5079),(42,212,344)}, and so on.
#
# The combined volume of the first 100 cuboids, C1,...,C100, is 723581599.
#
# What is the combined volume of all 50000 cuboids, C1,...,C50000?
# ans: 328968937309
#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
def lagged_f_g():
    lst = []
    for k in range(NUM_CUBES*6+1):
        if k <= 55:
            lst.append((100003 - 200003*k + 300007*k**3) % 1000000)
        else:
            lst.append((lst[k-24] + lst[k-55]) % 1000000)
    return lst
#-------------------------------------------------------------------------------
def overlap(c1,c2):
    x1,y1,z1,dx1,dy1,dz1 = c1
    x2,y2,z2,dx2,dy2,dz2 = c2

    if x1 <= x2 and x2 < x1 + dx1:
        x, dx = x2, min(x1 + dx1, x2 + dx2) - x2
    elif x2 <= x1 and x1 < x2 + dx2:
        x, dx = x1, min(x2 + dx2, x1 + dx1) - x1
    else:
        return 0

    if y1 <= y2 and y2 < y1 + dy1:
        y, dy = y2, min(y1 + dy1, y2 + dy2) - y2
    elif y2 <= y1 and y1 < y2 + dy2:
        y, dy = y1, min(y2 + dy2, y1 + dy1) - y1
    else:
        return 0

    if z1 <= z2 and z2 < z1 + dz1:
        z, dz = z2, min(z1 + dz1, z2 + dz2) - z2
    elif z2 <= z1 and z1 < z2 + dz2:
        z, dz = z1, min(z2 + dz2, z1 + dz1) - z1
    else:
        return 0

    return dx*dy*dz
#-------------------------------------------------------------------------------
def get_cube(n):
    x = S[6*n-5] % 10000
    y = S[6*n-4] % 10000
    z = S[6*n-3] % 10000
    dx = 1 + (S[6*n-2] % 399)
    dy = 1 + (S[6*n-1] % 399)
    dz = 1 + (S[6*n] % 399)
    return ((x,y,z,dx,dy,dz))
#-------------------------------------------------------------------------------
start = time()
NUM_CUBES = 100 #50*10**3
S = lagged_f_g()
volume = 0

for j in range(1,NUM_CUBES+1):
    x,y,z,dx,dy,dz = get_cube(j)
    volume += dx*dy*dz
   
for j in range(1,NUM_CUBES+1):
    for k in range(j+1,NUM_CUBES+1):
        c1 = get_cube(j)
        c2 = get_cube(k)
        volume -= overlap(c1,c2)
   
print(f'Solution: {volume}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 328968937309
#-------------------------------------------------------------------------------    
