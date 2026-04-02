#-------------------------------------------------------------------------------
# 194_coloured_configurations.py
# ans: 61190912

# Consider graphs built with the units A (see pdf for pic) and B (see pdf for
# pic) where the units are glued along the vertical edges as in the graph
# (see pdf for pic).
#
# A configuration of type (a, b, c) is a graph thus built of a units A and b
# units B, where the graph's vertices are coloured using up to c colours, so
# that no two adjacent vertices have the same color.
#
# The compound graph above is an example of a configuration of type (2, 2, 6),
# in fact of type (2, 2, c) for all c ≥ 4.
#
# Let N(a, b, c) be the number of configurations of type (a, b, c).
# For example, N(1, 0, 3) = 24, N(0, 2, 4) = 92928 and N(2, 2, 3) = 20736.
#
# Find the last 8 digits of N(25, 75, 1984).
# N(1,0,c) = c (c-1) f1(c),
# N(0,1,c) = c (c-1) f2(c),
# 
# where
# 
# f1(c) = c5 - 9c4 + 34c3 - 69c2 + 77c - 38
# f2(c) = c5 - 8c4 + 27c3 - 50c2 + 52c - 24
# 
# And it follows quite swiftly from there that
# 
# N(a,b,c) = c (c-1) f1(c)a f2(c)b (a+b)!/a!b!

#-------------------------------------------------------------------------------
from math import factorial
from time import time
#-------------------------------------------------------------------------------
def f1(c):
    return c**5 - 9*c**4 + 34*c**3 - 69*c**2 + 77*c - 38
#-------------------------------------------------------------------------------
def f2(c):
    return c**5 - 8*c**4 + 27*c**3 - 50*c**2 + 52*c -24
#-------------------------------------------------------------------------------
def N(a,b,c):
    return c*(c-1) * f1(c)**a * f2(c)**b * factorial(a+b)//(factorial(a)*factorial(b))
#-------------------------------------------------------------------------------
start = time()
print(int(N(1,0,3)))
print(int(N(0,2,4)))
print(int(N(2,2,3)))
sol = N(25, 75, 1984) % 10**8
print(f'Solution: {sol}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#answer: 61190912
#-------------------------------------------------------------------------------
