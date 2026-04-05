################################################################################
##Pandigital prime
##Problem 41
##We shall say that an n-digit number is pandigital if
##it makes use of all the digits 1 to n exactly once.
##For example, 2143 is a 4-digit pandigital and is also prime.
##What is the largest n-digit pandigital prime that exists?
import math
import itertools
################################################################################
def testThePerms(digitString):
    perms = itertools.permutations(digitString)
    permsLst = list(perms)
    permsLst.sort(reverse=True)
    candidates = [''.join(i) for i in permsLst]
    for i in candidates:
        if isPrime(int(i)):
            return(i)
    return(0)
################################################################################        
def isPrime(n):
    if n <= 1:   # one is not considered a prime number
        return False
    if n == 2:   # two is a prime number
        return True
    if n > 2 and n % 2 == 0:  # eliminate all even numbers greater than 2
        return False

    max_div = math.floor(math.sqrt(n))  # test up to the square root of n
    for i in range(3, 1 + max_div, 2):  # only need to check odd numbers
        if n % i == 0:
            return False
    return True
################################################################################
digitString = '123456789'
while len(digitString) > 1:
    result = testThePerms(digitString)
    if result == 0:
        digitString = digitString[0:len(digitString)-1]
    else:
        break
print(result)
################################################################################
#solution: 7652413
################################################################################
