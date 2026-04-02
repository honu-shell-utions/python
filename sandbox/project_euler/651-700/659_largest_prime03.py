from time import time

def euler_659(L):
    f = [4*x**2+1 for x in range(L+1)]
    largest_prime = [0]*(L+1)

    def sieve(start, fx):
        j = start % fx
        while j <= L:
            if f[j] % fx == 0:
                largest_prime[j] = max(largest_prime[j], fx)
                while f[j] % fx == 0:
                    f[j] //= fx
            j += fx

    for x in range(1, L+1):
        if f[x] > 1:
            sieve(-x, f[x])
            sieve(x, f[x])

    return (sum(largest_prime) % 10**18)
#  -----------------------------------------------------------------------------
for exp in range(2,8):
    start = time()
    limit = 10**exp
    print(f'For n = 10^{exp}: {euler_659(limit):>18}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  10**2 --> 433752
#  10**3 --> 299015732
#  10**4 --> 223215627804
#  10**5 --> 178688812032788
#  10**6 --> 148687122056813880
#  10**7 --> 238518915714422000
#  -----------------------------------------------------------------------------
