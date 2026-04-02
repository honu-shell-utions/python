#-------------------------------------------------------------------------------
## Cardano Triplets
## Problem 251
## A triplet of positive integers (a,b,c) is called a
## Cardano Triplet if it satisfies the condition:
## 
## see graphic
## 
## For example, (2,1,5) is a Cardano Triplet.
## 
## There exist 149 Cardano Triplets for which a+b+c ≤ 1000.
## 
## Find how many Cardano Triplets exist such that a+b+c ≤ 110,000,000.
#-------------------------------------------------------------------------------
from sympy import divisors
from time import time
#-------------------------------------------------------------------------------
start=time()
result=0
nMax=110*10**6
#nMax=10**3

sols=set()
for a9 in range(0,(nMax//9+1)//2):
    for a1 in [2,5,8]:
        a=9*a9+a1
        if a<nMax-1:
            v1=(((8*a+15)*a+6)*a-1)//27
            bopt=[(v1//(d*d),d) for d in divisors(v1) if v1%(d*d)== 0]
            sols.update({(a,b,c) for (b,c) in bopt if a+b+c<=nMax})
    
print(f'Solution: {len(sols)}, Run-Time: {time() - start} ')
#-------------------------------------------------------------------------------
# solution: 18946051
#-------------------------------------------------------------------------------
