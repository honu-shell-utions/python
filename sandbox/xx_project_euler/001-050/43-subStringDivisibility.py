################################################################################
##Sub-string divisibility
##Problem 43
##The number, 1406357289, is a 0 to 9 pandigital number because
##it is made up of each of the digits 0 to 9 in some order, but
##it also has a rather interesting sub-string divisibility property.
##
##Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
##In this way, we note the following:
##
##d2d3d4=406 is divisible by 2
##d3d4d5=063 is divisible by 3
##d4d5d6=635 is divisible by 5
##d5d6d7=357 is divisible by 7
##d6d7d8=572 is divisible by 11
##d7d8d9=728 is divisible by 13
##d8d9d10=289 is divisible by 17
##
##Find the sum of all 0 to 9 pandigital numbers with this property.
################################################################################
import itertools
################################################################################
def getThePerms():
    perms = itertools.permutations('0123456789')
    permsLst = list(perms)
    candidates = [''.join(i) for i in permsLst]
    return(candidates)
################################################################################        
grandTotal = 0
theList = getThePerms()
for i in range(len(theList)):
    currentElement = theList[i]
    testMe = currentElement[1]+currentElement[2]+currentElement[3]
    if int(testMe) % 2 == 0:
        testMe = currentElement[2]+currentElement[3]+currentElement[4]
        if int(testMe) % 3 == 0:
            testMe = currentElement[3]+currentElement[4]+currentElement[5]
            if int(testMe) % 5 == 0:
                testMe = currentElement[4]+currentElement[5]+currentElement[6]
                if int(testMe) % 7 == 0:
                     testMe = currentElement[5]+currentElement[6]+currentElement[7]
                     if int(testMe) % 11 == 0:
                        testMe = currentElement[6]+currentElement[7]+currentElement[8]
                        if int(testMe) % 13 == 0:
                            testMe = currentElement[7]+currentElement[8]+currentElement[9]
                            if int(testMe) % 17 == 0:
                                print(currentElement)
                                grandTotal += int(currentElement)

print()
print('The Grand Total:',grandTotal)
################################################################################
#solution: 16695334890
################################################################################
