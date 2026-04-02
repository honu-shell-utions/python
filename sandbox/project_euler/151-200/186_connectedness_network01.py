#-------------------------------------------------------------------------------
# 186_connectedness_network.py
# Here are the records from a busy telephone system with one million users:
# RecNr	Caller	Called
# 1	200007	100053
# 2	600183	500439
# 3	600863	701497
# ...	...	...
# The telephone number of the caller and the called number in record n are
# Caller(n) = Ssub(2n-1) and Called(n) = Ssub(2n) where S1, 2, 3,... come from
# the "Lagged Fibonacci Generator":
#
# For 1 ≤ k ≤ 55, Ssub(k) = [100003 - 200003k + 300007k^3] (modulo 1000000)
# For 56 ≤ k, Ssub(k) = [Ssub(k-24) + Ssub(k-55)] (modulo 1000000)
#
# If Caller(n) = Called(n) then the user is assumed to have misdialled and the
# call fails; otherwise the call is successful.
#
# From the start of the records, we say that any pair of users X and Y are
# friends if X calls Y or vice-versa. Similarly, X is a friend of a friend of
# Z if X is a friend of Y and Y is a friend of Z; and so on for longer chains.
#
# The Prime Minister's phone number is 524287. After how many successful
# calls, not counting misdials, will 99% of the users (including the PM) be a
# friend, or a friend of a friend etc., of the Prime Minister?
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def lfg():
    seq=[0]
    for k in range(1,56):
        seq.append((100003 - 200003*k + 300007*k**3)%1000000)
    for k in range(56,10**7):
        seq.append((seq[k-24]+seq[k-55])%1000000)
    return seq
#-------------------------------------------------------------------------------
records = lfg()
for n in range(1,4):
    print(n,records[2*n-1],records[2*n])
#-------------------------------------------------------------------------------
#solution:
#-------------------------------------------------------------------------------
