##Digit factorials
##
##Problem 34
##145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
##
##Find the sum of all numbers which are equal to the sum of the
##factorial of their digits.
##
##Note: As 1! = 1 and 2! = 2 are not sums they are not included.
import math
totalOfAll = 0
for i in range(3,2_500_000):
    strI = str(i)
    total = 0
    for j in range(len(strI)):
        total += math.factorial(int(strI[j]))
    if total == i:
        totalOfAll += i
print(totalOfAll)
#solution 40730       

