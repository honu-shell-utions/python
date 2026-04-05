from time import time

def euler_410(N):
    nums = [0] + (N//2)*[0, 1]
    for p in range(3, N+1):
        if nums[p] == 0:
            for i in range(p, N+1, p):
                nums[i] += 1
    cnt = 0
    for k in range(2, N+1):
        numdivs = 2**(nums[k] - 1)
        k2 = 2*k
        if k % 2 == 0:
            cnt += (((R + k)//k2) * ((X + k)//k2) + (R//k2) * (X//k2)) * numdivs
        else:
            cnt += (R//k) * (X//k) * numdivs
    return cnt

for R,X in [(1,5),(2,10),(10,100),(10**8,10**9)]:
    start = time()
    N = min(R,X)
    sol = 2*R*X + 4*euler_410(N)
    if R == 10**8:
        sol *= 2
    print(f'Solution: {sol:19}, Run-Time: {time()-start:0.3f}')

# solution: 799999783589946560
