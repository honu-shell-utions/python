from math import isqrt

def small_factor_generator(n):
    for i in range(2,1+isqrt(n)):
        if n%i == 0: yield i

def problem088(n=12000):
    best = [0] * (n+1)
    sum_decomp = {}
    for i in range(2,2*n+1):
        sum_decomp[i] = set([(1, i)])
        for k in small_factor_generator(i):
            for a,b in sum_decomp[i/k]:
                sum_decomp[i].add((a+1, b+k))
                dex = i+(a+1)-(b+k)
                if dex <= n and best[dex] == 0:
                    best[dex] = i
        print(i,sum_decomp)
        print('best',best)
        print()
    return sum(set(best))

print(problem088(13))
