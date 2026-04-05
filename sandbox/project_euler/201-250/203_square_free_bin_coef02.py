
# The binomial coefficients (n over k) can be arranged in triangular form,
# Pascal's triangle, like this:
#
#        1
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1
#   1 5 10 10 5 1
#  1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
#      .........
#
# It can be seen that the first eight rows of Pascal's triangle contain twelve
# distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.
#
# A positive integer n is called squarefree if no square of a prime divides n.
# Of the twelve distinct numbers in the first eight rows of Pascal's triangle,
# all except 4 and 20 are squarefree. The sum of the distinct squarefree
# numbers in the first eight rows is 105.
#
# Find the sum of the distinct squarefree numbers in the first 51 rows of
# Pascal's triangle.
# ____________________________________________________________________________
from math import factorial
from time import time
# ____________________________________________________________________________
def n_r(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))
# ____________________________________________________________________________
def bin_coefficients(rows):
    distinct_nums = set()
    for r in range(rows):
        for c in range(r+1):
            distinct_nums.add(n_r(r, c))
    return distinct_nums
# ____________________________________________________________________________
# A positive integer n is called squarefree if no square
# of a prime divides n
def sum_squarefree_nums(nums):
    # Only a few primes are required. For example, 51! is the biggest numerator
    # (nCk = n! / k! (n-k)! ) and the largest prime factor required is ≤ √51 which
    # is 7. You can add a few more to try bigger problems.
    primes_sqrd = tuple(x*x for x in (2, 3, 5, 7))
    
    bad_total = 0
    for n in nums:
        for x in primes_sqrd:
            if n % x == 0:
                bad_total += n
                break

    return sum(nums) - bad_total
# ____________________________________________________________________________
t0 = time()
nums = bin_coefficients(51)
tally = sum_squarefree_nums(nums)
print(f'{tally}  {tally==34029210557338}  rt: {time()-t0}')  # 
# ____________________________________________________________________________
