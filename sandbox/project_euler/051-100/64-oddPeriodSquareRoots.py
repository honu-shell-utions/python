################################################################################
##Odd Period Square Roots
##Problem 64
################################################################################
import math
################################################################################
def contFrac(n):
    numerator1 = 1
    a = int(math.sqrt(n))
    aList = [a]
    while True:
        if n == a*a:
            break
        numerator2 = (n - a**2) / numerator1
        next = int((math.sqrt(n)+a)/numerator2)
        aList.append(next)
        if next == 2*int(math.sqrt(n)):
            break
        denominator = next*numerator2 - a
        numerator1 = numerator2
        a = denominator
    return aList
################################################################################
counter = 0
MAX = 10_000
for i in range(2,MAX+1):
    cfResult = contFrac(i)
    if i == 7:
        print(cfResult)
    #note: we are looking for a repeating pattern that is odd in length
    #the first element of the chain is the int(sqrt(number being processed))
    #so if the repeating part is odd in length the whold chain is even in length
    if len(cfResult) % 2 == 0:
        counter += 1
print('Solution: ',counter)
################################################################################
#solution: 1322
################################################################################
