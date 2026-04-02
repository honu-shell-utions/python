################################################################################
##Distinct primes factors 
##Problem 47
##The first two consecutive numbers to have
##two distinct prime factors are:
##
##14 = 2 × 7
##15 = 3 × 5
##
##The first three consecutive numbers to have
##three distinct prime factors are:
##
##644 = 2² × 7 × 23
##645 = 3 × 5 × 43
##646 = 2 × 17 × 19.
##
##Find the first four consecutive integers to have four
##distinct prime factors each. What is the first of these numbers?
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
################################################################################
START = 100
STOP = 1_000_000
targetNumDigits = 4
firstHit = -1

solutionList = []
for i in range(START,STOP):
    primeList = []
    for j in range(2,1_000):
        if i % j == 0 and isPrime(j):
            primeList.append(j)
    solutionList.append([i,primeList])

for i in range(len(solutionList)-targetNumDigits+1):
    allGood = False
    for j in range(targetNumDigits):
        allGood = len(solutionList[i+j][1]) == targetNumDigits
        if not allGood:
            break
    if allGood:
        firstHit = i+j - targetNumDigits + 1
        break

if allGood:
    for i in range(targetNumDigits):
        print(solutionList[i+firstHit])
else:
    print("No solution.")

################################################################################
#solution: 134043
################################################################################
