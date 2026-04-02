# 238_infinite_string_tour.py
#
# Create a sequence of numbers using the "Blum Blum Shub" pseudo-random number
# generator:
# s↓0 = 14025256
# s↓(n+1) = s↓(n)**2 mod 20300713 (where ↓ means subscript)
#
# Concatenate these numbers  s↓0s↓1s↓2... to create a string w of infinite
# length. Then, w = 14025256741014958470038053646...
#
# For a positive integer k, if no substring of w exists with a sum of digits
# equal to k, p(k) is defined to be zero. If at least one substring of w
# exists with a sum of digits equal to k, we define p(k) = z, where z is the
# starting position of the earliest such substring.
#
# For instance:
# The substrings 1, 14, 1402, ...
# with respective sums of digits equal to 1, 5, 7, ...
# start at position 1, hence p(1) = p(5) = p(7) = ... = 1.
#
# The substrings 4, 402, 4025, ...
# with respective sums of digits equal to 4, 6, 11, ...
# start at position 2, hence p(4) = p(6) = p(11) = ... = 2.
#
# The substrings 02, 0252, ...
# with respective sums of digits equal to 2, 9, ...
# start at position 3, hence p(2) = p(9) = ... = 3.
#
# Note that substring 025 starting at position 3, has a sum of digits equal
# to 7, but there was an earlier substring (starting at position 1) with a sum
# of digits equal to 7, so p(7) = 1, not 3.
#
# We can verify that, for 0 < k ≤ 10**3, ∑ p(k) = 4742
#
# Find ∑ p(k), for 0 < k ≤ 2×10**15
# {ans == 9922545104535661}
# -----------------------------------------------------------------------------
from time import time
# -----------------------------------------------------------------------------
start = time()

from itertools import accumulate, chain
from time import time

S0 = 14025256
SEQ_MOD = 20300713


def gen_seq():
    s = S0
    while True:
        for d in str(s):
            yield int(d)
        s = pow(s, 2, SEQ_MOD)
        if s == S0:
            break

PARTIAL_SUMS = tuple(chain((0,), accumulate(gen_seq())))  # include 0 as a partial sum
N = len(PARTIAL_SUMS) - 1  # real length of sequence should not include the empty sum (0).
PARTIAL_SUMS_SET = frozenset(PARTIAL_SUMS)  # with 0 added we find sums that are divisible by PARTIAL_SUMS[-1].

def p(k):
    for offset in range(N):
        if (k + PARTIAL_SUMS[offset]) % PARTIAL_SUMS[-1] in PARTIAL_SUMS_SET:  # This works only if 0 is sums.
            return offset + 1
    return 0

num_recurrent_sum, remainder = divmod(2 * (10 ** 15), PARTIAL_SUMS[-1])
recurrent_sum = sum(p(k+1) for k in range(PARTIAL_SUMS[-1]))
print('period:',PARTIAL_SUMS[-1])
solution = (recurrent_sum * num_recurrent_sum) + sum(p(k+1) for k in range(remainder))

print(f'Solution: {solution}, Run-Time: {time()-start}')
# -----------------------------------------------------------------------------
# solution: 9922545104535661
# -----------------------------------------------------------------------------
