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
##------------------------------------------------------------------------------
def make_perms():
    t_list = []
    temp = list(permutations(values))
    for t in temp:
        if t[0] != 0:
            t_list.append(t)

    return sorted(t_list,reverse=True)
    
##------------------------------------------------------------------------------
def euler_170(perm):
    for position in range(1,len(values)-1):
        perm_s = ''
        for p in perm:
            perm_s += str(p)
        front = int(''.join(perm_s[:position]))
        temp = ''.join(perm_s[position:])
        if temp[0] == 0:
            continue
        back = int(temp)
        g = gcd(front,back)
        if g % 3 != 0:
            continue
        temp1 = str(front) + str(back)
        temp2 = str(g)+str(front//g)+str(back//g)
        if sorted(temp1) == sorted(perm_s) and sorted(temp2) == sorted(perm_s):
            return int(temp1)
            #print(temp1,temp2,g,front//g,back//g)
    return -1
##------------------------------------------------------------------------------
values = [0,1,2,3,4,5,6,7,8,9]
perms = make_perms()
max_cp = -10**6
for p in perms:
    temp = euler_170(p)
    if temp > max_cp:
        max_cp = temp

print(max_cp)
##------------------------------------------------------------------------------
##solution: 9857164023
##------------------------------------------------------------------------------
