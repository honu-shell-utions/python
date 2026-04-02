
n, a1, b1, a2, b2 = 2, 1, 1, 1, 1
while True:
    n += 1
    a1, b1 = a1 + b1, a1
    a2, b2 = a2 + b2, a2
    if a1 >= 10**15:
        a1 //= 10
        b1 //= 10
    a2 %= 10**9
    if ''.join(sorted(str(a1)[:9])) != "123456789": continue
    if ''.join(sorted(str(a2))) != "123456789": continue
    print(n)
    break

#329468
