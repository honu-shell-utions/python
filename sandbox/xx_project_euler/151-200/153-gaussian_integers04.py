from math import gcd, isqrt
from sympy import divisors
from time import time

LIMIT = 10**8
def sum_real_divisors():
    temp = 0
    for i in range(1,LIMIT+1):
        temp += sum(divisors(i))
    return temp

def euler153():
    int_sum = sum_real_divisors()
    complex_sum = 0   
    for a in range(1,isqrt(LIMIT) + 1):
        for b in range(1,LIMIT - a**2 +1):
            if gcd(a,b) == 1:
                mn_limit = LIMIT // (a*a+b*b)
                for m in range(1,mn_limit+1):
                    numNs = mn_limit // m
                    complex_sum += m*a*numNs

    print(int(int_sum + complex_sum*2))

go = time()
euler153()
print(round(time()-go))

# 10: 161
# 100: 16749
# 1000: 1752541
# 10000: 178231226
# 100000: 17924657155
# solution: 17971254122360635
