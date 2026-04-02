# ----------------------------------------------------------------------------
# 171_sum_squares.py
# finding numbers for which the sum of the squares of the digits is a square
#
# For a positive integer n, let f(n) be the sum of the squares of the digits
# (in base 10) of n, e.g.
#      f(3) = 3^2 = 9,
#      f(25) = 2^2 + 5^2 = 4 + 25 = 29,
#      f(442) = 4^2 + 4^2 + 2^2 = 16 + 16 + 4 = 36
#
# Find the last nine digits of the sum of all n, 0 < n < 10^20, such that
# f(n) is a perfect square.
# ----------------------------------------------------------------------------
from math import sqrt, isqrt
from time import time
# ----------------------------------------------------------------------------
def f(n):
    total = 0
    while n > 0:
        total += (n % 10)**2
        n //= 10

    if sqrt(total) == isqrt(total):
        return True
    else:
        return False
# ----------------------------------------------------------------------------
start = time()
total = 0
for n in range(1,10**8):
    if f(n):
        total += n
        total %= 10**9


print(f'The solution is {total}, Run-Time is {time()-start}')
# ----------------------------------------------------------------------------
# solution: 142989277
# ----------------------------------------------------------------------------
