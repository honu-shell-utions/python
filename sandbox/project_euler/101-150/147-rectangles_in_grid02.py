################################################################################
## Rectangles in cross-hatched grids
## Problem 147
## In a 3x2 cross-hatched grid, a total of 37 different
## rectangles could be situated within that grid as indicated
## in the sketch.
##
## There are 5 grids smaller than 3x2, vertical and
## horizontal dimensions being important, i.e.
## 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is
## cross-hatched, the following number of different
## rectangles could be situated within those smaller grids:
##
## 1x1	1
## 2x1	4
## 3x1	8
## 1x2	4
## 2x2	18
##
## Adding those to the 37 of the 3x2 grid, a total of 72
## different rectangles could be situated within 3x2 and smaller grids.
##
## How many different rectangles could be situated within
## 47x43 and smaller grids?
################################################################################
from time import time
################################################################################
start = time()

def upright(m, n):
    return (m+1) * m // 2 * (n+1) * n //2

def tilted(m, n):
    if m < n:
        m, n = n, m
    x = n * ((2*m - n) * (4*n**2 - 1) - 3) // 6
    return x

WIDTH = 47
HEIGHT = 43
lst = []
for width in range(1, WIDTH+1):
    for height in range(1, HEIGHT+1):
        lst.append(upright(width, height) + tilted(width, height))

ans = sum(lst)
print(f'number of rectangles within {WIDTH}x{HEIGHT} grid: {ans} runtime: {time()-start}')
################################################################################
#solution: 846910284
################################################################################
