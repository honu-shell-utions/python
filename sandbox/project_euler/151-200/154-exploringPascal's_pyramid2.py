from time import time

def euler154(level=200000,divisor=12):
    go = time()
    nsum=0
    nfac2=facpfac(level,2)
    nfac5=facpfac(level,5)    
    facs2=[facpfac(x,2) for x in range(level+1)]
    facs5=[facpfac(x,5) for x in range(level+1)]
    
    for p in range(level//2+1):
        nf5_pf5=nfac5-facs5[p]
        nf2_pf2=nfac2-facs2[p]
        for q in range(min(p, level-2*p)+1):
            r=level-p-q           
            if nf5_pf5-facs5[q]-facs5[r]<divisor:
                continue
            if nf2_pf2-facs2[q]-facs2[r]<divisor:
                continue
            if p==q or p==r:
                nsum+=3
                continue
            nsum+=6
    print (nsum)
    print(time()-go)
    
def facpfac(n,prime):
    """returns exponents of 2 and 5 as factors of n!!"""
    exponent=0
    power=1
    delta=10
    while delta>0:
        delta=n//prime**power
        exponent+=delta
        power+=1
    return exponent

euler154()
# 479742450
