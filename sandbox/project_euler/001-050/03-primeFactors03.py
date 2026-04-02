##################################################################################
#jim mccleery, november, 2021, modified March, 2023
from sympy import factorint
from math import factorial
##################################################################################
def factor_n(n):
    fn = factorial(n)
    x = factorint(fn)
    print(f'Prime factorization of {n}! = {fn}.')
    for base,exp in x.items():
        if base == list(x)[-1]:
            print(base,'^',exp)
        else:     
            print(base,'^',exp,end=' * ')
    print('-'*70)
##################################################################################
for n in range(11):
    factor_n(n)
##################################################################################
