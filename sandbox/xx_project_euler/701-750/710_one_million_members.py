# ----------------------------------------------------------------------------
# 710_one_million_members.py
#
# One Million Members
# The number 6 can be written as a palindromic sum in exactly eight different
# ways: (1, 1, 1, 1, 1, 1), (1, 1, 2, 1, 1), (1, 2, 2, 1), (1, 4, 1),
# (2, 1, 1, 2), (2, 2, 2), (3, 3), (6)
#
# We shall define a twopal to be a palindromic tuple having at least one
# element with a value of 2. It should also be noted that elements are not
# restricted to single digits. For example, (3, 2, 13, 6, 13, 2, 3) is a valid
# twopal.
#
# If we let t(n) be the number of twopals whose elements sum to n, then it can
# be seen that t(6) = 4:
# (1, 1, 2, 1, 1), (1, 2, 2, 1), (2, 1, 1, 2), (2, 2, 2)
#
# Similarly t(20) = 824
#
# In searching for the answer to the ultimate question of life, the universe,
# and everything, it can be verified that t(42) = 1_999_923, which happens to
# be the first value of t(n) that exceeds one million.
#
# However, your challenge to the "ultimatest" question of life, the universe,
# and everything is to find the least value of n > 42 such that t(n) is
# divisible by one million.
# ----------------------------------------------------------------------------
from sympy.utilities.iterables import partitions
from math import factorial
# ----------------------------------------------------------------------------
for n in [6,20,42,61,75,100]:
    num_palins = 0
    for p in partitions(n):
        odds = 0
        ok = False
        half_len = sum(p.values()) // 2
        for key, val in p.items():
            if key == 2:
                ok = True
            if val % 2 == 1:
                odds += 1           
        if odds in [0,1] and ok:
            palins = factorial(half_len)
            for v in p.values():
                palins //= factorial(v//2)
            num_palins += palins
            
    print(f'Number of palindromes in partitions of {n}: {num_palins}')    
# ----------------------------------------------------------------------------
# solution = 1275000
# ----------------------------------------------------------------------------
