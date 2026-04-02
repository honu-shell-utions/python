# -----------------------------------------------------------------------------
# 725_digit_sum_numbers.py
#
# Digit Sum Numbers
# A number where one digit is the sum of the other digits is called a digit
# sum number or DS-number for short. For example, 352, 3003 and 32812 are
# DS-numbers.
#
# We define S(n) to be the sum of all DS-numbers of n digits or less.
#
# You are given S(3) = 63270 and S(7) = 85499991450
#
# Find S(2020). Give your answer modulo 10^16
# -----------------------------------------------------------------------------
from time import time
# -----------------------------------------------------------------------------
def is_DSN(n):
    str_n = str(n)
    lst_n = sorted(str_n)
    max_val = int(lst_n[-1])
    total = 0
    for d in lst_n[:-1]:
        total += int(d)
    return total == max_val
# -----------------------------------------------------------------------------
def S(limit):
    ans = 0
    for n in range(1,limit):
        if is_DSN(n):
            ans += n
    return ans
# -----------------------------------------------------------------------------
MOD = 10**16
for max_digits in range(1,10):
    start = time()
    ans = S(10**max_digits) % MOD
    print(f'Solution for limit = {10**max_digits}: {ans}, Run-Time: {time()-start}')
# -----------------------------------------------------------------------------
# solution: 4598797036650685
# -----------------------------------------------------------------------------
