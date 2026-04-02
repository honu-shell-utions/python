#  -----------------------------------------------------------------------------
#  Three similar triangles
#  Problem 299
#  -----------------------------------------------------------------------------
from math import gcd
#  -----------------------------------------------------------------------------
def incenter_case():
    count = 0
    for n in range(1,L//2):
      for m in range(1,n):
        if((m+n) % 2 == 0):
            continue
        if(gcd(m,n)!=1):
            continue
        b = n*n - m*m
        d = 2*n*m
        temp = b+d
        if b+d >= L:
            break
        if b == d:
            count += L//temp
        else:
            count += 2*(L//temp)
    return count
#  -----------------------------------------------------------------------------
def parallel_case():
    count = 0
    for n in range(1,L,2):
      for m in range(1,L):
        if gcd(m,n) != 1:
            continue
        g = 2*n*m
        a = n*n + 2*m*m
        b = g+a;
        if b > L//2:
            break;
        count += (L-1)//(2*b)
    return count

for L in [10**2,10**3,10**4,10**5,10**6,10**7,10**8]:
    print(f'Solution for L = {L}: {incenter_case() + parallel_case()}')
#  -----------------------------------------------------------------------------
#  solution: 549936643
#  -----------------------------------------------------------------------------
