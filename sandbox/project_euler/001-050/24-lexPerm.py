##Lexicographic permutations
##Problem 24
##A permutation is an ordered arrangement of objects.
##For example, 3124 is one possible permutation of the
##digits 1, 2, 3 and 4. If all of the permutations are
##listed numerically or alphabetically, we call it lexicographic
##order. The lexicographic permutations of 0, 1 and 2 are:
##
##012   021   102   120   201   210
##
##What is the millionth lexicographic permutation of the digits
##0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
##jim mccleery, november, 2021
######################################################################
import itertools
######################################################################
positionRequired = 1_000_000-1
a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations_object = itertools.permutations(a_list)
permutations_list = list(permutations_object)
print(permutations_list[positionRequired])
######################################################################
# (2, 7, 8, 3, 9, 1, 5, 4, 6, 0)
######################################################################
#Solution: 2783915460
