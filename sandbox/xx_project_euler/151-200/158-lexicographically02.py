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

########################################################################
from math import factorial
max_size = 26
dp = { (0, 0, 0) : 0, (0, 0, 1) : 1}

def get_num(*args):
    if args in dp:
        return dp[args]
    
    length, num_greater, count = args
    if count > 1:
        return 0
    result = sum(get_num(length-1, i, count + ((i < num_greater) and 1 or 0)) \
                 for i in range(length))
    dp[args] = result
    return result
        
p = lambda n: sum(get_num(n-1, i, 0) for i in range(n))\
    * (factorial(max_size) // (factorial(n) * factorial(max_size - n)))


max_pn, max_n = max((p(n), n) for n in range(2, max_size+1))
print("The result is:", max_pn, "found at n:", max_n)
