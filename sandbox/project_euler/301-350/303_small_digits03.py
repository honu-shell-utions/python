#  -----------------------------------------------------------------------------
#  Multiples with small digits
#  Problem 303
#  For a positive integer n, define f(n) as the least positive
#  multiple of n that, written in base 10, uses only digits ≤ 2.
#  
#  Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.
#  -----------------------------------------------------------------------------
from time import time
from itertools import product
#  -----------------------------------------------------------------------------
def digitCombos(n):
    gen = product(choices,repeat = n)
    return gen
#  -----------------------------------------------------------------------------
def f(div,n):
    gen = digitCombos(n)
    for dc in gen:
        num = int(''.join(dc))
        if num > 0 and num % div == 0:
            return num
#  -----------------------------------------------------------------------------    
def function_sum(div_max,n):
    tot = 0
    for div in range(1,div_max + 1):
        tot += f(div,n) // div
        if div % 100 == 0:
            print(f'{div:>10}\t{tot:>20}\t{round(time()-start,2):>6} seconds')
#  -----------------------------------------------------------------------------
start = time()
choices = ['0','1','2']           
function_sum(10**4, 20)
#  -----------------------------------------------------------------------------
