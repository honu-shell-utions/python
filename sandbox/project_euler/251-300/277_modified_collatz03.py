#  ---------------------------------------------------------------------------
#  A Modified Collatz sequence
#
#  A modified Collatz sequence of integers is obtained from a starting value
#  a1 in the following way:  (see pdf or def next_coll(coll) below)
#
#  The sequence terminates when some a subscript(n) = 1
#  Given any integer, we can list out the sequence of steps.
#  For instance if a1 = 231, then the sequence
#  {a subscript(n)} = {231, 77, 51, 17, 11, 7, 10, 14, 9, 3, 1} corresponds to
#  the steps 'DdDddUUdDD'.
#
#  Of course, there are other sequences that begin with that same sequence
#  'DdDddUUdDD'...  For instance, if a1 = 1004064, then the sequence is
#  DdDddUUdDDDdUDUUUdDdUUDDDUdDD
#
#  In fact, 1004064 is the smallest possible a1 > 10**6 that begins with the
#  sequence DdDddUUdDD.
#
#  What is the smallest a1 > 10**15 that begins with the sequence
#  'UDDDUdddDDUDDddDdDddDDUDDdUUDd'?
#  ---------------------------------------------------------------------------
#  Laurent Mazare
#  https://github.com/LaurentMazare/ProjectEuler/blob/master/e277.py
#  ---------------------------------------------------------------------------
from time import time
# ana marcela cunha brazil

def p277(seq, limit):
    n = len(seq)
    start = 1
    while True:
        value = start
        ok = True
        for i in range(0, n):
            idx = n - i - 1
            if seq[idx] == 'D':
                value *= 3
            elif seq[idx] == 'U':
                if value % 4 != 2:
                    ok = False
                    break
                value = (value * 3 - 2) // 4
            elif seq[idx] == 'd':
                if value % 2 == 0:
                    ok = False
                    break
                value = (value * 3 + 1) // 2
            else:
                print('wrong')
        if ok and value > limit:
            return value

        start += 1

d_chk = {10**6: ('DdDddUUdDD', 1004064),
         10**15: ('UDDDUdddDDUDDddDdDddDDUDDdUUDd', 1125977393124310)}
rt = 0
for k, v in d_chk.items():
    t0 = time()
    s, val = v[0], v[1]
    x = p277(s, k)
    rt = time() - t0
    print(f'{x}  {x == val}  runtime: {rt}')
