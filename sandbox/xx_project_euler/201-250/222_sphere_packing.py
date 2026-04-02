#-------------------------------------------------------------------------------
## Sphere Packing
## Problem 222
## What is the length of the shortest pipe, of internal
## radius 50mm, that can fully contain 21 balls of radii
## 30mm, 31mm, ..., 50mm?
## 
## Give your answer in micrometres (10^(-6) m) rounded
## to the nearest integer.
#-------------------------------------------------------------------------------
from math import sqrt
from time import time
#-------------------------------------------------------------------------------
def get_sphere_list():
    #spheres = [50,48,46,44,42,40,38,36,34,32,30,31,33,35,37,39,41,43,45,47,49]
    sphere_list = []
    for r in range(50,29,-2):
        sphere_list.append(r)
    for r in range(31,50,2):
        sphere_list.append(r)
    return sphere_list
#-------------------------------------------------------------------------------
def vert_dist(r1, r2):
    'The vertical distance between centres of spheres radius r1, r2.'
    return sqrt((r1+r2)**2 - (100-r1-r2)**2)
#-------------------------------------------------------------------------------
def get_pipe_length(order):
    'Calculate total distance from order.'
    total = order[0] + order[-1]
    for a in range(len(order) - 1):
        total += vert_dist(order[a], order[a+1])
    return total
#-------------------------------------------------------------------------------
start = time()
spheres = get_sphere_list()
length = get_pipe_length(spheres)

print(f'Solution: {round(length*10**3)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 1590933
#-------------------------------------------------------------------------------
