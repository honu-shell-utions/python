#  -----------------------------------------------------------------------------
#  Near Power Sums
#  Problem 749
#  https://projecteuler.net/problem=749
#  -----------------------------------------------------------------------------
from time import time
from math import log, ceil, floor
from collections import Counter
#  -----------------------------------------------------------------------------
def euler_749(power, lowest, digits, val):
    if len(digits) == size:
        if val == 0:
            return
        digcount = Counter(digits)
        lildigcount = Counter(map(int, str(val-1)))
        for _ in range(size - len(str(val-1))):
            lildigcount[0] += 1
        bigdigcount = Counter(map(int, str(val+1)))
        for _ in range(size - len(str(val+1))):
            bigdigcount[0] += 1

        if lildigcount == digcount:
            found.add(val-1)
        if bigdigcount == digcount and val+1 < 10**size:
            found.add(val+1)
        return

    for dig in range(lowest, 10):
        if val + dig**power < 10**size:
            euler_749(power, dig, digits + [dig], val + dig**power)    
#  -----------------------------------------------------------------------------
size = 16
found = set()
power = 1
while 2**power < 10**size:
    euler_749(power, 0, [], 0)
    power += 1

print(sum(found))
#  -----------------------------------------------------------------------------
print("Answer: ", total)
print("Time: ", time() - start)
#  -----------------------------------------------------------------------------
#  solution: 13459471903176422
#  -----------------------------------------------------------------------------
