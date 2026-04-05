###########################################################################
##Reciprocal cycles
##
##Problem 26
##A unit fraction contains 1 in the numerator.
##The decimal representation of the unit fractions with
##denominators 2 to 10 are given:
##
##1/2	= 	0.5
##1/3	= 	0.(3)
##1/4	= 	0.25
##1/5	= 	0.2
##1/6	= 	0.1(6)
##1/7	= 	0.(142857)
##1/8	= 	0.125
##1/9	= 	0.(1)
##1/10	= 	0.1
##Where 0.1(6) means 0.166666..., and has a 1-digit
##recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
##
##Find the value of d < 1000 for which 1/d contains
##the longest recurring cycle in its decimal fraction part.
## jim mccleery, november, 2012
import math
###########################################################################
def repeating_dec_sol(den):
    if den < 2:
        print('Denominator must be 2 or greater')
        return
    num = 1
    result = ""
    result += str(num // den)
    result += "."
    quotient_num = []
    
    while num:
        remainder = num % den
        num = remainder*10
        quotient = num // den

        if [num, quotient] not in quotient_num:
            quotient_num.append([num, quotient])
        else:
            index = quotient_num.index([num, quotient])
            for i in quotient_num[:index]:
                result += str(i[-1])
            result += "("
            for i in quotient_num[index:]:
                result += str(i[-1])
            result += ")"
            break
        
    return result
###########################################################################
listOfRepeatingDigits = []
for i in range(2,1001):
    strDigits = str(repeating_dec_sol(i))
    leftParen = strDigits.find('(')
    if leftParen != -1:
        rightParen = strDigits.find(')')
        strDigits = strDigits[leftParen+1:rightParen]
        listOfRepeatingDigits.append(str(i))
        listOfRepeatingDigits.append(strDigits)

maxLength = 0

for i in range(len(listOfRepeatingDigits)):
        if len(listOfRepeatingDigits[i]) > maxLength:
            maxLength = len(listOfRepeatingDigits[i])
            keepIndex = i

print(listOfRepeatingDigits[keepIndex-1],listOfRepeatingDigits[keepIndex])
numProcessed = listOfRepeatingDigits[keepIndex-1]           
length = len(listOfRepeatingDigits[keepIndex])
print('Number processed: ',numProcessed,'Length of repetend:',length)
###########################################################################
#solution: 983
###########################################################################
