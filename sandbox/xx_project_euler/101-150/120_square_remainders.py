################################################################################
# 128_square_remainders.py
#
# Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.
#
# For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49.
# And as n varies, so too will r, but for a = 7 it turns out that r(max) = 42.
# 
# For 3 ≤ a ≤ 1000, find ∑ r(max).
# NOTE: r(max) max is subscript
################################################################################
from time import time

start = time()
total = 0
for a in range(3,1001):
    if a % 2 == 0:
        total += a**2 - 2*a
    else:
        total += a**2 - a
        
print('The Solution:',total,'Total Run Time:',time()-start)

################################################################################
# solution: 333082500
################################################################################
