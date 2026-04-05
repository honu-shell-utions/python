################################################################################
##Special subset sums: meta-testing
##Problem 106
##Let S(A) represent the sum of elements in set A of size n.
##We shall call it a special sum set if for any two non-empty
##disjoint subsets, B and C, the following properties are true:
##
##S(B) ≠ S(C); that is, sums of subsets cannot be equal.
##If B contains more elements than C then S(B) > S(C).
##
##For this problem we shall assume that a given set contains n
##strictly increasing elements and it already satisfies the second rule.
##
##Surprisingly, out of the 25 possible subset pairs that can be
##obtained from a set for which n = 4, only 1 of these pairs need
##to be tested for equality (first rule).  Similarly, when n = 7,
##only 70 out of the 966 subset pairs need to be tested.
##
##For n = 12, how many of the 261625 subset pairs that can be
##obtained need to be tested for equality?
################################################################################
from itertools import chain, combinations
from time import time
################################################################################
def how_many_to_test(set_of_pairs):
    questionable_pairs = 0
    for sp in set_of_pairs:
        s1,s2 = sp
        s1_list = sorted(list(s1))
        s2_list = sorted(list(s2))
        for k in range(len(s1)):
            if s1_list[k] > s2_list[k]:
                questionable_pairs += 1
                break
    return questionable_pairs           
################################################################################
#create the power set for the current set
def powerset(the_set):
    return chain.from_iterable(combinations(the_set, r) for r in range(len(the_set)+1))
################################################################################
def qualifying_disjoint_pairs(current_set):
    disjoint_pairs = []
    ps =  powerset(current_set)
    #get the combos taking 2 subsets at a time
    combos = set(combinations(ps,2))
    for c in combos:
        s1,s2 = c
        s1 = set(s1)
        s2 = set(s2)
        if s1.isdisjoint(s2):
            disjoint_pairs.append([s1,s2])
    return disjoint_pairs
################################################################################
#start the clock
start = time()
current_set04 = [1,2,3,4]
current_set05 = [1,2,3,4,5]
current_set06 = [1,2,3,4,5,6]
current_set07 = [1,2,3,4,5,6,7]
current_set12 = [1,2,3,4,5,6,7,8,9,10,11,12]

#s04 = qualifying_disjoint_pairs(current_set04)
#s05 = qualifying_disjoint_pairs(current_set05)
#s06 = qualifying_disjoint_pairs(current_set06)
#s07 = qualifying_disjoint_pairs(current_set07)
s12 = qualifying_disjoint_pairs(current_set12)

size22 = []
size33 = []
size44 = []
size55 = []
size66 = []

for q in s12:
    s1,s2 = q
    if len(s1) != len(s2): continue
    if len(s1) == 1: continue
    if len(s1) == 2:
        size22.append(q)
    elif len(s1) == 3:
        size33.append(q)
    elif len(s1) == 4:
        size44.append(q)
    elif len(s1) == 5:
        size55.append(q)
    else:
        size66.append(q)

count = how_many_to_test(size22)
count += how_many_to_test(size33)
count += how_many_to_test(size44)
count += how_many_to_test(size55)
count += how_many_to_test(size66)

print('Solution:',count,'Run Time:',time()-start)
################################################################################
#solution: 21384
################################################################################
