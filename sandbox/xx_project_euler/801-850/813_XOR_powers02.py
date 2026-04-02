#  -----------------------------------------------------------------------------
#  XOR-Powers
#  Problem 813
#  https://projecteuler.net/problem=813
#  -----------------------------------------------------------------------------
#  We can represent each whole number as a set S of nonnegative integers, where 
#  d ∈ S if and only if the 2^d-digit in the number's binary representation is 1.
#  To compute P(8^12*12^8) = P(2^32*3^8), we start with 11 (represented by the set 
#  {0,1,3}), square 52 times, and then cube 8 times.
#  -----------------------------------------------------------------------------
def multiply(S, T):
    product = set()
    for s in S:
        for t in T:
            if s+t in product:
                product.remove(s+t)
            else:
                product.add(s+t)
    return product
#  -----------------------------------------------------------------------------
def square(S):
    return multiply(S, S)
#  -----------------------------------------------------------------------------
def cube(S):
    return multiply(multiply(S, S), S)
#  -----------------------------------------------------------------------------
# start with 11 = 2^0 + 2^1 + 2^3
S = {0,1,3}

# square 52 times
for i in range(52):
    S = square(S)

# cube 8 times
for i in range(8):
    S = cube(S)

# compute the residue modulo 10^9 + 7
answer = 0
for s in S:
    answer += pow(2, s, 10**9+7)
    answer %= 10**9+7
print(answer)
#  -----------------------------------------------------------------------------
#  solution: 14063639
#  -----------------------------------------------------------------------------
