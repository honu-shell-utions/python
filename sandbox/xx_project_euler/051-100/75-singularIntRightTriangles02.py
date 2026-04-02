# It turns out that 12 cm is the smallest length of wire that can be bent to
# form an integer sided right angle triangle in exactly one way, but there
# are many more examples.
# 12 cm: (3, 4, 5)
# 24 cm: (6, 8, 10)
# 30 cm: (5, 12, 13)
# 36 cm: (9, 12, 15)
# 40 cm: (8, 15, 17)
# 48 cm: (12, 16, 20)
#
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
# integer sided right angle triangle, and other lengths allow more than one
# solution to be found; for example, using 120 cm it is possible to form
# exactly three different integer sided right angle triangles.
# 120 cm: (30, 40, 50), (20, 48, 52), (24, 45, 51)
#
# Given that L is the length of the wire, for how many values of L ≤ 1_500_000
# can exactly one integer sided right angle triangle be formed?
# from itertools import takewhile, count
# from math import gcd
# import time
#
# wire_len = 1_500_000
# start = time.time()
#
#
# def find_hits():
#     found_per = set()
#     rep_per = set()
#     generator = ((n, m) for n in count(3, 2) for m in range(1, n, 2) if gcd(m, n) == 1)
#     for n, m in generator:
#         a = m * n
#         b = (n ** 2 - m ** 2) // 2
#         c = (n ** 2 + m ** 2) // 2
#         perimeter = a + b + c
#         if m == 1 and perimeter > wire_len:
#             break
#
#         for per in takewhile(lambda x: x <= wire_len, (perimeter * i for i in count(1))):
#             if per in found_per:
#                 rep_per.add(per)
#             else:
#                 found_per.add(per)
#     print('runtime:', time.time() - start)
#     print('ans:', len(found_per - rep_per))
#
#
# find_hits()

# p075_alt.py  project euler forum python solution (kzi, germany (i think))
from time import time
from math import gcd

start = time()


# implemented from wikipedia (project euler forum) cuemath (mem)
def pyth_trip_gen(num):
    m_limit = int((num // 2) ** 0.5)
    for m in range(2, m_limit):  # m > n
        for n in range(1, m):
            if m % 2 == 0 or n % 2 == 0:
                if gcd(m, n) == 1:
                    m_sqr = m * m
                    n_sqr = n * n
                    yield 2*m*n, m_sqr - n_sqr, m_sqr + n_sqr


wire_length = 1_500_000
# wire_length = 100
lst_count = [0] * (wire_length + 1)

for trip in pyth_trip_gen(wire_length):
    length = sum(trip)
    # print(length, end=', ')
    if length <= wire_length:
        for perimeter in range(length, len(lst_count) + 1, length):
            # print(perimeter, end=', ')
            lst_count[perimeter] += 1
# print()
print(lst_count.count(1))
print(f'time: {time() - start} sec')
