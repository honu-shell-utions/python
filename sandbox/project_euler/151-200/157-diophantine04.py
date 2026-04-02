from math import gcd
from sympy import divisors


def f(n):
    divs = divisors(10**n)
    sol=0
    for a in divs:
        for b in divs:
            if b>=a and gcd(a,b)==1:
                p=(10**n*(a+b))//(a*b)
                sol+=len(divisors(p))
    return sol

print(sum(f(i) for i in range(1,10)))

