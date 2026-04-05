#-------------------------------------------------------------------------------
## Circular Logic
## Problem 209
## A k-input binary truth table is a map from k input bits
## (binary digits, 0 [false] or 1 [true]) to 1 output bit.
## For example, the 2-input binary truth tables for the
## logical AND and XOR functions are:
## 
## x	y	x AND y
## 0	0	0
## 0	1	0
## 1	0	0
## 1	1	1
## 
## x	y	x XOR y
## 0	0	0
## 0	1	1
## 1	0	1
## 1	1	0
## 
## How many 6-input binary truth tables, τ, satisfy the formula
## 
## τ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0
## 
## for all 6-bit inputs (a, b, c, d, e, f)?
#-------------------------------------------------------------------------------
from math import factorial as fact
def f(a,b,c,d,e,f):
    return (b,c,d,e,f, int(a!=(b and c)))

abcdef=[ (a,b,c,d,e,f) for a in [0,1] for b in [0,1] for c in [0,1] for d in [0,1] for e in [0,1] for f in [0,1] ]
cyclelist=[]

for x in abcdef:
    l=set([])
    while x not in l:
        l.add(x)
        x=f(*x)
    if l not in cyclelist:
        cyclelist.append(l)
for x in cyclelist:
    print(len(x))

res=1*18*18*4*3
s=0
for k in range(1,23):
    s+=fact(46-k-1)/(fact(46-k-1-k)*fact(k))
    s+=2*fact(46-k-1)/(fact(46-k-1-k+1)*fact(k-1))
s+=3
print (int(res*s))

#-------------------------------------------------------------------------------
# solution: 15964587728784 
#-------------------------------------------------------------------------------
