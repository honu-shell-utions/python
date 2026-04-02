################################################################################
# 50-consecutivePrimesSum.py
#
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13  This is the longest sum of consecutive primes that
# adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?
#
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
def getNextPrime(num):
    t = 1
    while True:
        if isPrime(num+t):
            return num+t
        else:
            t += 1      
################################################################################
possibleSolutions = []

for i in range(1_000):
    counter = 1
    startingPrime = currentPrime = getNextPrime(i)
    total = startingPrime
    while total < 1_000_000:
        currentPrime = getNextPrime(currentPrime)
        counter += 1
        total += currentPrime
        if isPrime(total):
            possibleSolutions.append([counter,total])

max = 0
for i in range(len(possibleSolutions)):
    currentSolution = possibleSolutions[i]
    if currentSolution[0] > max:
        count = currentSolution[0]
        total = currentSolution[1]
        max = count
        
print(count,total)
################################################################################
#solution: 997651
################################################################################
