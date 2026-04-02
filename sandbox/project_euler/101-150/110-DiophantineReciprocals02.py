from sympy import primerange

def next(exponents):
    i = 0
    while i < len(exponents) and exponents[i] == 3:
        i += 1
    if i < len(exponents):
        n = exponents[i]
        while i >= 0:
            exponents[i] = n + 1
            i -= 1
    else:
        return None
    return exponents

def getn(primes, exponents):
    num = 1
    for i in range(len(exponents)):
        num *= pow(primes[i], exponents[i])
    return num

def ways(exponents):
    i = 1
    for e in exponents:
        i *= 2 * e + 1
    return (i + 1) / 2

primes = list(primerange(2,100))
exponents = [0] * len(primes)

nmin = 10**100
while exponents:
    num = getn(primes, exponents)
    if num < nmin:
        w = ways(exponents)
        if w > 4*10**6:
            nmin = num
    exponents = next(exponents)

print(nmin)
# 9350130049860600
