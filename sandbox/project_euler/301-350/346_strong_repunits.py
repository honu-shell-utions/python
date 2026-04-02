#  -----------------------------------------------------------------------------
#  Strong Repunits
#  Problem 346
#  https://projecteuler.net/problem=346
#  -----------------------------------------------------------------------------
# 1 is a strong repunit because in every base b >= 2, its representation is "1",
# which is a repunit.
# 
# 2 is not a strong repunit because in base 2 it is "10", but in every
# base b >= 3 it is "2".
# 
# As for other numbers, first assume that n is an arbitrary integer at least 3.
# It is trivially a repunit in base b = n - 1 (which is at least 2), where its
# representation is "11". For this n to be a strong repunit, it needs to be a
# repunit in at least one other base.
# 
# Obviously it can't be "11" in another base. So it must be {"111",
# "1111", "11111", or some longer string} in some base smaller than b.
# 
# Phrased differently, if an integer n >= 3 has the representation
# {"111", "1111", or some longer string} in some base b >= 2, then
# it is automatically a strong repunit because firstly, its value is
# at least 7 ("111" in base 2), and secondly it is equal to "11" in some
# base b' >= 2.
# 
# Hence all we need to do is for each repunit length 3, 4, 5, etc., we
# generate the string (e.g. "111"), then evaluate its value at base 2, 3, etc.
# as long as the value stays within the limit, and add these values to the set
# of known strong repunits (to catch possible duplicates).
# 
# Note that the longest repunit length we need to test is at most the
# bit length of the limit. For example, because the limit is
# 10^12 = 1110100011010100101001010001000000000000 (base 2),
# any repunit longer than "1111111111111111111111111111111111111111"
# is guaranteed to exceed the limit in every base.
# 
#  -----------------------------------------------------------------------------
from itertools import count
from time import time
#  -----------------------------------------------------------------------------
def euler_346(limit):
    strong_repunits = {1}
    for length in range(3,limit.bit_length()+1):
        for base in count(2):
        # Evaluate value = base^(length-1) + base^(length-2) + ... + base^1 + base^0
        # Due to the geometric series, value = (base^length - 1) / (base - 1)
            value = (base**length - 1) // (base - 1)
            if value >= limit:
                break
            else:
                strong_repunits.add(value)
    return sum(strong_repunits)         
#  -----------------------------------------------------------------------------
print('-'*70)
for exp in range(1,16):
    start = time()
    if exp == 12:
        print('-'*70)    
    print(f'Solution for 10^{exp:2}: {euler_346(10**exp):25}, Run-Time: {time()-start:6.3f}')
    if exp == 12:
        print('-'*70)    
print('-'*70)
#  -----------------------------------------------------------------------------
#  solution: 336108797689259276
#  -----------------------------------------------------------------------------
