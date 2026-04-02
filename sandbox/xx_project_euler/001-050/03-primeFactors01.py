##################################################################################
#jim mccleery, november, 2021
##################################################################################
##Largest prime factor 
##Problem 3
##The prime factors of 13195 are 5, 7, 13 and 29.
##
##What is the largest prime factor of the number 600851475143 ?
##################################################################################
def factors(num):
    factorList = []
    for i in range(1,num+1):
        if num % i == 0:
            factorList.append(i)
    return factorList
##################################################################################
def getPrimeFactors(n):
    factorList = []
    fList = factors(n)
    if len(fList) == 2:
        factorList.append(fList[1])
        return factorList
    
    flag = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            if flag:
                factorList.append(i)
            flag = False
            n /= i
        else:
            flag = True
            i += 1

    if max(factorList) != n:
        factorList.append(int(n))
    
    return factorList
##################################################################################
print(getPrimeFactors(600851475143))
##################################################################################
#solution: 6857
