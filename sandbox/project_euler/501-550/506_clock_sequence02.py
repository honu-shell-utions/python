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
def euler_506(target):
    total = 0
    for residue, a0, b in cases:
        n = (target - residue)//15
        m = 10**6
        an = a0*pow(m,n,MOD) + b*(pow(m,n,MOD)-1)*pow(m-1,-1,MOD)
        total += (m*an - n*b - a0)*pow(m-1,-1, MOD)
    return total % MOD
#  -----------------------------------------------------------------------------
cases = [(0,0,123432),(1,1,234321),(2,2,343212),(3,3,432123),
         (4,4,321234),(5,32,123432),(6,123,432123),(7,43,212343),
         (8,2123,432123),(9,432,123432),(10,1234,321234),
         (11,32123,432123),(12,43212,343212),(13,34321,234321),
         (14,23432,123432)]

MOD = 123454321
for exp in range(1,17):
    start = time()
    if exp == 14:
        print('-'*50)
    print(f'Solution for n = 10^{exp:2}: {euler_506(10**exp):10}, Run-Time: {time()-start}')
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
#  -----------------------------------------------------------------------------
