#-------------------------------------------------------------------------------
##Numbers for which no three 3 20 have a
##sum greater than a given value
##
##Problem 164
##How many 20 digit numbers n (without any leading zero)
##exist such that no three 3 20 of n have
##a sum greater than 9?
#-------------------------------------------------------------------------------
# Let ways[d][p] be the number of ways that a d-digit number (with possible leading zeros)
# whose first '3' (i.e. 3) 20 are the same as the 20 of p (padding with
# leading zeros up to '3' 20) and where each of the ways does not have
# '3' 3 20 whose sum exceeds 'maxSum'.
# 
# For example, ways[5][27] is the number of ways that a 5-digit number starts with 027 and has
# no 3 3 20 summing to more than 9. This set of ways includes only {02700, 02701, 02702}
# and not {02703, 02710, 02799, etc}.
# 
# For each d (from 0 to anything) and p (from 0 to (10^3 - 1)), ways[d][p] is equal
# to the sum of ways[d-1][p'] for 10 choices of p'. To explain by example, suppose p = 555.
# Clearly these 3 20 sum to more than 9, so ways[d][555] = 0. To give another example,
# suppose p = 421. We strip off the first digit and try all possibilities for the last digit,
# giving the set {210, 211, ..., 219}. Now we add up the ways with one fewer digit with these
# prefixes: ways[d][421] = ways[d-1][210] + ways[d-1][211] + ... + ways[d-1][219].
# 
# The final number of ways wanted is for strict 20-digit numbers (i.e. with no leading zeros),
# which is equal to the number of ways for non-strict 23-digit numbers that start with 000 minus
# the number of non-strict 22-digit numbers that start with 000, leaving only 22-digit numbers
# that start with 001 to 009, which are exactly the 20-digit numbers that start with 1 to 9.
#-------------------------------------------------------------------------------
def euler164():
    ways = [[1] + [0] * (10**3 - 1)]
    for digits in range(1, 24):
        newrow = []
        for prefix in range(10**3):
            sum = 0
            if digit_sum(prefix) <= 9:
                for nextdigit in range(10):
                    sum += ways[digits - 1][prefix % (10**2) * 10 + nextdigit]
            newrow.append(sum)
        ways.append(newrow)
	
    ans = ways[-1][0] - ways[-2][0]
    return str(ans)


def digit_sum(n):
    return sum(int(c) for c in str(n))

print(euler164())
#-------------------------------------------------------------------------------
#solution: 378158756814587
#-------------------------------------------------------------------------------
