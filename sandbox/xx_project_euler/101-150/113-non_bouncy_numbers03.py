# p113_non-bouncy numbers.py
# Working from left-to-right if no digit is exceeded by the digit to its left
# it is called an increasing number; for example, 134468.
#
# Similarly, if no digit is exceeded by the digit to its right it is called a
# decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor decreasing a
# "bouncy" number; for example, 155349.
#
# As n increases, the proportion of bouncy numbers below n increases such that
# there are only 12951 numbers below one-million that are not bouncy and only
# 277032 non-bouncy numbers below 10**10.
#
# How many numbers below a googol (10**100) are not bouncy?
# modified p111 takes too long...
# https://cp-algorithms.com/combinatorics/stars_and_bars.html

from time import time
from math import factorial


# stars and bars technique
def nCr(n, r):
    top = factorial(n)
    btm = factorial(n-r)*factorial(r)
    return top // btm

go = time()
n = 100   # 51161058134250
# n = 10  # 277032
# n = 6   # 12951

# nCr((bars+stars),stars)

increasing = nCr(n+9, 9)-1
decreasing = nCr(n+10, 10)-1
ans = increasing + decreasing - 10*n
rt = time() - go
print('ans:', ans)  # 51161058134250
print('runtime:', rt)
