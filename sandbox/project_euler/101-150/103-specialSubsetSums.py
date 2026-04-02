# ----------------------------------------------------------------------------
# 103-specialSubsetSums.py
#
# Let S(A) represent the sum of elements in set A of size n. We shall call it
# a special sum set if for any two non-empty disjoint subsets, B and C, the
# following properties are true:
# 1) S(B) ≠ S(C); that is, sums of subsets cannot be equal.
# 2) If B contains more elements than C then S(B) > S(C).
#
# If S(A) is minimised for a given n, we shall call it an optimum special sum
# set. The first five optimum special sum sets are given below.
# n = 1: {1}
# n = 2: {1, 2}
# n = 3: {2, 3, 4}
# n = 4: {3, 5, 6, 7}
# n = 5: {6, 9, 11, 12, 13}
# It seems that for a given optimum set, A = {a1, a2, ... , an}, the next
# optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the
# "middle" element on the previous row.
# By applying this "rule" we would expect the optimum set for n = 6 to be
# A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the
# optimum set, as we have merely applied an algorithm to provide a near
# optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25},
# with S(A) = 115 and corresponding set string: 111819202225.
#
# Given that A is an optimum special sum set for n = 7, find its set string.
# NOTE: This problem is related to Problem 105 and Problem 106
# ----------------------------------------------------------------------------
##def passRules(s1,s2):
### 1) S(B) ≠ S(C); that is, sums of subsets cannot be equal.
### 2) If B contains more elements than C then S(B) > S(C).
##     sum1 = sum(s1)
##     sum2 = sum(s2)
##     if sum1 == sum2:
##          return False
##     elif len(s1) > len(s2) and sum1 <= sum2:
##          return False
##     elif len(s1) < len(s2) and sum1 >= sum2:
##          return False
##     else:
##          return True
# ----------------------------------------------------------------------------
# A = {a1, a2, ... , an}
# B = {b, a1+b, a2+b, ... ,an+b}
def getNextSet(previousSet):
     newSet = set()
     tempLst = sorted(list(previousSet))
     middleIndex = len(tempLst)//2
     b = tempLst[middleIndex]
     newSet.add(b)
     for i in range(len(tempLst)):
          newSet.add(tempLst[i]+b)
     return newSet                     
# ----------------------------------------------------------------------------
##from itertools import chain, combinations
##
##def powerset(theSet):
##    return chain.from_iterable(combinations(theSet, r) for r in range(len(theSet)+1))
# ----------------------------------------------------------------------------
import time
start = time.time()
currentSet = {11, 18, 19, 20, 22, 25}
currentSet = getNextSet(currentSet)
temp = sorted(list(currentSet))
solution = ''
for element in temp:
     solution += str(element)
     
print('The solution:',solution,'Run Time:',time.time()-start)
# ----------------------------------------------------------------------------
# solution: 20313839404245
# ----------------------------------------------------------------------------
