################################################################################
# 49-primePermutations.py
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this
# sequence?
#
################################################################################
import math
################################################################################
def getThePermPrimes():
    permPrimes = []
    for i in range(1,10):
        for j in range(10):
            for k in range(10):
                for m in range(10):
                    tmp = str(i)+str(j)+str(k)+str(m)
                    if isPrime(int(tmp)):
                        permPrimes.append(int(tmp))
    return(permPrimes)
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
theDiff = 3330
theList = getThePermPrimes()
for i in range(len(theList)):
    n0 = theList[i]
    n1 = theList[i]+theDiff
    n2 = theList[i]+2*theDiff    
    if n1 in theList and n2 in theList:
        testThis = (sorted(str(n0)) == sorted(str(n1)) == sorted(str(n2)))
        if testThis:                                                  
            print(n0,n1,n2)

################################################################################
#solution: 296962999629
################################################################################
