keep = []
pwrs = []

for i in range(10):
    pwrs.append(i**5)

def pwr_sum(n):
    tally = 0
    while n > 0:
        tally += pwrs[n % 10]
        n //= 10
    return tally

def do_it():
    tally = 0
    for i in range(10, 9**5*6+1):  # 6*9^5 = 354294
        if i == pwr_sum(i):
            tally += i
            keep.append(i)
    return sum(keep),keep

print(do_it())
#solution: 443839
