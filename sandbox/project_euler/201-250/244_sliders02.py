#-------------------------------------------------------------------------------
# 244_sliders.py
#
# You probably know the game Fifteen Puzzle. Here, instead of numbered tiles,
# we have seven red tiles and eight blue tiles.
#
# A move is denoted by the uppercase initial of the direction
# (Left, Right, Up, Down) in which the tile is slid, e.g. starting from
# configuration (S), by the sequence LULUR we reach the configuration (E):
# (see pdf pic)
#
# For each path, its checksum is calculated by (pseudocode):
# checksum = 0
# checksum = (checksum × 243 + m1) mod 100 000 007
# checksum = (checksum × 243 + m2) mod 100 000 007
#    …
# checksum = (checksum × 243 + mn) mod 100 000 007
# where mk is the ASCII value of the kth letter in the move sequence and the 
# ASCII values for the moves are:
#
# L	76
# R	82
# U	85
# D	68
#
# For the sequence LULUR given above, the checksum would be 19761398.
#
# Now, starting from configuration (S), find all shortest ways to reach 
# configuration (T).  (see pdf pic)
#
# What is the sum of all checksums for the paths having the minimal length?
# {ans == 96356848}
#-------------------------------------------------------------------------------
from random import choice
from time import time
#-------------------------------------------------------------------------------
def make_move():
    global blank_row
    global blank_col

    while True:
        move = choice(['L','R','U','D'])
        if move == 'L' and blank_col != 3:
            break
        if move == 'R' and blank_col != 0:
            break
        if move == 'U' and blank_row != 3:
            break
        if move == 'D' and blank_row != 0:
            break
    
    if move == 'L':
        grid[blank_row][blank_col] = grid[blank_row][blank_col+1]
        grid[blank_row][blank_col+1] = 'X'
        blank_col += 1
    elif move == 'R':
        grid[blank_row][blank_col] = grid[blank_row][blank_col-1]
        grid[blank_row][blank_col-1] = 'X'
        blank_col -= 1
    elif move == 'U':
        grid[blank_row][blank_col] = grid[blank_row+1][blank_col]
        grid[blank_row+1][blank_col] = 'X'
        blank_row += 1
    else:
        grid[blank_row][blank_col] = grid[blank_row-1][blank_col]
        grid[blank_row-1][blank_col] = 'X'
        blank_row -= 1

    return move
#-------------------------------------------------------------------------------
def show_grid():
    for r in grid:
        print(r)
#-------------------------------------------------------------------------------
start = time()
moves = {'L':76, 'R': 82, 'U': 85, 'D': 68}
const = 100_000_007
target = [['X','B','R','B'],['B','R','B','R'],['R','B','R','B'],['B','R','B','R']]
blank_row = 0
blank_col = 0
min_moves = 10**8
for _ in range(10**6):
    grid = [['X','R','B','B'],['R','R','B','B'],['R','R','B','B'],['R','R','B','B']]
    num_moves = 0
    checksum = 0
    while True:
        move = make_move()
        num_moves += 1
        if num_moves > 600:
            break
        checksum = (checksum * 243 + moves[move]) % const
        if grid == target:
            if num_moves < min_moves:
                min_moves = num_moves
            break
  
print(min_moves,checksum)
print(time()-start)
#-------------------------------------------------------------------------------
# min paths: 560
# solution: 96_356_848
#-------------------------------------------------------------------------------
