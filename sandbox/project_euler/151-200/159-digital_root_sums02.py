from math import isqrt

N = 1000000

D = {n: [] for n in range(2,N)}

for i in range(2, isqrt(N)+1):
    for j in range(i*i, N, i):
        D[j].append(i)
        
for n in range(2,N):
    a = n%9
    mdrs = a if a else 9
    if D[n]:
        for div in D[n]:
            mdrs = max(mdrs, D[div] + D[n//div])
    D[n] = mdrs

print(sum(D.values()))

# 14489159
