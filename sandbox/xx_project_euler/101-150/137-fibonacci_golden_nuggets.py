################################################################################
##Fibonacci golden nuggets
##Problem 137
##
##For this problem we shall be interested in values of x for which 
##A(x) is a positive integer.
##
##We shall call A(x) a golden nugget if x is rational,
##because they become increasingly rarer; for example,
##the 10th golden nugget is 74049690.
##
##Find the 15th golden nugget.
################################################################################
from sympy import fibonacci as fib
################################################################################
solution = fib(2*15) * fib(2*15 + 1)
print(solution)
################################################################################
#solution: 1120149658760
################################################################################
