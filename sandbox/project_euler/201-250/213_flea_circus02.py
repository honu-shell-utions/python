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
import numpy as np
from time import time
#-------------------------------------------------------------------------------
start = time()
N = 30
M = N**2
cor_to_index = lambda row,col: col + N*row
A = np.zeros((M,M))

for row in range(N):
    for col in range(N):
        if row>0:
            A[cor_to_index(row,col), cor_to_index(row-1,col)] = 1
        if col>0:
            A[cor_to_index(row,col), cor_to_index(row,col-1)] = 1
        if row<N-1:
            A[cor_to_index(row,col), cor_to_index(row+1,col)] = 1
        if col<N-1:
            A[cor_to_index(row,col), cor_to_index(row,col+1)] = 1

A /= np.sum(A,axis=0)
A50 = np.linalg.matrix_power(A,50)
solution = np.sum(np.prod(1-A50,axis=1))

print(f'Solution: {round(solution,6)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 330.721154
#-------------------------------------------------------------------------------
