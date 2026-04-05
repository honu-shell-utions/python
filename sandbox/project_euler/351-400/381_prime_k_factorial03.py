from sympy import primerange

prime = primerange(5,10**8)

sum_s = 0
for i in prime:
    a = i%8
    b = i//8
    if a == 1:
        sum_s += 3*b
    elif a == 3:
        sum_s += b
    elif a == 5:
        sum_s += 7*b + 4
    elif a == 7:
        sum_s += 5*b + 4
        
print(sum_s)
# 139602943319822	
