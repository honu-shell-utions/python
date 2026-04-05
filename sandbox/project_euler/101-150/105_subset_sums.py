################################################################################
##Special subset sums: testing
##Problem 105
##Let S(A) represent the sum of elements in set A of size n.
##We shall call it a special sum set if for any two non-empty
##disjoint subsets, B and C, the following properties are true:
##
##S(B) ≠ S(C); that is, sums of subsets cannot be equal.
##If B contains more elements than C then S(B) > S(C).
##For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special
##sum set because 65 + 87 + 88 = 75 + 81 + 84,
##whereas {157, 150, 164, 119, 79, 159, 161, 139, 158}
##satisfies both rules for all possible subset pair combinations and S(A) = 1286.
##
##Using sets.txt (right click and "Save Link/Target As..."), a 4K
##text file with one-hundred sets containing seven to twelve elements
##(the two examples given above are the first two sets in the file),
##identify all the special sum sets, A1, A2, ..., Ak, and find the
##value of S(A1) + S(A2) + ... + S(Ak).
##
##NOTE: This problem is related to Problem 103 and Problem 106.
################################################################################
from itertools import chain, combinations
import csv
from time import time
################################################################################
#load the file
def process_file():
    temp = []
    with open('105_subset_sums.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            one_set = {int(i) for i in row}
            temp.append(one_set)      
    return temp
################################################################################
#create the power set for the current set
def powerset(the_set):
    return chain.from_iterable(combinations(the_set, r) for r in range(len(the_set)+1))
################################################################################
def the_test(disjoint_pairs):
    pass_the_test = []
    fail_the_test = []
    for dp in disjoint_pairs:
        flag = True
        s1,s2 = dp
        if sum(s1) == sum(s2):
            flag = False
        if len(s1) > len(s2) and sum(s1) < sum(s2):
            flag = False
        if len(s2) > len(s1) and sum(s2) < sum(s1):
            flag = False

        if flag:
            pass_the_test.append([s1,s2])
        else:
            fail_the_test.append([s1,s2])
                
    return pass_the_test,fail_the_test
################################################################################
#start the clock
start = time()

#list to hold the sets from the data file
sets_from_file = []
sets_from_file = process_file()

##create the set of sets that pass the test
pass_the_test = []
#to hold the total of the sums of the 'passing' sets
total = 0
for current_set in sets_from_file:
    disjoint_pairs = []
    ps = set()
    #create the power set from the current set
    ps =  powerset(current_set)
    #get the combos taking 2 subsets at a time
    combos = set(combinations(ps,2))
    for c in combos:
        s1,s2 = c
        s1 = set(s1)
        s2 = set(s2)
        if s1.isdisjoint(s2) and len(s1) != 0 and len(s2) != 0:
            disjoint_pairs.append([s1,s2])

    #extract the list of passed and the list of failed
    p,f = the_test(disjoint_pairs)

    #if there were no failures accumulate the set sums
    if len(f) == 0:
        total += sum(current_set)

print('The solution:',total,'Run Time:',time()-start)
################################################################################
#solution: 73702
################################################################################
