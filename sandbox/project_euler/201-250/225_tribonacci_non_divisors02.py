ele = []
i = 1
while(len(ele) < 124):
    a0 = 1
    a1 = 1
    a2 = 1
    while True:
        a0, a1, a2 = a1, a2, (a1+a2+a0)%i
        if([a0, a1, a2] == [1,1,1]):
            ele.append(i)
            break
        if(a2 == 0):
            break
    i += 2

print(ele[123])
