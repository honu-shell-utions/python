################################################################################
## Pandigital multiples
## Problem 38
## Take the number 192 and multiply it by each of 1, 2, and 3:
##
## 192 × 1 = 192
## 192 × 2 = 384
## 192 × 3 = 576
## By concatenating each product we get the 1 to 9 pandigital,
## 192384576. We will call 192384576 the concatenated product of
## 192 and (1,2,3)
##
## The same can be achieved by starting with 9 and multiplying by
##1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is
## the concatenated product of 9 and (1,2,3,4,5).
##
## What is the largest 1 to 9 pandigital 9-digit number that can
## be formed as the concatenated product of an integer with (1,2, ... , n)
## where n > 1?
################################################################################
def makeCandidate(num,digits):
    numStr = str(num)
    buildStr = ''
    for i in range(1,digits+1):
        buildStr += str(num*i)
    return(buildStr)
################################################################################        
def isPan(num,digits):
    digitString = '123456789'
    testMe = makeCandidate(num,digits)
    lenOfTestMe = len(testMe)   
    if lenOfTestMe != 9:
        return False   
    for i in range(lenOfTestMe):       
        if testMe[i] in digitString:
            digitString = digitString.replace(testMe[i],'x')
        else:
            return False       
    return True
################################################################################
for i in range(1,10_000):
    for j in range(1,10):       
        if(isPan(i,j)):
            print('Number to test:',i,'Values of n: 1 to',j,'Result:',makeCandidate(i,j))
################################################################################
#solution: 932718654
################################################################################
