#  -----------------------------------------------------------------------------
#  Nth digit of Reciprocals
#  Problem 820
#  https://projecteuler.net/problem=820
#  -----------------------------------------------------------------------------
from fractions import Fraction
from time import time
#  -----------------------------------------------------------------------------
def find_rat_pat(den,base=10):
    r = Fraction(1,den)
    
    #get integer portion
    whole, fractional = divmod(r, 1)
    whole_digits = []
    while whole:
        whole, digit = divmod(whole, base)
        whole_digits.append(digit)

    #get fractional portion
    fractional_digits = []
    seen = {}
    while fractional not in seen:
        seen[fractional] = len(fractional_digits)
        digit, fractional = divmod(fractional * base, 1)
        fractional_digits.append(digit)
    s = seen[fractional]
    return [whole_digits,
            fractional_digits[:s],
            fractional_digits[s:] if fractional else []]
#  -----------------------------------------------------------------------------
def d(pos,x):
    whole,front,rep = find_rat_pat(x)
    len_front = len(front)
    len_rep = len(rep)
    tmp = pos - len_front
    if len_front >= pos:
        return front[pos-1]
    elif len_rep == 0:
        return 0
    else:
        idx = (tmp % len_rep) - 1
        return rep[idx]
#  -----------------------------------------------------------------------------
def S(n):
    total = 0
    for k in range(1,n+1):
        total += d(n,k)
    return total
#  -----------------------------------------------------------------------------
for n in [7,10**2,10**3,10**5,10**7]:
    start = time()
    print(f'Solution for n = {n:8}, {S(n):9}, Run-Time: {time()-start:8.2f}')
#  -----------------------------------------------------------------------------
#  solution: 44967734
#  -----------------------------------------------------------------------------
