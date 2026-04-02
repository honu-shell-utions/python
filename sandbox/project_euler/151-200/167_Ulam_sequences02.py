from time import time

start=time()
result=0

def U(a,b,n):
    U=[a,b]
    UC1={a+b}
    UC2=set()
    
    for z in range(n-2):
        c=U[-1]  
        for u1 in U:
            if  u1!=c:
                if u1+c not in UC2: UC1.add(u1+c)
                elif u1+c in UC1: UC1.remove(u1+c)
                UC2.add(u1+c) 
        num=min(UC1)
        UC1.remove(num)
        U.append(num)

    return  U

periods=[0,0,32,26,444,1628,5906,80,126960,380882,2097152]
diffs=[0,0,126,126,1778,6510,23622,510,507842,1523526,8388606]

goal=10**11
for n in range(8,11):
    i=2*n+1
    steps=goal//periods[n]
    initial=goal%periods[n]
    print(i,initial)
    l=U(2,i,initial+1)
    vi=l[initial-1]
    vf=vi+steps*diffs[n]
    print(n,vf)
    result+=vf
            
stop = time()

print(f'Result: {result}')
print(f'Time: {stop - start:4e}s')
# 3916160068885
