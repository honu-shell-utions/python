#  -----------------------------------------------------------------------------
#  Dominating Numbers
#  Problem 788
#  https://projecteuler.net/problem=788
#  -----------------------------------------------------------------------------
def is_dominating(n):
    digit_count = [0]*10
    str_n = str(n)
    for d in str_n:
        digit_count[int(d)] += 1
    if max(digit_count) > len(str_n) // 2:
        return True
    else:
        return False
#  -----------------------------------------------------------------------------
def D(n):
    count = 0
    for k in range(1,10**n):
        if is_dominating(k):
            count += 1
    return count
#  -----------------------------------------------------------------------------
MOD = 10**9+7
for N in range(1,11):
    print(f'From 1 to 10^{N} there are {D(N)%MOD} dominate numbers.')
#  -----------------------------------------------------------------------------
#  solution: 471745499
#  -----------------------------------------------------------------------------
