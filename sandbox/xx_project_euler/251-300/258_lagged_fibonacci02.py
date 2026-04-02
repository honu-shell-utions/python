from time import time
n = 2000
p = 20092010
t = 10**18

def mul(x, y):
    z = n * [0]
    for i in range(n):
        for j in range(n):
            if i + j >= n:
                z[i+j-n] = (z[i+j-n] + x[i] * y[j]) % p
                z[i+j-n+1] = (z[i+j-n+1] + x[i] * y[j]) % p
            else:
                z[i+j] = (z[i+j] + x[i] * y[j]) % p
    return z

def pow(m, n):
    if n == 1:
        return m
    if n % 2 == 0:
        mm = pow(m, n // 2)
        r = mul(mm, mm)
    else:
        r = mul(m, pow(m, n - 1))
    return r

start = time()
solution = sum(pow([0,1] + (n - 2) * [0], t)) % p

print(f'Solution: {solution}, Run-Time: {time()-start}')
## solution: 12747994
