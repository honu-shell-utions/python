def p217(n):
    def ceil_half(x):
        return (x+1)/2

    total = sum(range(1,10))

    if n < 1:
        return 0
    if n == 1:
        return total

    sums = []
    count = []
    max_length = ceil_half(n-2)*18
    for x in range(n+1):
        sums.append([0]*int(max_length+1))
        count.append([0]*int(max_length+1))
        
    # k = 0
    count[0][0] = 1
    
    # k = 1
    sums[1][0] = sum(range(1,10))
    count[1][0] = 10

    # delta with leading zeros
    delta = {}
    for x in range(-9,10):
        delta[x] = (0,0,0)
    for (a,b) in [(a,b) for a in range(10) for b in range(10)]:
        a1, b1, c1 = delta[a-b]
        delta[a-b] = a1+a, b1+b, c1+1

    # k 2+
    k_pow = 1
    for k in range(2,n-1):
        max_x = int(ceil_half(k-2)*9)
        k_pow *= 10
        
        for x in range(-max_x, max_x+1):
            prev_count = count[k-2][x]
            prev_sum = 10*sums[k-2][x]
            for d,(a,b,c) in delta.items():
                sums[k][x+d] += c*prev_sum + prev_count*(k_pow*a + b)
                count[k][x+d] += c*prev_count

            
    #calc values without leading zeros
    k_pow = 1
    for k in range(2,n+1):
        k_pow *= 10
        for x in range(-9, 10):
            prev_count = count[k-2][x]
            prev_sums = 10*sums[k-2][x]
            a,b,c = delta[-x]
            
            # adjust for leading zeros
            if x >= 0:
                b -= x
                c -= 1

            total += c*prev_sums + prev_count*(k_pow*a + b)

    return total

print(p217(47)%(3**15))
# 6273134
