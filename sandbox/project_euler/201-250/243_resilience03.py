#-------------------------------------------------------------------------------
from sympy import prime, totient
#-------------------------------------------------------------------------------
def res(n):
    return totient(n)/(n-1)
#-------------------------------------------------------------------------------
antiprime = 2
prev = 0
p = 2
while True:
    prev = antiprime
    antiprime *= prime(p)
    if res(antiprime) < 15499/94744:
        antiprime = prev
        break
    p += 1
    
k = 1
while res(antiprime * k) >= 15499/94744:
    k += 1
    
print(antiprime * k)
#-------------------------------------------------------------------------------
