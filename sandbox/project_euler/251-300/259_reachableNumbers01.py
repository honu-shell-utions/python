# ----------------------------------------------------------------------------
# 259_reachableNumbers.py
#
# Reachable Numbers
# A positive integer will be called reachable if it can result from an
# arithmetic expression obeying the following rules:
# • uses the digits 1 through 9, in that order and exactly once each
# • any successive digits can be concatenated (for example, using the digits
#   2, 3 and 4 we obtain the number 234)
# • only the four usual binary arithmetic operations (addition, subtraction,
#   multiplication and division) are allowed
# • each operation can be used any number of times, or not at all
# • unary minus is not allowed
# • any number of (possibly nested) parentheses may be used to define the order
#   of operations
#
# For example, 42 is reachable, since (1 / 23) * ((4 * 5) - 6) * (78 - 9) = 42
#
# What is the sum of all positive reachable integers?  {ans == 20101196798}
# ----------------------------------------------------------------------------
from fractions import *
from itertools import *
from functools import *
from time import time
# ----------------------------------------------------------------------------
start = time()
n = 9
f = [[set() for i in range(n + 1)] for j in range(n + 1)]

for l in reversed(range(n + 1)):
    for r in range(l + 1, n + 1):
        tmp = [Fraction(reduce(lambda x, y: x * 10 + y, range(1, n + 1)[l:r]))]
        for k in range(l, r):
            print ('[%d, %d] <= |%d| * |%d|' % (l, r, len(f[l][k]), len(f[k][r])))
            for a in f[l][k]:
                for b in f[k][r]:
                    tmp += [a + b]
                    tmp += [a - b]
                    tmp += [a * b]
                    if b != 0:
                        tmp += [a / b]

        f[l][r] = set(tmp)
        print ("l = %d, r = %d, f[l, r].size = %d" % (l, r, len(f[l][r])))

ans = 0
for v in f[0][n]:
    if v == int(v) and v > 0:
        ans += int(v)
        
print(f'Solution: {ans}, Run-Time: {time()-start}')
# ----------------------------------------------------------------------------
# solution: 20101196798
# ----------------------------------------------------------------------------
