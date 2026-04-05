from math import factorial

def binomial(n, k):
    return factorial(n) // factorial(n-k) // factorial(k)

def ds_count(n):
    m = (10 ** n - 1) // 9
    return sum([(m * 2 * k * (n * binomial(n-2+k, k) - binomial(n, 2))) // n for k in range(1, 10)])

print(ds_count(2020) % 10 ** 16)
