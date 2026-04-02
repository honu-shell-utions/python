# 31-coinSum.py
#
# In the United Kingdom the currency is made up of pound (£) and pence (p).
# There are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?
#------------------------------------------------------------------------------
import numpy as np

coins = np.array([1, 2, 5, 10, 20, 50, 100, 200], int)

def count_ways(target, avc):
    if avc <=1: return 1
    res = 0
    while target >= 0:
        res = res + count_ways(target, avc -1)
        target = target - coins[avc-1]
    return res

amount = 200
ways = np.zeros(amount, int)
print(count_ways(amount, len(coins)))
#solution: 73682
