################################################################################
# Perhaps less well known is 169, in that it produces the longest chain of
# numbers that link back to 169; it turns out that there are only three such
# loops that exist:
#
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
#
# It is not difficult to prove that EVERY starting number will eventually get
# stuck in a loop.  For example,
#  69 → 363600 → 1454 → 169 → 363601 (→ 1454)
#  78 → 45360 → 871 → 45361 (→ 871)
#  540 → 145 (→ 145)
#
# Starting with 69 produces a chain of five non-repeating terms, but the
# longest non-repeating chain with a starting number below one million is
# sixty terms.
#
# How many chains, with a starting number below one million, contain exactly
# sixty non-repeating terms?
################################################################################
import math
import time
################################################################################
def totalFacts(num):
    total = 0
    strNum = str(num)
    for n in strNum:
        total += math.factorial(int(n))
    return(total)
################################################################################
start = time.time()
theList = []
countExactly60 = 0

for i in range(1,1_000_000):
    theList.clear()
    theList.append(i)
    temp = i
    while True:
        temp = totalFacts(temp)
        if temp in theList:
            theList.append(temp)
            break
        else:
            theList.append(temp)

    if len(theList)-1 == 60 and theList[0] != theList[-1]:
        countExactly60 += 1
        
print('The solution:',countExactly60,'Run time:', time.time()-start)
################################################################################
#solution: 402
################################################################################

