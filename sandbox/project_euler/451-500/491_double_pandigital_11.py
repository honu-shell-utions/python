#  -----------------------------------------------------------------------------
#  Double pandigital number divisible by 11
#  Problem 491
#  https://projecteuler.net/problem=491
#  -----------------------------------------------------------------------------
from itertools import combinations
from math import factorial
#  -----------------------------------------------------------------------------
fact10 = factorial(10)
digits = [0,1,2,3,4,5,6,7,8,9]
digits += digits
pools = []
answer = 0
combos = combinations(digits,10)
for c in combos:
    sum_odds = sum(c)
    sum_evens = 90 - sum_odds
    if abs(sum_evens - sum_odds) % 11 == 0:
        sc = sorted(c)
        if sc not in pools:
            pools.append(sc)
            
for p in pools:
    pairs = 10 - len(set(p))      
    allways = fact10//(2**pairs)
    answer += allways**2

print(answer*9//10)   
#  -----------------------------------------------------------------------------
#  solution: 194505988824000
#  -----------------------------------------------------------------------------
