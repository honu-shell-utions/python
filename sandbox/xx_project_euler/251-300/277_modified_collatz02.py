#  -----------------------------------------------------------------------------
#  A Modified Collatz sequence
#  Problem 277
#  -----------------------------------------------------------------------------
def next_coll(coll):
    if coll % 3 == 0:
        return coll//3, 'D'
    if coll % 3 == 1:
        return (4*coll+2)//3, 'U'
    return (2*coll-1)//3, 'd'
#  -----------------------------------------------------------------------------
def make_seq(begin_at):
    coll_seq_nums = []
    coll_seq_letters = []
    n, d = next_coll(begin_at)
    coll_seq_nums.append(n)
    coll_seq_letters.append(d)
    while coll_seq_nums[-1] != 1:
        n, d = next_coll(coll_seq_nums[-1])
        coll_seq_nums.append(n)
        coll_seq_letters.append(d)
    return coll_seq_nums,''.join(coll_seq_letters)
#  -----------------------------------------------------------------------------
def test_sol(n,target):
    seq_nums, seq_letters = make_seq(n)
    if target == ''.join(seq_letters[:len(target)]):
        print('----------------------------------')
        print('for n =',n)
        print('----------------------------------')
        print(seq_nums)
        print('----------------------------------')
        print(seq_letters)
        print('----------------------------------')
        return True
    return False
#  -----------------------------------------------------------------------------
def make_sol(n):
    x = 205891132094649*n+96521732651065
    return x
#  -----------------------------------------------------------------------------
target = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'
for n in range(2,10**10):
    x = make_sol(n)
    if x < 10**15:
        continue
    if test_sol(x,target):
        break
#  -----------------------------------------------------------------------------
#  solution: 1125977393124310
#  -----------------------------------------------------------------------------
