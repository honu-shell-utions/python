#-------------------------------------------------------------------------------
## Robot Walks
## Problem 208

## A robot moves in a series of one-fifth circular arcs (72°), with
## a free choice of a clockwise or an anticlockwise arc for each step,
## but no turning on the spot.
## 
## One of 70932 possible closed paths of 25 arcs starting northward (see diagram).
## 
## Given that the robot starts facing North, how many journeys
## of 70 arcs in length can it take that return it, after the
## final arc, to its starting position?
## 
## (Any arc may be traversed multiple times.)
#-------------------------------------------------------------------------------
from time import time
from functools import lru_cache
#-------------------------------------------------------------------------------
@lru_cache
def go(a,b,c,d,e,di):
    if a < 0  or  b < 0  or  c < 0  or  d < 0  or  e < 0: return 0
    if a == 0 and b == 0 and c == 0 and d == 0 and e == 0: return 1
    if di == 0:
        return go(a-1,b,c,d,e,1) + go(a,b,c,d,e-1,4)
    if di == 1:
        return go(a,b-1,c,d,e,2) + go(a-1,b,c,d,e,0)
    if di == 2:
        return go(a,b,c-1,d,e,3) + go(a,b-1,c,d,e,1)
    if di == 3:
        return go(a,b,c,d-1,e,4) + go(a,b,c-1,d,e,2)
    if di == 4:
        return go(a,b,c,d,e-1,0) + go(a,b,c,d-1,e,3)
#-------------------------------------------------------------------------------
start = time()
limit = 70
steps = limit // 5
solution = go(steps,steps,steps,steps,steps,0)
print(f'Solution: {solution}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 
#-------------------------------------------------------------------------------
