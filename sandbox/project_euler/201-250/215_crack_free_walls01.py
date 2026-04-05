#-------------------------------------------------------------------------------
## Crack-free Walls
## Problem 215
## Consider the problem of building a wall out of 2×1 and 3×1 bricks
## (horizontal×vertical dimensions) such that, for extra strength,
## the gaps between horizontally-adjacent bricks never line up in
## consecutive layers, i.e. never form a "running crack".
## 
## For example, the following 9×3 wall is not acceptable due to the
## running crack shown in red:
## 
## 
## There are eight ways of forming a crack-free 9×3 wall, written W(9,3) = 8.
## 
## Calculate W(32,10).
#-------------------------------------------------------------------------------
from sympy.utilities.iterables import multiset_permutations
from time import time
from itertools import product
#-------------------------------------------------------------------------------
def make_rows():
    xy_pairs = []
    for x in range(columns):
        for y in range(columns//2+1):
            if 3*x + 2*y == columns:
                xy_pairs.append((x,y))
    pr = []
    for x,y in xy_pairs:
        for row in multiset_permutations(x*'3'+ y*'2'):
            pr.append(row)
    return pr
#-------------------------------------------------------------------------------
def make_bit_rows():
    br = []
    for pr in possible_rows:
        temp = ''
        for val in pr:
            if val == '2':
                temp += '01'
            else:
                temp += '001'
        br.append(temp)
    return br
#-------------------------------------------------------------------------------
def ok(row_a,row_b):
    for k in range(len(row_a)-1):
        if row_a[k] == '1' and row_b[k] == '1':
            return False
    return True
#-------------------------------------------------------------------------------
def good_wall(wall):
    for k in range(len(wall)-1):
        if not ok(wall[k],wall[k+1]):
            return False
    return True
#-------------------------------------------------------------------------------
def count_solutions():
    count = 0
    bit_list = []
    for j in range(rows):
        bit_list.append(bit_rows)
    perms = product(*bit_list)
    for wall in perms:
        if good_wall(wall):
            count += 1
    return count
#-------------------------------------------------------------------------------
def W(c,r):
    global columns
    global rows
    global possible_rows
    global bit_rows
    columns = c
    rows = r
    possible_rows = make_rows()
    bit_rows = make_bit_rows()
    return count_solutions()
#-------------------------------------------------------------------------------
start = time()
#-------------------------------------------------------------------------------
print(f'Solution: {W(9,3)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# W(9,3) = 8
# W(12,5) = 96
# W(16,6) = 5218
# W(32,10) = 806844323190414
#-------------------------------------------------------------------------------

