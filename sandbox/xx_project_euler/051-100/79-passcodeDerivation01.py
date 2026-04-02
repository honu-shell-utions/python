################################################################################
# problem 79 passcode derivation
#
# A common security method used for online banking is to ask the user for three
# random characters from a passcode. For example, if the passcode was 531278,
# they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
# be: 317.
#
# The text file, keylog.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order, analyse the file
# so as to determine the shortest possible secret passcode of unknown length.
#
################################################################################
import itertools
import time
################################################################################
def makePerms(theList):
    permutations_object = itertools.permutations(theList)
    return(list(permutations_object))
################################################################################
#set start time
start = time.time()

#read the file into a list
fromFileList = [x for x in open('79-keylog.txt').read().splitlines()]

#set to hold the used digits
usedDigitsSet = set()

#fill the set
for trio in fromFileList:
    for j in range(3):
        usedDigitsSet.add(int(trio[j]))

#creat a list from the set of used digits & sort it
usedDigitsList = list(usedDigitsSet)

#get the permutations of that list
permList = makePerms(usedDigitsList)

#loop through the permutations of the usedDigitList
for perm in permList:
    #set flag
    allGood = True
    #for each permutation loop through the trios in the fromFileList
    for trio in fromFileList:
        #for each trio test the order against the current perm
        val01 = int(trio[0])
        val02 = int(trio[1])
        val03 = int(trio[2])
        if not(perm.index(val01) < perm.index(val02) < perm.index(val03)):
            allGood = False
            break
    solStr = ''       
    if allGood:
        for i in range(len(perm)):
            solStr += str(perm[i])            
        print('The solution is:',solStr,'Run time:',time.time()-start)
        break              
################################################################################
#solution: 73162890
################################################################################
