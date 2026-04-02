#  -----------------------------------------------------------------------------
#  Multiples with small digits
#  Problem 303
#  For a positive integer n, define f(n) as the least positive
#  multiple of n that, written in base 10, uses only digits ≤ 2.
#  
#  Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def has_allowed_digits(n):
    mult_n = n
    while True:
        temp = str(mult_n)
        if temp.count('1') + temp.count('2') + temp.count('0') == len(temp):
            return mult_n
        else:
            mult_n += n
#  -----------------------------------------------------------------------------
start = time()
limit = 10**4
total = 0
for n in range(1,limit + 1):
    total += has_allowed_digits(n)//n

print(f'Solution: {total}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 1111981904675169
#  -----------------------------------------------------------------------------
