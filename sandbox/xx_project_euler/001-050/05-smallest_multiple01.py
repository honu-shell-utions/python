#-------------------------------------------------------------------------------
#2520 is the smallest number that can be divided
#by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly
#divisible by all of the numbers from 1 to 20?
#-------------------------------------------------------------------------------
from sympy import factorint
#-------------------------------------------------------------------------------
def make_product(n):
    result = {}
    for k in range(1,n+1):
        kd = factorint(k)
        for key,val in kd.items():
            if key in result:
                result[key] = max(val,result[key])
            else:
                result[key] = val
    product = 1
    for key,val in result.items():
        product *= key**val
    return product
#-------------------------------------------------------------------------------
LIMIT = 100
for n in range(1,LIMIT+1):
    if n == 20:
        print('-'*70)
    print(f'Solution for n = {n:3}: {make_product(n)}')
    if n == 20:
        print('-'*70)
#-------------------------------------------------------------------------------        
#solution: 232792560
#-------------------------------------------------------------------------------
