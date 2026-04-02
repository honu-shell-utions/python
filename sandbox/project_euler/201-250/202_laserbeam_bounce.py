#-------------------------------------------------------------------------------
## Laserbeam
## Problem 202
## Three mirrors are arranged in the shape of an equilateral triangle,
## with their reflective surfaces pointing inwards.
## 
## There is an infinitesimal gap at each vertex of the triangle through
## which a laser beam may pass.
## 
## Label the vertices A, B and C. There are 2 ways in which a laser beam
## may enter vertex C, bounce off 11 surfaces, then exit through the same
## vertex: one way is shown below; the other is the reverse of that.
## 
## There are 80840 ways in which a laser beam may enter vertex C, bounce
## off 1000001 surfaces, then exit through the same vertex.
## 
## In how many ways can a laser beam enter at vertex C, bounce off 12017639147
## surfaces, then exit through the same vertex?
#-------------------------------------------------------------------------------
import fractions
from math import gcd
from time import time
#-------------------------------------------------------------------------------
# When a laser hits a mirror, instead of thinking of the laser reflecting, 
# you can think of the laser entering a new triangle that is a mirror image 
# of the first one. Repeatedly extending the picture this way results in an
# infinite grid of triangles. This solution works by iterating over the mirrored
# vertices of the row that corresponds to 12017639147 bounces, and counting 
# the vertices that are reachable, and correspond to vertex C. 
#-------------------------------------------------------------------------------
start = time()
surf = 12017639147
#surf = 1000001
row = (surf + 3)//2
offset = 3 - (row % 3)
col = offset
row -= offset

total = 0
while row > col:
   if gcd(row,col) == 1:
      total += 1
   row -= 3
   col += 3

print(f'Solution: {total * 2}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#solution: 1209002624
#-------------------------------------------------------------------------------
