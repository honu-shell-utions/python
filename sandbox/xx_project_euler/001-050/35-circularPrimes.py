##Circular primes
##
##Problem 35

##The number, 197, is called a circular prime because all
##rotations of the digits: 197, 971, and 719, are themselves prime.
##
##There are thirteen such primes below 100:
##2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
##
##How many circular primes are there below one million?
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
def makeCircle(num):
    strNum = str(num)
    length = len(strNum)
    strNewList = list(strNum)
    for i in range(length):
        strNewList[i] = strNum[(i+1)%length]    
    strNew = "".join(strNewList)
    return(int(strNew))

##################################################################################
def makeListOfCircles(num):
    circleList = []
    result = makeCircle(num)
    circleList.append(result)
    for i in range(len(str(num))-1):
        result = makeCircle(result)
        circleList.append(result)

    return(circleList)
##################################################################################
solutionSet = set()
for i in range(2,1_000_000):
    if isPrime(i):
        currentList = makeListOfCircles(i)
        allPrime = True
        for j in range(len(currentList)):
            if not(isPrime(currentList[j])):
                allPrime = False           
        if allPrime:
            solutionSet.add(currentList[j])
                
print(len(solutionSet))
#solution: 55
##################################################################################
