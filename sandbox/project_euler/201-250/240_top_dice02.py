# 240_top_dice_monteCarlo.py
#
# Top Dice
# There are 1_111 ways in which five 6-sided dice (sides numbered 1 to 6)
# can be rolled so that the top three sum to 15. Some examples are: 
# 
# D1, D2, D3, D4, D5 = 4, 3, 6, 3, 5 
# D1, D2, D3, D4, D5 = 4, 3, 3, 5, 6 
# D1, D2, D3, D4, D5 = 3, 3, 3, 6, 6 
# D1, D2, D3, D4, D5 = 6, 6, 3, 3, 3 
# 
# In how many ways can twenty 12-sided dice (sides numbered 1 to 12)
# be rolled so that the top ten sum to 70?
# {ans == 7448717393364181966}
# -----------------------------------------------------------------------------
from itertools import combinations_with_replacement
from math import factorial
from time import time

start = time()
DICE_COUNT = 20
FACE_COUNT = 12
TOP_DICE_COUNT = 10
TOP_DICE_SUM = 70

def get_combination_count(combination):
    freqs = [0] * FACE_COUNT
    for i in combination:
        freqs[i - 1] += 1
    n, d = factorial(DICE_COUNT), 1
    for i in freqs:
        d *= factorial(i)
    return int(n/d)
    
def euler_240():
    ways = 0
    for i in combinations_with_replacement(range(1, FACE_COUNT + 1), DICE_COUNT):
        if sum(i[DICE_COUNT - TOP_DICE_COUNT::]) == TOP_DICE_SUM:
            ways += get_combination_count(i)
    return ways
    
print(f'Solution: {euler_240()}, Run-Time: {time()-start}')
# -----------------------------------------------------------------------------
# solution: 7448717393364181966
