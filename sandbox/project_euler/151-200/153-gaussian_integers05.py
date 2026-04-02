from math import gcd, isqrt
from time import time

limit = 10**3
go = time()

sigma = limit*(limit+1)//2
for n in range(1,limit//2 + 1):
        sigma += n*(limit//n - 1)
        sigma += 2*n*(limit//(2*n))

for a in range(2,isqrt(limit)+1):
    for b in range(1,a+1):
        if gcd(a,b) > 1:
            continue
        c = a**2 + b**2
        if c > limit:
            break
        k = 1
        while k*c <= limit:
            sigma += 2*k*(a+b)*(limit//(k*c))
            k += 1
                  
print(sigma)
print(round(time()-go))

# 10: 161
# 100: 16749
# 1000: 1752541
# 10000: 178231226
# 100000: 17924657155
# solution: 17971254122360635
