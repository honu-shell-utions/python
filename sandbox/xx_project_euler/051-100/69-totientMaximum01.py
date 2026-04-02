################################################################################
##Totient maximum
##Problem 69
##Euler's Totient function, φ(n) [sometimes called the phi function],
##is used to determine the number of numbers less than n which are
##relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
##all less than nine and relatively prime to nine, φ(9)=6.
##
##  n	Relatively Prime	φ(n)	n/φ(n)
##  2	1	         1	2
##  3	1,2	         2	1.5
##  4	1,3	         2	2
##  5	1,2,3,4	         4	1.25
##  6	1,5	         2	3   (maximum)
##  7	1,2,3,4,5,6       6	1.1666...
##  8	1,3,5,7	         4	2
##  9	1,2,4,5,7,8       6	1.5
## 10	1,3,7,9	         4	2.5
##
##It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
##
##Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
################################################################################
from fractions import Fraction
import time
################################################################################
def areRelPrime(a,b):
    f = Fraction(a,b)
    if b == f.denominator:
        return True
    else:
        return False
################################################################################
MAX = 10
temp = []
maxPhi = -1
maxN = -1
start = time.time()
for n in range(2,MAX+1):
    temp.clear()
    temp.append(n)
    for j in range(1,n):
        if areRelPrime(j,n):
            temp.append(j)
            
    phi = temp[0]/(len(temp)-1)
    if phi > maxPhi:
        maxPhi = phi
        maxN = n        
    print(temp[0],':',temp[1:],',',len(temp)-1,',',phi)
        
end = time.time()
print('Max Phi of:',maxPhi,'for n =',maxN,'Run time:',end-start)
################################################################################
#solution: 510510, but this version doesn't work for n = 10**6
################################################################################
