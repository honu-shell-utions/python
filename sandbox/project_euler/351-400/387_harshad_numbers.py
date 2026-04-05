# -----------------------------------------------------------------------------
# 387_harshad_numbers.py
#
# A Harshad or Niven number is a number that is divisible by the sum of
# its digits.
#
# 201 is a Harshad number because it is divisible by 3, the sum of its digits.
# When we truncate the last digit from 201, we get 20, which is a Harshad
# number. When we truncate the last digit from 20, we get 2, which is also a
# Harshad number.
#
# Let's call a Harshad number that, while recursively truncating the last
# digit, always results in a Harshad number a right truncatable Harshad number.
#
# Also:
# 201 / 3 = 67 which is prime. Let's call a Harshad number that, when divided
# by the sum of its digits, results in a prime a strong Harshad number.
#
# Now take the number 2011 which is prime. When we truncate the last digit
# from 2011 we get 201, a strong Harshad number that is also right truncatable.
#
# Let's call such primes strong, right truncatable Harshad primes.
#
# You are given that the sum of the strong, right truncatable Harshad primes
# less than 10,000 is 90619.
#
# Find the sum of the strong, right truncatable Harshad primes less than 10**14
# -----------------------------------------------------------------------------
from sympy import primerange, isprime
from time import time
# -----------------------------------------------------------------------------
def get_right_trunc():
    right_truncatables = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in right_truncatables:
        for a in range(0, 10):
            number = str(i) + str(a)
            sum = 0
            for b in number:
                sum += int(b)
            if int(number) % sum == 0 and int(number) < limit:
                right_truncatables.append(int(number))
    return right_truncatables
# -----------------------------------------------------------------------------
def get_strong_harsh():
    strong_harshad_numbers = []
    for i in right_truncatables:
        sum = 0
        for b in str(i):
            sum += int(b)
        if isprime(int(i / sum)) == True:
            strong_harshad_numbers.append(i)
    return strong_harshad_numbers
# -----------------------------------------------------------------------------
def get_prime_harsh():
    sols = []
    for i in strong_harshad_numbers:
        for a in range(0, 10):
            number = int(str(i) + str(a))
            if isprime(number) == True and number < limit:
                sols.append(number)
    return sols
# -----------------------------------------------------------------------------
start = time()
for limit in [10**4,10**8,10**14,10**20]:
    start = time()
    right_truncatables = get_right_trunc()
    strong_harshad_numbers = get_strong_harsh()
    solutions = get_prime_harsh()
    print(f'Solution for n = {limit}: {sum(solutions)}, Run-Time: {round(time()-start,3)} seconds')
# -----------------------------------------------------------------------------
#10^14 -> ans = 696067597313468
#10^8  -> ans = 130459097
#10^4  -> ans = 90619
# -----------------------------------------------------------------------------
