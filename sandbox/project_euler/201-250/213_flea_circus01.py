#-------------------------------------------------------------------------------
## Flea Circus
## Problem 213
## A 30×30 grid of squares contains 900 fleas, initially one flea per square.
## When a bell is rung, each flea jumps to an adjacent square at random
## (usually 4 possibilities, except for fleas on the edge of the grid or at
## the corners).
## 
## What is the expected number of unoccupied squares after 50 rings of the bell?
## Give your answer rounded to six decimal places.
#-------------------------------------------------------------------------------
from time import time
from random import choice
from numpy import zeros, ones
#-------------------------------------------------------------------------------
def get_move(x,y):
    while True:
        dx = choice([-1,1])
        dy = choice([-1,1])
        if 0 <= x+dx < size and 0 <= y+dy < size:
            return dx,dy
#-------------------------------------------------------------------------------
def count_unoccupied():
    empty_cells = 0
    for r in range(size):
        for c in range(size):
            if grid2[r,c] == 0:
                empty_cells += 1
    return empty_cells
#-------------------------------------------------------------------------------
start = time()
size = 30
bell_rings = 50
trials = 10**2
total = 0
for _ in range(trials):
    grid1 = ones((size,size),dtype=int)
    for k in range(bell_rings):
        grid2 = zeros((size,size),dtype=int)
        for r in range(size):
            for c in range(size):
                for _ in range(grid1[r,c]):
                    dx,dy = get_move(r,c)
                    grid2[r+dx,c+dy] += 1
        grid1 = grid2.copy()        
    total += count_unoccupied()

print(f'Solution: {round(total/trials,6)}, Run-Time: {time()-start}')
print(330.721154)
#-------------------------------------------------------------------------------
# solution: 330.721154
#-------------------------------------------------------------------------------
