###########################################################################
# Digit fifth powers
# Problem 30
# There are only three numbers that can be written as the sum of fourth powers
# of their digits: (as 1 = 1^4 is not a sum it is not included)

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers
# of their digits.
# 
###########################################################################
import numpy as np
###########################################################################
def solution():
    numDigits = 5
    power = 5
    solutionSet = set()

    placeValue = np.zeros(numDigits)
    for i in range(numDigits):
        placeValue[i] = int(10**(numDigits-i-1))   
    
    digits = np.zeros(numDigits)

    for d1 in range(1,10):
        for d2 in range(0,10):
            for d3 in range(0,10):
                for d4 in range(0,10):
                    for d5 in range(0,10):
                        digits[0] = d1
                        digits[1] = d2
                        digits[2] = d3
                        digits[3] = d4
                        digits[4] = d5
                        powerDigits = digits**power
                        numValue = digits*placeValue
                        if sum(powerDigits) == int(sum(numValue)):
                            solutionSet.add(int(sum(numValue)))
                
    return(sorted(solutionSet))
###########################################################################
print('-----------------------')
print(solution())
print('Sum:',sum(solution()))
print('-----------------------')
#443839
###########################################################################












