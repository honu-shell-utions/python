#-------------------------------------------------------------------------------
## Best Approximations
## Problem 192
#-------------------------------------------------------------------------------
from fractions import Fraction
from decimal import Decimal, getcontext
from time import time
#-------------------------------------------------------------------------------
start = time()
getcontext().prec = 55        # decimal digits of sqrt()
numbers = list(range(10**5+1))
denom_bound = 10**12
#-------------------------------------------------------------------------------
sum_denom = 0
for n in numbers :
    sqrtn = Decimal(n).sqrt()
    t = Fraction(sqrtn).limit_denominator(denom_bound)
    if t.denominator == 1:
        continue
    sum_denom += t.denominator
    
print(f'Solution: {sum_denom}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#solution: 57060635927998347
#-------------------------------------------------------------------------------
