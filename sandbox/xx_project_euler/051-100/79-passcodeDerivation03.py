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
import time
################################################################################
#function to reorder two elements on the list
def insertBump(idx1,idx2):
    num = usedDigitsList[idx2]
    usedDigitsList.remove(num)
    usedDigitsList.insert(idx1,num) 
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
        usedDigitsSet.add(trio[j])

#convert the set to a list
usedDigitsList = list(usedDigitsSet)

#loop through the usedDigitsList and reorder it
for trio in fromFileList:
    posA = usedDigitsList.index(trio[0])
    posB = usedDigitsList.index(trio[1])
    posC = usedDigitsList.index(trio[2])

    if posB < posA:
        insertBump(posB,posA)

    if posC < posB:
        insertBump(posC,posB)

#make a string out of the updated usedDigitsList
solution = ''
for c in usedDigitsList:
    solution += c

print('The solution:',solution,'Run time:',time.time()-start)
  
################################################################################
#solution: 73162890
################################################################################
