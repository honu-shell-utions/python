# 158-lexicographically.py
#
# Exploring strings for which only one character comes lexicographically after
# its neighbour to the left
#
# Taking three different letters from the 26 letters of the alphabet, character
# strings of length three can be formed. Examples are 'abc', 'hat' and 'zyx'.
#
# When we study these three examples we see that for 'abc' two characters come
# lexicographically after its neighbour to the left.
#
# For 'hat' there is exactly one character that comes lexicographically after
# its neighbour to the left. For 'zyx' there are zero characters that come
# lexicographically after its neighbour to the left.
#
# In all there are 10400 strings of length 3 for which exactly one character
# comes lexicographically after its neighbour to the left.
#
# We now consider strings of n ≤ 26 different characters from the alphabet.
# For every n, p(n) is the number of strings of length n for which exactly one
# character comes lexicographically after its neighbour to the left.
#
# What is the maximum value of p(n)?

from itertools import permutations
max_size = 5
letters = [chr(x) for x in range(97,123)]

grand_total = 0

for n in range(1,max_size+1):
    sub_total = 0
    perms = list(permutations(letters,n))
    for p in perms:
        x = 0
        for space in range(n-1):
            if p[space] < p[space+1]:
                x += 1
        if x == 1:
            sub_total += 1
    print(n,sub_total)
    grand_total += sub_total

print('grand total',grand_total)
