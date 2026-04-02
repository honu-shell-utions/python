import math
##################################################################################
def factors(num):
    factorList = []
    for i in range(1,num+1):
        if num % i == 0:
            factorList.append(i)
    return factorList
##################################################################################
def isPrime(testMe):
    if testMe != int(testMe) or testMe < 2:
        return False
    if len(factors(testMe)) == 2:
        return(True)
    else:
        return(False)       
##################################################################################
def primeList(num):
    allFactors = factors(num)
    primeFactors = []
    for i in range(len(allFactors)):
        if isPrime(allFactors[i]):
            primeFactors.append(allFactors[i])
    return(primeFactors)
##################################################################################
def expList(num):
    slots = []
    for i in range(0,num+1):
        slots.append(0)
    
    primes = primeList(num)
    for i in range(len(primes)):
        while num % primes[i] == 0:
            slots[primes[i]] += 1
            num /= primes[i]

    return(slots)
##################################################################################
def collectAllThePrimes(num):
    collectorList = expList(num)
    for i in range(num-1,0,-1):
        tmpList = expList(i)
        for j in range(0,len(tmpList)):
            if tmpList[j] > collectorList[j]:
                collectorList[j] = tmpList[j]
    return(collectorList)
##################################################################################
exponents = collectAllThePrimes(20)
total = 1
for i in range(1,len(exponents)):
    total *= i**exponents[i]
print(total)   
##################################################################################
#solution: 232792560
