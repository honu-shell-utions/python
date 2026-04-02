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
def binomial(m,n):
    num = 1
    den = 1
    for i in range (n):
        num*=m-i
        den*=(i+1)
    return num/den

p=1
for n in range (3,27):
    p=2*p+n-1
    print(n,int(p*binomial(26,n)))

########################################################################

