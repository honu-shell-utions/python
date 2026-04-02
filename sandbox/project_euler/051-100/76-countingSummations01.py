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
    counter = 0
    while True:
        testList = [0] * (num - 1)
        for i in range(len(testList)):
            testList[i] = random.randint(0,num)
    
        if findTotal(testList) == num and testList not in solList:
            print(testList)
            solList.append(testList)
            counter += 1
            if counter == 6:
                return solList

################################################################################
print(makeSolList(10))

################################################################################
#solution: 190569291
################################################################################
