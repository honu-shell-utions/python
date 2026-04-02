# p092_square_digit_chainsV2.py
#
# A number chain is created by continuously adding the square of the digits in
# a number to form a new number until it has been seen before.
#
# For example,
#  44 → 32 → 13 → 10 → 1 → 1
#  85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless
# loop. What is most amazing is that EVERY starting number will eventually
# arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?
import itertools
from math import factorial
from time import time


begin = time()
def square_digits(num):
    # squares the digits of a number, eg 44=4^2 + 4^2=32
    total = 0
    while num:
        total += (num % 10) ** 2
        num //= 10
    return total

    
def my_square_chain(i):
    if i == 1 or i == 89: 
        return i

    return my_square_chain(square_digits(i))


# https://codereview.stackexchange.com/questions/109255/project-euler-92-square-digit-chains
# 
# Consider the number 4,666,777. This number happens to chain into 89. That takes
# some amount of work to figure out. But eventually we get there. What does this
# tell us? Since we're only interested in the sum of the squares of the digits,
# the actual ordering of the digits is irrelevant. That is... once we know that
# 4,666,777 is valid, we also know that 6,466,777 is valid, and 7,664,776 is
# valid, and ... All 140 unique permutations of the digits 4666777 are things we
# want to count. The key is: once we're done with 4666777, we do not even need
# to consider the other 139!
# 
# There are only 11,440 unique digit combinations from 1 to 10,000,000. Any
# solution checking all of them is thus doing ~900x more work than necessary.
# We can use itertools.combinations_with_replacement to get the unique digit
# combinations, and then use itertools.groupby to help determine how many such
# combinations there are.
# 
# Still with the memoized my_square_chain:

def euler89():
    count_89 = 0 
    fact7 = factorial(7)
    digits = range(10)

    for num in itertools.combinations_with_replacement(digits, 7): 
        cur = sum(d**2 for d in num)
        if cur > 0 and my_square_chain(cur) == 89:
            count = fact7
            for _, g in itertools.groupby(num):
                count /= factorial(len(list(g)))
            count_89 += count
    return int(count_89)

print('ans:', euler89(), 'runtime:', time() - begin)  # 8581146 
