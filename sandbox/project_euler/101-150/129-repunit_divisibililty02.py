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
def A(n):
    if gcd(n, 10) != 1:
        return 0
    x = 1
    k = 1
    while x != 0:
        x = (x * 10 + 1) % n
        k += 1
    return k
################################################################################
limit = 1000001
n = limit

while A(n) < limit:
    n += 2

print(n)
################################################################################
#solution: 1000023
################################################################################
