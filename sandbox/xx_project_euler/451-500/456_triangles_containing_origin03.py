from collections import defaultdict
from fractions import Fraction
from time import time
start = time()

target = 2_000_000

n = defaultdict(int)
n[(5,0)] = 0

x_pow = 1
y_pow = 1
for _ in range(target):
    x_pow = (x_pow * 1248) % 32323
    y_pow = (y_pow * 8421) % 30103

    x = x_pow - 16161
    y = y_pow - 15051

    if y >= 0 and x > 0:
        n[(1,Fraction(y,x))] += 1
        n[(3,Fraction(y,x))] += 0
    elif y > 0 and x <= 0:
        if x  == 0:
            n[(2,float("-inf"))] += 1
            n[(4,float("-inf"))] += 0
        else:
            n[(2,Fraction(y,x))] += 1
            n[(4,Fraction(y,x))] += 0
    elif y <= 0 and x < 0:
        n[(3,Fraction(y,x))] += 1
    elif y < 0 and x >= 0:
        if x == 0:
            n[(4,float("-inf"))] += 1
        else:
            n[(4,Fraction(y,x))] += 1

fracs = sorted(n.keys())


LE_dict = {}

running_total = 0
for p in fracs:
    running_total += n[p]
    LE_dict[p] = running_total

def LE(p):
    if p[0] > 4:
        return LE_dict[(5,0)]
    return LE_dict[p]

def L(p):
    if p[0] > 4:
        return LE((5,0)) - n[(5,0)]
    return LE(p) - n[p]

nL_dict = {}

running_total = 0
for q,f in fracs:
    running_total += n[(q,f)]*L((q+2,f))
    nL_dict[(q,f)] = running_total

def nL(p):
    if p[0] > 4:
        return nL_dict[(5,0)]
    return nL_dict[p]

ans = 0

for q,f in fracs:
    if q > 2:
        break
    ans += n[(q,f)] * (nL((q+2,f)) - nL((q,f)) - n[(q+2,f)]*L((q+4,f)))
    ans -= n[(q,f)]*LE((q+2,f))* (L((q+2,f)) - LE((q,f)))

print("Answer: ", ans)
print("Time: ", time() - start)

#solution: 333333208685971546
