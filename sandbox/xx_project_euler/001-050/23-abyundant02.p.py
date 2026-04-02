# p023_non-abundant_sums.py
#
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less
# than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two
# abundant numbers is 24.
#
# By mathematical analysis, it can be shown that all
# integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as
# the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.
# upper limit 28123

limit = 28123

def is_abundant(n):
    divisors_sum = 1
    for m in range(2, n):
        if n % m == 0:
            divisors_sum += m
    return divisors_sum > n

lst_abundant= []
for i in range(12, limit):
    if is_abundant(i):
        lst_abundant.append(i)

abun_sums = set()
for k in lst_abundant:
    for j in lst_abundant:
        their_sum = k + j
        if their_sum > limit:
            break
        abun_sums.add(their_sum)

not_abun_sums = set()
for num in range(limit+1):
    if num not in abun_sums:
        not_abun_sums.add(num)
print(sum(not_abun_sums))   # 4179871
