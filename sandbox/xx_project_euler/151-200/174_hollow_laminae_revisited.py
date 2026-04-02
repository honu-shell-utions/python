# p174_hollow_laminae_revisited.py
#
# counting the number of "hollow" square laminae that can form one, two,
# three, ... distinct arrangements
#
# We shall define a square lamina to be a square outline with a square
# "hole" so that the shape possesses vertical and horizontal symmetry.
#
# Given eight tiles it is possible to form a lamina in only one way:
# 3x3 square with a 1x1 hole in the middle. However, using thirty-two tiles
# it is possible to form two distinct laminae.  see pic on website
#
# If t represents the number of tiles used, we shall say that t = 8 is
# type L(1) and t = 32 is type L(2).
#
# Let N(n) be the number of t ≤ 1,000,000 such that t is type L(n); for example,
# N(15) = 832.
# 
# What is ∑N(n) for 1 ≤ n ≤ 10?
# ----------------------------------------------------------------------------
from time import time
from numpy import zeros
#-------------------------------------------------------------------------------
start = time()
limit = 10**6
tally = zeros(limit+1, int)

for hole_edge in range(1,limit//4):
    layer_edge = hole_edge + 2
    layer_accumulations = 0
    while True:
        layer_area = layer_edge**2 - layer_accumulations - hole_edge**2
        layer_accumulations += layer_area
        if layer_accumulations > limit:
            break
        else:
            tally[layer_accumulations] += 1
        layer_edge += 2

ans = 0
for k in tally:
    if 1 <= k <= 10:
        ans += 1

print(f'Solution: {ans}, Run-Time:{time()-start}')
#-------------------------------------------------------------------------------
#solution: 209566
#-------------------------------------------------------------------------------
