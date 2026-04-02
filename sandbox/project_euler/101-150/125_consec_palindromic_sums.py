# p125_consec_palindromic_sums.py
#
# The palindromic number 595 is interesting because it can be written as the
# sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.
#
# There are exactly eleven palindromes below one-thousand that can be written
# as consecutive square sums, and the sum of these palindromes is 4164.
# Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned
# with the squares of positive integers.
#
# Find the sum of all the numbers less than 10^8 that are both palindromic and
# can be written as the sum of consecutive squares.
from time import time
from math import isqrt


go = time()
def reverse(n):
    rev = 0
    while n > 0:
        rev = 10 * rev + n % 10
        n = n // 10
    return rev


def is_palindrome(n):
    return n == reverse(n)


LIMIT = 10**8
#LIMIT = 10**3


st = set()
for a in range(1, isqrt(LIMIT)):
    a_sqrd = a * a

    while a_sqrd < LIMIT:
        a += 1
        a_sqrd += a * a
        if is_palindrome(a_sqrd) and a_sqrd < LIMIT:
            st.add(a_sqrd)
            

print('ans:', sum(st), 'runtime:', time() - go)
#print('eleven palindromes less than 1000: 4164')   
