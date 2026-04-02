################################################################################
## Counting summations
## Problem 76
## It is possible to write five as a sum in exactly six different ways:
##
## 4 + 1
## 3 + 2
## 3 + 1 + 1
## 2 + 2 + 1
## 2 + 1 + 1 + 1
## 1 + 1 + 1 + 1 + 1
##
## How many different ways can one hundred be written as a sum of at
## least two positive integers?
################################################################################
import random
import time
################################################################################
def findTotal(numList):
    total = 0
    factor = len(numList)
    for i in range(len(numList)):
        total += numList[i]*factor
        factor -= 1

    return total
################################################################################
def makeSolList(num):
    solList = []
    start = time.time()
    while True:
        total = num
        testList = [0] * (num - 1)

        for i in range(0,num - 2):
            temp = total // (num - i - 1)
            testList[i] = random.randint(0,temp)
            total = total - testList[i] * (num - i - 1)
        
        testList[num - 2] = total
    
        if findTotal(testList) == num and testList not in solList:           
            solList.append(testList)
            
        if time.time() - start > 15:
            start = time.time()
            print(len(solList))


################################################################################
print(makeSolList(6))
################################################################################
#solution: 190_569_291
################################################################################
