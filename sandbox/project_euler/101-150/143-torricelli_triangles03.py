from time import time
from math import gcd

t11=time()
def gen120t(lim):
    lms=int((lim)**0.5)
    d1,d2={},{}
    for j in range(1,lms+1):
        for i in range(j+1,lms+1):
            if (i-j)%3 and gcd(i,j)==1:
                p,q=i*i-j*j,2*i*j+j*j
                if p+q > lim:
                    break
                k=1
                while k*(p+q) <= lim:
                    d1[k*p,k*q],d1[k*q,k*p]=1,1
                    if k*p in d2:
                        d2[k*p].append(k*q)
                    else:
                        d2[k*p]=[k*q]
                    k+=1
    return d1,d2

def addt(d1,d2):
    dsum={}
    for p,q in d1:
        if q not in d2:
            continue
        for r in d2[q]:
            if p+q+r > lim:
                continue
            if (p,r) in d1 or (r,p) in d1:
                dsum[p+q+r]=1
                break
    return dsum

lim=120000
d1,d2=gen120t(lim)
sums=sum(addt(d1,d2))
print("\n\nSum is ",sums)
print ("Time taken ",time()-t11)
################################################################################
#solution: 30758397
################################################################################
