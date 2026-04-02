################################################################################
##Permuted multiples
## 
##Problem 52
##It can be seen that the number, 125874, and its double, 251748,
##contain exactly the same digits, but in a different order.
##
##Find the smallest positive integer, x, such that
##2x, 3x, 4x, 5x, and 6x, contain the same digits.
################################################################################
def sameDigits(num1,num2):
    strNum1 = sorted(str(num1))
    strNum2 = sorted(str(num2))
    return(strNum1 == strNum2)
################################################################################
set2 = set()
set3 = set()
set4 = set()
set5 = set()
set6 = set()
possibleSolutions = set()

for i in range(1_000,200_000):
    for j in range(2,7):
        if sameDigits(i,i*j):
            if j == 2: set2.add(i)
            if j == 3: set3.add(i)
            if j == 4: set4.add(i)
            if j == 5: set5.add(i)
            if j == 6: set6.add(i)

possibleSolutions = set2.intersection(set3)
possibleSolutions = possibleSolutions.intersection(set4)
possibleSolutions = possibleSolutions.intersection(set5)
possibleSolutions = possibleSolutions.intersection(set6)

print(possibleSolutions)
################################################################################
#solution: 142857
################################################################################
