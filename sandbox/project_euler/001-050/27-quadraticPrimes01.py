##Quadratic primes
##Problem 27
##Euler discovered the remarkable quadratic formula:
##
##n^2+n+41
##
##It turns out that the formula will produce 40 primes for
##the consecutive integer values 0≤n≤39. However, when 
##n=40, 40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when 
##n=41, 41^2+41+41 is clearly divisible by 41.
##
##The incredible formula n^2−79n+1601
##was discovered, which produces 80 primes for the consecutive values 
##0 ≤ n ≤ 79.
##
##The product of the coefficients, −79 and 1601, is −126479.
##
##Considering quadratics of the form: n^2+an+b, where |a|<1000 and 
##|b|≤1000 where |n| is the modulus/absolute value of n e.g. |11|=11
##and |−4|=4
##
##Find the product of the coefficients, a and b, for the quadratic
##expression that produces the maximum number of primes for consecutive values of 
##n, starting with n = 0.
## jim mccleery, november, 2021
##################################################################################
import math
from sympy import isprime
##################################################################################
def eulers_formula(n,a,b):
    return(n**2+a*n+b)
##################################################################################
maxNumOfPrimes = 0
for a in range(-999,1001):
    for b in range(-999,1001):
        n = 0
        while True:
            result = eulers_formula(n,a,b)
            if isprime(result):
                n += 1
                if a == 1 and b == 41:
                    print(n,a,b,result)
            else:
                break
        if n > maxNumOfPrimes:
            maxNumOfPrimes = n
            keepA = a
            keepB = b

print(maxNumOfPrimes,keepA*keepB)
#Solution: -59231
##################################################################################
