from math import isqrt
limit = 10**6
s = [0, 0] + [i % 9 + 1 for i in range(1, limit-1)]

for n in range(2, len(s)):
    
    s[n] = max([s[i] + s[n // i] \
                for i in range(1, isqrt(n) + 1) \
                if n % i == 0])
print(sum(s))
