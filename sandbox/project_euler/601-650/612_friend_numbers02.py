#  -----------------------------------------------------------------------------
#  Friend numbers
#  Problem 612
#  https://projecteuler.net/problem=612
#  -----------------------------------------------------------------------------
from time import time
from math import factorial
#  -----------------------------------------------------------------------------
def binomial(n, k):
    assert n >= 0 and k >= 0
    if n < k:
        return 0
    return factorial(n) // (factorial(n - k) * factorial(k))
#  -----------------------------------------------------------------------------
# counts how many numbers up to a digits contain a specific set of b digits,
# zero NOT allowed.
def F(a, b):
    assert a >= 0 and b >= 0
    if a < b or a == 0:
        return 0
    if b == 0:
        return 10 ** a
    if a == b:
        return factorial(a)
    return (10 - b) * F(a - 1, b) + b * F(a - 1, b - 1)
#  -----------------------------------------------------------------------------
# counts how many numbers up to a digits contain a specific set of b digits,
# zero MUST be included.
def F0(a, b):
    assert a >= 0 and b >= 0
    if a < b or a == 0:
        return 0
    if b == 0:
        return 10 ** a
    if a == b:
        return factorial(a) - factorial(a - 1)
    return (10 - b) * F(a - 1, b) + (b - 1) * F(a - 1, b - 1) + F0(a - 1, b)
#  -----------------------------------------------------------------------------
def calc_friend(n):
    return (n * (n - 1)) // 2
#  -----------------------------------------------------------------------------
def euler_612(N):
    solution = 0
    for d in range(1, 10, 2):
        solution += binomial(9, d - 1) * calc_friend(F0(N, d))
        solution += binomial(9, d) * calc_friend(F(N, d))
        solution -= binomial(9, d) * calc_friend(F0(N, d + 1))
        solution -= binomial(9, d + 1) * calc_friend(F(N, d + 1))
    return solution % MOD
#  -----------------------------------------------------------------------------
MOD = 1000267129
for exp in range(2,31):
    start = time()
    solution = euler_612(exp)
    if exp == 18:
        print('-'*65)
    print(f'Solution for 10^{exp:2}: {solution:10}, Run-Time: {time()-start}')
    if exp == 18:
        print('-'*65)
#  -----------------------------------------------------------------------------    
## 10 ^ 2 -> 1539 0.000121
## 10 ^ 3 -> 289665 0.000162
## 10 ^ 4 -> 39235977 0.000137
## 10 ^ 5 -> 527566505 0.000165
## 10 ^ 18 -> 819963842 0.498931
#  -----------------------------------------------------------------------------
#  solution: 819963842
#  -----------------------------------------------------------------------------
