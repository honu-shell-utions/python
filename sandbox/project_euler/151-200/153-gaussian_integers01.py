from time import time
from math import gcd
from sympy import divisors

def sum_real_divisors():
    temp = 0
    for i in range(1,limit+1):
        temp += sum(divisors(i))
    return temp

def sum_complex_divisors(n):
    temp = 0
    for a in range(1,n):
        for b in range(1,n):
            mag = a**2 + b**2
            if mag % 4 == 3 or mag > n**2:
                break
            q = n*gcd(a,b)/(a**2 + b**2)
            if q % 1 == 0:
                temp += 2*a
    return temp

go = time()
limit = 10**3
#find real solutions
grand_total = sum_real_divisors()

#now find the complex solutions
for n in range(1,limit+1):
    grand_total += sum_complex_divisors(n)

print(f'Limit = {limit}, total = {grand_total}, run-time = {round(time()-go,2)} seconds.')

# 10: 161
# 100: 16749
# 1000: 1752541
# 10000: 178231226
# 100000: 17924657155
# solution: 17971254122360635
