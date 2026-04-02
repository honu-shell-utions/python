# p108_diophantine_reciprocalsV2.py
#
# In the following equation x, y, and n are positive integers.
#
# 1/x + 1/y = 1/n
#
# For n = 4 there are exactly three distinct solutions:
#
#  1/5 + 1/20 = 1/4
#  1/6 + 1/12 = 1/4
#  1/8 + 1/8  = 1/4
#
# What is the least value of n for which the number of
# distinct solutions exceeds one-thousand?
#
# NOTE: This problem is an easier version of Problem 110;
# it is strongly advised that you solve this one first.
# see p108diophantine_reciprocals.pdf
# x = divisor + denominator
# y = denominator + (denominator**2 // divisor)
from sympy import factorint
from time import time


begin = time()
threshold = 1_000
n = 4

while True:
    d_factors = factorint(n)
    diophantine_tmp = 1
    for exp in d_factors.values():
        diophantine_tmp *= (1 + 2*exp)
    diophantine_divisors = (diophantine_tmp-1) // 2 + 1
    if diophantine_divisors > threshold:
        rt = time() - begin
        print(f'{diophantine_divisors} solutions when n is {n}')
        print('runtime:', rt)
        break
    n += 1
