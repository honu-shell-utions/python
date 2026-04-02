#  -----------------------------------------------------------------------------
#  Riffle Shuffles
#  Problem 622
# s https://projecteuler.net/problem=622
#  -----------------------------------------------------------------------------
#  For some reason the "Riffle shuffle" is actually known as the
#  Faro Shuffle: https://en.wikipedia.org/wiki/Faro_shuffle
#  Specifically we are talking about a faro out-shuffle
#  
#  In general, k perfect in-shuffles will restore the order of an n-card deck
#  if 2^{k} = 1 (mod n - 1)
#  For example, 8 consecutive out-shuffles restore the order of a 52-card deck,
#  because 2^{8} = 256 = 1 (mod 51)
#  
#  Therefore, the sum of all n s.t. s(n) = 8 is all n s.t. 2^8 = 1 (mod n - 1) 
#  and no divisor of n does it as well
#  
#  2^8 - 1 = (n - 1)l => 255 = (n - 1)l
#  
#  Therefore we find the divisors of 255, they are our candidate numbers.
#  For each candidate number, x, we check if 2^n (mod x) = 1, if yes then we need
#  to check it is indeed the smallest
#  
#  Knowing that 2^n = 1 (mod x), we know that either this is the order of 2 or a
#  divisor of 60 is, simply check each divisor of 60
#  -----------------------------------------------------------------------------
from time import time
from sympy import divisors
#  -----------------------------------------------------------------------------
def euler_622(n):
    div = divisors(pow(2, n) - 1)
    div_n = divisors(n)
    total = 0
    # go through the divisors of 2^n - 1 = xk
    for x in div:
        # test to see if 2^n = 1 (mod x)
        if pow(2, n, x) == 1:
            # now we know 2^n = 1 (mod x),
            # now we test if any divisor, y, of n does it earlier
            # because then s(x + 1) = y
            if all([pow(2, y, x) != 1 for y in div_n[:len(div_n) - 1]]):
                total += (x + 1)
    return total
#  -----------------------------------------------------------------------------
print('-'*70)
for n_cards in range(1,101):
    t0 = time()
    ans = euler_622(n_cards)
    rt = time() - t0
    if n_cards == 8 or n_cards == 60:
        print('-'*70)
    print(f's({n_cards:>3}): answer: {ans:>32}  runtime: {rt:.5f}')
    if n_cards == 8 or n_cards == 60:
        print('-'*70)
print('-'*70)
#  -----------------------------------------------------------------------------
#  solution: 3010983666182123972
#  -----------------------------------------------------------------------------
