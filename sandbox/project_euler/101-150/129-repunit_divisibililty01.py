################################################################################
##Repunit divisibility
##Problem 129
##A number consisting entirely of ones is called a repunit.
##We shall define R(k) to be a repunit of length k;
##for example, R(6) = 111111.
##
##Given that n is a positive integer and GCD(n, 10) = 1,
##it can be shown that there always exists a value, k, for
##which R(k) is divisible by n, and let A(n) be the least
##such value of k; for example, A(7) = 6 and A(41) = 5.
##
##The least value of n for which A(n) first exceeds ten is 17.
##
##Find the least value of n for which A(n) first exceeds one-million.
################################################################################
from math import gcd
################################################################################
def R(k):
    if k < 1:
        return 0
    x = 1
    while x < 10**(k-1):
        x = x * 10 + 1 
    return x
################################################################################
def A(n):
    for k in range(1,n+1):
        if gcd(n,10) == 1 and R(k) % n == 0:
            return k
    return -1      
################################################################################
n = 10001
while True:
    result = A(n)
    if result > 10000:
        print('\n\nA('+str(n)+')',result)
        break
    n += 2
################################################################################
#solution: 
################################################################################
