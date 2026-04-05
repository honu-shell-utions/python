##################################################################################
#jim mccleery, november, 2021
import math
##################################################################################
def getPrimeFactors(n):
    original = n
    baseList = []
    powerList = []
    flag = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            if flag:
                baseList.append(i)
            flag = False
            n /= i
        else:
            flag = True
            i += 1

    if max(baseList) != n:
        baseList.append(int(n))

    for i in range(len(baseList)):
        powerCounter = 0
        while original % baseList[i] == 0:
            powerCounter += 1
            original = original/baseList[i]
        powerList.append(powerCounter)
    
    for i in range(len(baseList)):
        print(baseList[i],'^',powerList[i],end='')
        if i < len(baseList)-1:
            print(' * ',end='')
        
##################################################################################
getPrimeFactors(math.factorial(10))
##################################################################################
