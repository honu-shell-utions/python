################################################################################
##Arithmetic expressions
##Problem 93
##By using each of the digits from the set, {1, 2, 3, 4},
##exactly once, and making use of the four arithmetic operations
##(+, −, *, /) and brackets/parentheses, it is possible to form
##different positive integer targets.
##
##For example,
##
##8 = (4 * (1 + 3)) / 2
##14 = 4 * (3 + 1 / 2)
##19 = 4 * (2 + 3) − 1
##36 = 3 * 4 * (2 + 1)
##
##Note that concatenations of the digits, like 12 + 34, are not allowed.
##
##Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
##target numbers of which 36 is the maximum, and each of the numbers 1 to 28
##can be obtained before encountering the first non-expressible number.
##
##Find the set of four distinct digits, a < b < c < d, for which the
##longest set of consecutive positive integers, 1 to n, can be obtained,
##giving your answer as a string: abcd.
################################################################################
from  operator import add, sub, mul, truediv
import itertools
import time
################################################################################
def seq_length(s,c=1):
    while c in s:
        c+= 1
    return c-1
################################################################################
start = time.time()
maxt, maxs = 0, 0
for terms in itertools.combinations(range(1, 10), 4):
    s = set()
    for n in itertools.permutations(terms):
        for op in itertools.product([add, mul, sub, truediv], repeat=3):
            x = op[0](op[1](n[0],n[1]),op[2](n[2],n[3]))        # (a.b).(c.d)
            if x%1 == 0 and x > 0:
                s.add(int(x))
                x = op[0](op[1](op[2](n[0],n[1]),n[2]),n[3])   # ((a.b).c).d
                if x%1 == 0 and x > 0:
                    s.add(int(x))
                    if seq_length(s) > maxs:
                        maxs, maxt = seq_length(s), terms

print('Solution:', ''.join(str(i) for i in maxt),'Run time:',time.time()-start)
################################################################################
#solution: 1258
################################################################################
