# 96-sudokuComputer.py
# The objective of SuDoku puzzles is to replace the blanks (or zeros) in a
# 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of
# the digits 1 to 9.
#
# The file contains fifty different Su Doku puzzles ranging in difficulty, but
# all with unique solutions.
#
# By solving all fifty puzzles find the sum of the 3-digit numbers found in the
# top left corner of each solution grid; for example, 483 is the 3-digit number
# found in the top left corner of grid 01.

import numpy as np
import time

filename = '96-Sudoku.txt'
tally = 0

def parse_grids(lines):
    lst_grid = []
    for i in range(0, len(lines), 10):
        lst_row = []
        for j in range(1, 10):
            row = [int(digit) for digit in lines[i + j].strip()]
            lst_row.append(row)
        lst_grid.append(lst_row)
    return lst_grid

def read_file(fn):
    with open(fn, 'r') as txtfile:
        lines = txtfile.readlines()
        grids = parse_grids(lines)
    arr = np.array(grids, dtype=int)
    return arr

def possible(y, x, n):  # helper function
    global grid
    global tally

    for i in range(0, 9):
        if grid[y][i] == n:  # checking down (like y-axis cartesian or row)
            return False
    for i in range(0, 9):
        if grid[i][x] == n:  # checking across (like x-axis cartesian or col)
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:  # checking peers in mini-square
                return False
    return True


def solve():  # recursive with back-tracking if necessary
    global grid
    global tally

    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y][x] == 0:  # looping to find "empty" square

                # loop through all the numbers we could put in square 1, 2, ..., 9
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0  # back-tracking, went through possible n-vals without success
                return  # finished (no empty squares)
    tally += (grid.item(0) * 100) + (grid.item(1) * 10) + grid.item(2)

start = time.time()
np_arr = read_file(filename)
for i in range(50):
    grid = np_arr[i].copy()
    solve()

print()
print('The solution:', tally,'Running time:',time.time()-start)
