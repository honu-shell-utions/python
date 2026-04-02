#-------------------------------------------------------------------------------
## Concatenation Coincidence
## Problem 751
#-------------------------------------------------------------------------------
from math import ceil, modf
from time import time
#-------------------------------------------------------------------------------
def sequence(t, n):
    def next_b(b):
        b, a = modf(b)
        return a * (1 + b)

    result = f'{t}.'
    i = 1
    while len(result) < n + 2:
        x = float(result)
        for _ in range(i):
            x = next_b(x)
        result += str(int(x))
        i += 1
    return result

start = time()
theta = 2.956938891377988
print(f'Solution: {sequence(2, 24)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 2.223561019313554106173177
#-------------------------------------------------------------------------------
