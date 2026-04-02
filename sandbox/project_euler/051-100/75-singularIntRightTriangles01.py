################################################################################
# It turns out that 12 cm is the smallest length of wire that can be bent to
# form an integer sided right angle triangle in exactly one way, but there
# are many more examples.
# 12 cm: (3, 4, 5)
# 24 cm: (6, 8, 10)
# 30 cm: (5, 12, 13)
# 36 cm: (9, 12, 15)
# 40 cm: (8, 15, 17)
# 48 cm: (12, 16, 20)
#
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
# integer sided right angle triangle, and other lengths allow more than one
# solution to be found; for example, using 120 cm it is possible to form
# exactly three different integer sided right angle triangles.
# 120 cm: (30, 40, 50), (20, 48, 52), (24, 45, 51)
#
# Given that L is the length of the wire, for how many values of L ≤ 1_500_000
# can exactly one integer sided right angle triangle be formed?
################################################################################
from itertools import takewhile, count
from math import gcd
import time
################################################################################
LIMIT = 1_500_000
def findHits():
    found_per = set()
    rep_per = set()
    generator = ((n, m) for n in count(3, 2) for m in range(1, n, 2) if gcd(m,n) == 1)
    for n, m in generator:
        a = n * m
        b = (n ** 2 - m ** 2) // 2
        c = (n ** 2 + m ** 2) // 2
        #print(n,m,a,b,c)
        perimeter = a + b + c
        if m == 1 and perimeter > LIMIT:
            break
        for per in takewhile(lambda x: x <= LIMIT, (perimeter * i for i in count(1))):
            if per in found_per:
                rep_per.add(per)
            else:
                found_per.add(per)
                
    print("The result is", len(found_per - rep_per),'Run time:',time.time()-start)
################################################################################
start = time.time()
findHits()
################################################################################
#solution: 161667
################################################################################
