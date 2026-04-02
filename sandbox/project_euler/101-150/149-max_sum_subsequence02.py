################################################################################
from time import time
import numpy as np
################################################################################
def load_grid():
    for i in range(SIZE ** 2):
        if i <= 55:
            grid[i] = ((100003 - 200003 * i + 300007 * i * i * i) % 1000000 - 500000)
        else:
            grid[i] = ((grid[i-24] + grid[i-55]) % 1000000) - 500000
################################################################################
def get_max_substring_sum(x, y, dx, dy):
    result = 0
    current = 0
    while 0 <= x < SIZE and 0 <= y < SIZE:
        current = max(current + grid[y][x], 0)  # reset the running sum if it goes negative
        result = max(current, result)           # best seen running sum
        x += dx
        y += dy
    return result
################################################################################
def scan_all():
    max_row = -10**9
    max_col = -10**9
    for i in range(SIZE):
        #process the rows
        temp = get_max_substring_sum(0,i,+1,0)
        if temp > max_row:
            max_row = temp
        #process the columns
    for i in range(SIZE):
        temp = get_max_substring_sum(i,0,0,+1)
        if temp > max_col:
            max_col = temp
    return max(int(max_row),int(max_col))
################################################################################
start = time()
SIZE = 2000
grid = np.zeros(SIZE**2)
load_grid()
grid = grid.reshape(SIZE,SIZE)
ans = scan_all()
end = time()
run_time = round(end - start,2)
print(f'greatest substring sum = {ans} runtime: {run_time} seconds.')
################################################################################
#solution: 52852124
################################################################################

