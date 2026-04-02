# p169_powers_of_2.py
# Exploring the number of different ways a number can be expressed as a sum of
# powers of 2
#
# Define f(0)=1 and f(n) to be the number of different ways n can be expressed
# as a sum of integer powers of 2 using each power no more than twice.
#
# For example, f(10)=5 since there are five different ways to express 10:
# 1 + 1 + 8
# 1 + 1 + 4 + 4
# 1 + 1 + 2 + 2 + 4
# 2 + 4 + 4
# 2 + 8
#
# What is f(10^25)?
from math import log10
d_data = {0: 1, 1: 1}
d_chk = {10: 5, 10**25: 178653872807}


def euler169(n):
    if n in d_data:
        return d_data[n]
    if n % 2:
        val = euler169(n // 2)
    else:
        val = euler169(n // 2) + euler169(n // 2 - 1)
    d_data[n] = val
    return val


for k, v in d_chk.items():
    ans = euler169(k)
    exp = int(log10(k))
    print(f'euler(10^{exp}): {ans} {ans==d_chk[k]}')
print()

# for i in sorted(d_data):
#     print(f'{i:>32,} {d_data[i]:>17,}')
