#-------------------------------------------------------------------------------
# 219_skew-cost_coding.py
#
# problem 219: skew-cost coding
# Let A and B be bit strings (sequences of 0's and 1's).
# If A is equal to the leftmost length(A) bits of B, then A is said to be a
# prefix of B.
# For example, 00110 is a prefix of 001101001, but not of 00111 or 100110.
#
# A prefix-free code of size n is a collection of n distinct bit strings such
# that no string is a prefix of any other. For example, this is a prefix-free
# code of size 6:
#
# 0000, 0001, 001, 01, 10, 11
#
# Now suppose that it costs one penny to transmit a '0' bit, but four pence to
# transmit a '1'. Then the total cost of the prefix-free code shown above is
# 35 pence, which happens to be the cheapest possible for the skewed pricing
# scheme in question.
# In short, we write cost(6) = 35.
#-------------------------------------------------------------------------------
def get_cost(N):
    t = [1,2,3,4]
    k = t[-1] + t[-4]
    while k <= N:
        t.append(k)
        k = t[-1] + t[-4]

    ans=5
    a=6
    for i in range(2,len(t)):
        ans += a * (t[i]-t[i-1])
        a += 1
    ans += a * (N-t[i])
    return ans
#-------------------------------------------------------------------------------
for exp in range(1,51):
    if exp == 9:
        print('--------------------------------------')   
    print(f'Cost(10^{exp}) = {get_cost(10**exp)}')
    if exp == 9:
        print('--------------------------------------')
#-------------------------------------------------------------------------------
# solution: 64564225042
#-------------------------------------------------------------------------------
