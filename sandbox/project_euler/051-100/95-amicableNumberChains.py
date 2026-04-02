# 95-amicableChains.py
# The proper divisors of a number are all the divisors excluding the number
# itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As
# the sum of these divisors is equal to 28, we call it a perfect number.
#
# Interestingly the sum of the proper divisors of 220 is 284 and the sum of
# the proper divisors of 284 is 220, forming a chain of two numbers. For this
# reason, 220 and 284 are called an amicable pair.
#
# Perhaps less well known are longer chains. For example, starting with 12496,
# we form a chain of five numbers:
#
#  12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
#
# Since this chain returns to its starting point, it is called an amicable
# chain.
#
# Find the smallest member of the longest amicable chain with no element
# exceeding one million.

# INFO: sociable numbers research wikipedia, mathworld, ...
# Are there numbers whose aliquot sequence has period 3? Not that we know of.
# Currently the only aliquot sequence periods that have been demonstrated are
# 4, 5, 6, 8, 9, and 28

# In 1918 Poulet found the example above of length five and the following chain
# of length 28.
#
# 14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072, 589786, 294896,
# 358336, 418904, 366556, 274924, 275444, 243760, 376736, 381028, 285778,
# 152990, 122410, 97946, 48976, 45946, 22976, 22744, 19916, 17716
# ans:  14316
################################################################################
from math import isqrt
import time
################################################################################
factor_limit = 1_000_000
################################################################################
def proper_divisors(n):
    divs = set()
    divs.add(1)
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(list(divs))
################################################################################
def makeChain(n):
    chain = [n]
    currentValue = n

    while True:
        newValue = sum(proper_divisors(currentValue))
        if newValue == n:
            return True,chain
        elif newValue in chain or newValue > MAX_SIZE or newValue == 1:
            return False,chain
        else:
            chain.append(newValue)
            currentValue = newValue
################################################################################
start = time.time()
MAX_SIZE = 1_000_000
max = 0
keepMe = []

for i in range(1,100_000):
    hit,lst = makeChain(i)
    size = len(lst)
    if hit and size > max:
        max = size
        keepMe = lst
        
print('Solution:',max,keepMe,'Run Time:',time.time()-start)
################################################################################

