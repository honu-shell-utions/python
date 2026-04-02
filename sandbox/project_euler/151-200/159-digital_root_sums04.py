from math import isqrt

def mdrs(N):
    def drs(n):
        return (n-1)%9+1
          
    m = [drs(i) for i in range(0,1+N)]   
          
    for x in range(2,isqrt(N)+1):
        Q = m.copy()
        s = x*x
        v = 2*m[x]
        while s <= N:
            if v > m[s]: Q[s] = v
            s,v = s*x,v+m[x]    
        m=Q       

    R = m.copy()
    for x in range(2,isqrt(N)+1):
        Q = R.copy()
        for y in range(x+1, N//x+1):
           s,v = x*y, m[x]+R[y]
           if v > R[s] : Q[s] = v
        R = Q

    return R

     
print(sum(mdrs(999999)[2:]))
