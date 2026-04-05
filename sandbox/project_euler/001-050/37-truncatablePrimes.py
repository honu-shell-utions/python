##Truncatable primes
## 
##Problem 37
##The number 3797 has an interesting property. Being prime itself,
##it is possible to continuously remove digits from left to right,
##and remain prime at each stage: 3797, 797, 97, and 7. Similarly
##we can work from right to left: 3797, 379, 37, and 3.
##
##Find the sum of the only eleven primes that are both truncatable
##from left to right and right to left.
##
##NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
import math
##################################################################################
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
##################################################################################
def chopper(num):
    strnum1 = str(num)
    strnum2 = str(num)
    while len(strnum1) >= 1:
        if not isPrime(int(strnum1)):
            return(False)
        if not isPrime(int(strnum2)):
            return(False)
        strnum1 = strnum1[1:]
        strnum2 = strnum2[:len(strnum2)-1]
    return(True)
        
##################################################################################
counter = 0
solutions = []
i = 11
while counter < 11:
    if isPrime(i):
        if chopper(i):
            solutions.append(i)
            counter += 1
    i += 2
            
print('Number of Truncatable Primes',counter)
print('List of Trunctable Primes',solutions)
print('Sum of Trunctable Primes',sum(solutions))
##################################################################################
#solution: 748317
##################################################################################
