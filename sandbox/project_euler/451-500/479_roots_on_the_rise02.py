limit = 10**6
limit = 10**3
MOD = 10**9+7


def sum_k(k):
    return ((pow(k, 2, MOD) - 1)*((pow(1-k**2, limit, MOD) - 1) % MOD)*pow(pow(k, 2, MOD), MOD-2, MOD)) % MOD

s = 0
for i in range(2, limit+1):
    s = (s + sum_k(i)) % MOD
    
print (s % MOD)

# 191541795
