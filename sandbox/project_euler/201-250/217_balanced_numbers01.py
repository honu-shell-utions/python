#-------------------------------------------------------------------------------
##Balanced Numbers
##Problem 217
##A positive integer with k (decimal) digits is called balanced
##if its first ⌈k/2⌉ digits sum to the same value as its last ⌈k/2⌉
##digits, where ⌈x⌉, pronounced ceiling of x, is the smallest
##integer ≥ x, thus ⌈π⌉ = 4 and ⌈5⌉ = 5.
##
##So, for example, all palindromes are balanced, as is 13722.
##
##Let T(n) be the sum of all balanced numbers less than 10^n. 
##Thus: T(1) = 45, T(2) = 540 and T(5) = 334795890.
##
##Find T(47) mod 3^15
#-------------------------------------------------------------------------------
from math import ceil
#-------------------------------------------------------------------------------
def is_balanced(n):
    n_list = []
    for n in list(str(n)):
        n_list.append(int(n))
    sum_left = 0
    sum_right = 0
    half = len(n_list)//2
    if len(n_list) % 2 == 0:
        sum_left = sum(n_list[0:half])                     
    else:
        sum_left = sum(n_list[0:half+1])
    sum_right = sum(n_list[half:])                           
    return sum_left == sum_right
#-------------------------------------------------------------------------------
def T(n):
    sum_balanced = 0
    for j in range(1,10**n):
        if is_balanced(j):
            sum_balanced += j
    return sum_balanced
#-------------------------------------------------------------------------------
print(T(1))
print(T(2))
print(T(5))
#print(T(47)%(3**15))

#-------------------------------------------------------------------------------
# solution: 6273134
#-------------------------------------------------------------------------------
