#-------------------------------------------------------------------------------
## Tours on a 4 x n playing board
## Problem 237
## Let T(n) be the number of tours over a 4 × n playing board such that:
## 
## The tour starts in the top left corner.
## The tour consists of moves that are up, down, left, or right one square.
## The tour visits each square exactly once.
## The tour ends in the bottom left corner.
## The diagram shows one tour over a 4 × 10 board:
## 
## T(10) is 2329. What is T(10**12) modulo 10^8?
#-------------------------------------------------------------------------------
import numpy as np
T8 = 10**8

s = np.matrix([[2, 2, -2, 1],
               [1, 0,  0, 0],
               [0, 1,  0, 0],
               [0, 0,  1, 0]], dtype=int)

b = np.array([[4], [1], [1], [0]])

def s12(s):   # Calculate s**(10**12)
    for i in range(12):
        ss= s
        s = s*s % T8  # s**2
        s = s*s % T8  # s**4
        s = ss*s % T8 # s**5
        s = s*s % T8  # s**10
    return s

print(s12(s)*b % T8)
#-------------------------------------------------------------------------------
# solution: 15836928
#-------------------------------------------------------------------------------
