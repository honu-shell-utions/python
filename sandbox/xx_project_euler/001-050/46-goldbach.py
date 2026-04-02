################################################################################
##Goldbach's other conjecture 
##Problem 46
##It was proposed by Christian Goldbach that every
##odd composite number can be written as the sum
##of a prime and twice a square.
##
##9 = 7 + 2×1^2
##15 = 7 + 2×2^2
##21 = 3 + 2×3^2
##25 = 7 + 2×3^2
##27 = 19 + 2×2^2
##33 = 31 + 2×1^2
##
##It turns out that the conjecture was false.
##
##What is the smallest odd composite that cannot
##be written as the sum of a prime and twice a square?
################################################################################
import math
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
##################################################################################
START = 35
STOP = 6_000

solutionList = []
solutionSet = set()
for i in range(START,STOP,2):
    if not isPrime(i):
        b = 1
        temp = i-2*b**2
        while temp > 0:
            if isPrime(temp):
                #solutionList.append([i,temp,b])
                solutionSet.add(i)
            b += 1
            temp = i-2*b**2

for i in range(START,STOP,2):
    if i not in solutionSet and not isPrime(i):
        solution = i
        break

print('Solution:',solution)
################################################################################
#solution: 5777 
################################################################################
