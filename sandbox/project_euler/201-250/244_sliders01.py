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

#-------------------------------------------------------------------------------
def make_move(move):
    global blank_row
    global blank_col
    
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
#-------------------------------------------------------------------------------
def show_grid():
    for r in grid:
        print(r)
    print()
#-------------------------------------------------------------------------------
moves = {'L':76, 'R': 82, 'U': 85, 'D': 68}
const = 100_000_007
checksum = 0
grid = [['X','R','B','B'],['R','R','B','B'],['R','R','B','B'],['R','R','B','B']]
blank_row = 0
blank_col = 0
show_grid()
for c in 'LULUR':
    print(c)
    make_move(c)
    show_grid()
    checksum = (checksum * 243 + moves[c]) % const
    
print(checksum, checksum == 19761398)
#-------------------------------------------------------------------------------
# solution: 96356848
#-------------------------------------------------------------------------------
