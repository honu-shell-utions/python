def tribonacci_gen():
    T1 = T2 = T3 = 1
    yield T1
    yield T2
    yield T3
    while True:
        yield T1+T2+T3
        T1,T2,T3 = T2,T3,T1+T2+T3

def is_divisor(n):
    for t in trib_list:
        if t % n == 0:
            return True
    return False

trib = tribonacci_gen()
trib_list = []
for _ in range(10**5):
    trib_list.append(next(trib))

num_non_divs = 0
non_divs_list = []
for n in range(3,10**6,2):
    if not is_divisor(n):
        num_non_divs += 1
        non_divs_list.append(n)
        if num_non_divs == 124:
            break
print(num_non_divs,non_divs_list[-1])
