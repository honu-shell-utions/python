##------------------------------------------------------------------------------
# 170_pandigital_products.py
#
# Find the largest 0 to 9 pandigital that can be
# formed by concatenating products
#
# Take the number 6 and multiply it by each of 1273 and 9854:
#    6 × 1273 = 7638
#    6 × 9854 = 59124
# By concatenating these products we get the 1 to 9 pandigital 763859124.
# We will call 763859124 the "concatenated product of 6 and (1273,9854)".
# Notice too, that the concatenation of the input numbers, 612739854, is
# also 1 to 9 pandigital.
#
# The same can be done for 0 to 9 pandigital numbers.
#
# What is the largest 0 to 9 pandigital 10-digit concatenated product of an
# integer with two or more other integers, such that the concatenation of
# the input numbers is also a 0 to 9 pandigital 10-digit number?
##------------------------------------------------------------------------------
from itertools import permutations
from math import gcd
from time import time
##------------------------------------------------------------------------------
def is_pan(perm):
    return sorted(perm) == values
##------------------------------------------------------------------------------
def make_int(perm):
    return int(''.join(perm))
##------------------------------------------------------------------------------
def make_perms():
    p_list = list(permutations(values))
    return sorted(p_list,reverse=True)
##------------------------------------------------------------------------------
def euler_170(perm):
    for position in range(1,len(values)-1):
        front = int(''.join(perm[:position]))
        temp = ''.join(perm[position:])
        if temp[0] == 0:
            continue
        back = int(temp)
        g = gcd(front,back)
        if g % 3 != 0:
            continue
        temp = str(g)+str(front//g)+str(back//g)
        if is_pan(temp):
            return True
    return False
##------------------------------------------------------------------------------
start = time()
values = ['0','1','2','3','4','5','6','7','8','9']
perms = make_perms()
for p in perms:
    if euler_170(p):
        ans = make_int(p)
        break

print(f'Solution: {ans}, Run-Time: {time()-start}')
##------------------------------------------------------------------------------
##solution: 9857164023
##------------------------------------------------------------------------------
