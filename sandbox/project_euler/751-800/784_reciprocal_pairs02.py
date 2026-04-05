from sympy import divisors
from time import time

def F(N):
    p_minus_one_divisors = [1]
    p_divisors = [1]
    tot_sum = 0
    for p in range(2,N+1):
        if p%4 == 1:
            p_plus_one_divisors = divisors((p+1)//2)
        else:
            p_plus_one_divisors = divisors(p+1)
        div_seq = [x*y for x in p_minus_one_divisors for y in p_plus_one_divisors]
        if p%2 == 1:
            div_seq = set(div_seq + [2*d for d in div_seq])
        tot_sum += sum(d for d in div_seq if d > 2*p)
        p_minus_one_divisors = p_divisors
        p_divisors = p_plus_one_divisors
    return tot_sum

for limit in [5,10**2,2*10**6]:
    start = time()
    solution = F(limit)
    print(f'Solution: {solution}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 5833303012576429231
#  -----------------------------------------------------------------------------
