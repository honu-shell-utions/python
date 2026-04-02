from time import time
from math import gcd

def sum_real_divisors():
    temp = 0
    for i in range(1,limit+1):
        temp += (limit//i)*i
    return temp

def sum_complex_divisors():
    temp = 0
    a = 1
    while (a*a < limit):
        for b in range(1,a+1):
            if gcd(a,b) == 1:
                mag = a*a + b*b
                val = 2*(a+b)
                if a == b:
                    val = 2
                j = 1
                while mag*j <= limit:
                    temp += (j*val*(limit//(mag*j)))
                    j += 1
        a += 1
    return temp

go = time()
limit = 10**8
#find real solutions
grand_total = sum_real_divisors()

#now find the complex solutions
grand_total += sum_complex_divisors()

print(f'Limit = {limit}, total = {grand_total}, run-time = {round(time()-go,2)} seconds.')

# 10: 161
# 100: 16749
# 1000: 1752541
# 10000: 178231226
# 100000: 17924657155
# solution: 17971254122360635

