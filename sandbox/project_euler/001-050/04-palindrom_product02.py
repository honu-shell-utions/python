##################################################################################
#jim mccleery, november, 2021, revised March, 2023
##################################################################################
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two
#2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of
#two 3-digit numbers.
##################################################################################
from itertools import combinations
##################################################################################
def make_combos():
    nums = [x for x in range(100,1000)]
    combos = combinations(nums,2)
    return combos
##################################################################################
largest = -1
for a,b in make_combos():
    res = a*b
    if str(res) == str(res)[::-1]:
        if res > largest:
            largest = res
print(largest)
##################################################################################
#solution: 906609 
##################################################################################
