#  -----------------------------------------------------------------------------
#  Clock sequence
#  Problem 506
#  Consider the infinite repeating sequence of digits:
#  1234321234321234321...
#  
#  Amazingly, you can break this sequence of digits into a sequence
#  of integers such that the sum of the digits in the n'th value is n.
#  
#  The sequence goes as follows:
#  1, 2, 3, 4, 32, 123, 43, 2123, 432, 1234, 32123, ...
#  
#  Let vn be the n'th value in this sequence. For example,
#  v2 = 2, v5 = 32 and v11 = 32123.
#  
#  Let S(n) be v1 + v2 + ... + vn.
#  
#  For example, S(11) = 36120, and S(1000) mod 123454321 = 18232686.
#  
#  Find S(10^14) mod 123454321.
#  
#  https://projecteuler.net/problem=506
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def seq_gen():
    while True:
        for c in "123432":
            yield c 
#  -----------------------------------------------------------------------------
def S(n):
    total = 0
    s_gen = seq_gen()
    for k in range(1,n+1):
        sum_digits = 0
        build = ''
        while k != sum_digits:
            digit_chr = next(s_gen)
            build += digit_chr
            sum_digits += int(digit_chr)
        total += (int(build) % MOD)
    return total % MOD
#  -----------------------------------------------------------------------------
MOD = 123454321
for exp in range(1,18):
    start = time()
    if exp == 14:
        print('-'*50)
    print(f'Solution for n = 10^{exp:2}: {S(10**exp):10}, Run-Time: {time()-start}')
    if exp == 14:
        print('-'*50)
#  -----------------------------------------------------------------------------
#  sol 10^1  3997
#  sol 10^2  9291482
#  sol 10^3  18232686
#  sol 10^4  107644726
#  sol 10^5  14130558
#  sol 10^6  66623446
#  sol 10^7  97735042
#  sol 10^8  38488039
#  sol 10^9  63289614
#  sol 10^10 64396722
#  sol 10^11 75467802
#  sol 10^12 62724281
#  sol 10^13 58743392
#  ------------------
#  sol 10^14 18934502
#  ------------------
#  sol 10^15 114662886
#  sol 10^16 84312158
#  sol 10^17 55582398
#  -----------------------------------------------------------------------------
