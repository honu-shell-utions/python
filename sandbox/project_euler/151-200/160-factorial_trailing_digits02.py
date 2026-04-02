
N = 10**12
D = 10**5

def factorial_no5s(n):
    f = 1
    for i in range(2, n+1):
        if i % 5 != 0:
            f *= i
    return f

def f(n): # direct computation for small n
    f = 1
    while n > 1:
        f *= n
        while f % 10 == 0:
            f //= 10
        f %= D
        n -= 1
    return f

n, m = N, 0
while n % 100 == 0:
    m += n // 100
    n //= 5

h = factorial_no5s(100) // (2**20)

print(f(n) * pow(h, m, D) % D)  # Answer: 16576
