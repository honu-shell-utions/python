# ------------------------------------------------------------------------------
# Prime triplets
# Problem 196
# Build a triangle from all positive integers in the following way:
# 
#  1
#  2  3
#  4  5  6
#  7  8  9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35 36
# 37 38 39 40 41 42 43 44 45
# 46 47 48 49 50 51 52 53 54 55
# 56 57 58 59 60 61 62 63 64 65 66
# . . .
# 
# Each positive integer has up to eight neighbours in the triangle.
# 
# A set of three primes is called a prime triplet if one of the three
# primes has the other two as neighbours in the triangle.
# 
# For example, in the second row, the prime numbers 2 and 3 are elements
# of some prime triplet.
# 
# If row 8 is considered, it contains two primes which are elements of
# some prime triplet, i.e. 29 and 31.
# 
# If row 9 is considered, it contains only one prime which is an element
# of some prime triplet: 37.
# 
# Define S(n) as the sum of the primes in row n which are elements of
# any prime triplet.
# 
# Then S(8) = 60 and S(9) = 37.
# 
# You are given that S(10000) = 950007619.
# 
# Find  S(5678027) + S(7208785).
# ------------------------------------------------------------------------------
from numpy import zeros
from sympy import isprime
from time import time
from itertools import combinations
from math import sqrt
# ------------------------------------------------------------------------------
def load_grid(grid,first_value,width_first_row):
    k = first_value
    for r in range(5):
        for c in range(r+width_first_row):
            if isprime(k):
                grid[r,c+2] = k
            k += 1
# ------------------------------------------------------------------------------
def contiguous(p1,p2):
    if p1 in inner_grid and p2 in inner_grid:
        return True
    if not p1 in inner_grid and not p2 in inner_grid:
        return False
    r1,c1 = p1
    r2,c2 = p2
    if sqrt((r1-r2)**2 + (c1-c2)**2) > sq_root_2:
        return False
    return True
# ------------------------------------------------------------------------------
def is_triple(grid,row,col):
    for p1,p2 in offset_list:
        r1,c1 = p1
        r2,c2 = p2
        if grid[row+r1][col+c1] and grid[row+r2][col+c2]:
            if contiguous(p1,p2):
                return grid[row][col]
    return 0  
# ------------------------------------------------------------------------------
def S(row):
    end_last_row = (row+2)*(row+3)//2
    end_next_to_last_row = (row+1)*(row+2)//2
    width = end_last_row - end_next_to_last_row + 4
    grid = zeros((5,width),dtype=int)
    first_value = (row-3)*(row-2)//2 + 1
    width_first_row = width - 8   
    load_grid(grid,first_value,width_first_row)
    total = 0
    for c in range(2,width-2):
        if grid[2,c]:
            total += is_triple(grid,2,c)
    return total
# ------------------------------------------------------------------------------
start = time()
sq_root_2 = sqrt(2)
#build combinations of offsets, omitting (0,0)
offsets = []
for off_row in range(-2,3):
    for off_col in range(-2,3):
        if not(off_row == 0 and off_col == 0):
            offsets.append((off_row,off_col))        
offset_list = list(combinations(offsets,2))

#build list of 'inner grid', omitting (0,0)
inner_grid = []
for r in range(-1,2):
    for c in range(-1,2):
        if not(r == 0 and c == 0):
            inner_grid.append((r,c))
# ------------------------------------------------------------------------------
solution = S(5678027) + S(7208785)
# ------------------------------------------------------------------------------
print(f'Solution: {solution}, Run-Time: {time()-start}')
# ------------------------------------------------------------------------------
# solution: 322303240771079935
# ------------------------------------------------------------------------------
