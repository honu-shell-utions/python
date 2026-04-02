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
from functools import cache
import sys
sys.setrecursionlimit(10**8)


# A181688

@cache
def a(n):
    if n == 1: return 1
    if n == 2: return 1
    if n == 3: return 4
    if n == 4: return 8
    if n == 5: return 23
    return 2*a(n-1) + 2*a(n-2) - 2*a(n-3) + a(n-4)
#-------------------------------------------------------------------------------
##print(5,a(5))
##print(10,a(10))
##print(20,a(20))
##print(100,a(100))

##print(a(10**12) % 10**8)
print(a(5.6 * 10**8) % 10**8)
#-------------------------------------------------------------------------------
# solution: 15836928
#-------------------------------------------------------------------------------
