################################################################################
##Magic 5-gon ring
##Problem 68
##Consider the following "magic" 3-gon ring, filled
##with the numbers 1 to 6, and each line adding to nine.
##
##
##Working clockwise, and starting from the group of
##three with the numerically lowest external node
##(4,3,2 in this example), each solution can be described
##uniquely.
##
##For example, the above solution can be described by
##the set: 4,3,2; 6,2,1; 5,1,3.
##
##It is possible to complete the ring with four different
##totals: 9, 10, 11, and 12. There are eight solutions
##in total.
##
##Total	Solution Set
##9	4,2,3; 5,3,1; 6,1,2
##9	4,3,2; 6,2,1; 5,1,3
##10	2,3,5; 4,5,1; 6,1,3
##10	2,5,3; 6,3,1; 4,1,5
##11	1,4,6; 3,6,2; 5,2,4
##11	1,6,4; 5,4,2; 3,2,6
##12	1,5,6; 2,6,4; 3,4,5
##12	1,6,5; 3,5,4; 2,4,6
##
##By concatenating each group it is possible to form 9-digit strings;
##the maximum string for a 3-gon ring is 432621513.
##
##Using the numbers 1 to 10, and depending on arrangements,
##it is possible to form 16- and 17-digit strings. What is the maximum
##16-digit string for a "magic" 5-gon ring?
################################################################################
import random
import itertools
outerRing = []
innerRing = []
solutions = []
intSolutions = []
b = c = d = e = f = 0
a = '6'
################################################################################
def makePerms(numList):
    permutations_object = itertools.permutations(numList)
    return(list(permutations_object))
################################################################################
def makeIntSolutions():
    tempList = []
    i = 0
    while i < len(solutions):
        temp = ''.join(solutions[i]+solutions[i+1]+solutions[i+2]+solutions[i+3]+solutions[i+4])
        tempList.append(int(temp))
        i += 5
    return(tempList)
################################################################################
outerPerms = makePerms(['7','8','9','10'])
innerPerms = makePerms(['1','2','3','4','5'])

for outer in range(len(outerPerms)):
    b = outerPerms[outer][0]
    c = outerPerms[outer][1]
    d = outerPerms[outer][2]
    e = outerPerms[outer][3]
    for inner in range(len(innerPerms)):     
        g = innerPerms[inner][0]
        h = innerPerms[inner][1]
        i = innerPerms[inner][2]
        j = innerPerms[inner][3]
        f = innerPerms[inner][4]
        if int(a) + int(g) + int(h) == \
            int(b) + int(h) + int(i) == \
            int(c) + int(i) + int(j) == \
            int(d) + int(j) + int(f) == \
            int(e) + int(f) + int(g):
            solutions.append([a,g,h])
            solutions.append([b,h,i])
            solutions.append([c,i,j])
            solutions.append([d,j,f])
            solutions.append([e,f,g])

counter = 1
for i in solutions:
    print(i,end='')
    if counter % 5 == 0:
        print()
    counter += 1

intSolutions = makeIntSolutions()   
print(intSolutions)
if len(intSolutions) > 0:
    print('Solution:',max(intSolutions))
else:
    print('No solution')
################################################################################
#solution: 6531031914842725
################################################################################
