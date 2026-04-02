##Starting in the top left corner of a 2×2 grid, and only
##being able to move to the right and down, there are exactly
##6 routes to the bottom right corner.
##How many such routes are there through a 20×20 grid?
## jim mccleery, november, 2021

from math import comb
import scipy.special

n = 40
k = 20
# Print total number of possible combinations
print(comb(n, k))
print(round(scipy.special.binom(n, k)))
#solution: 137846528820
