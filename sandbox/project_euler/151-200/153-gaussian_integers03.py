from math import gcd
from time import time

def euler153():
    NN = 10**4
    N = NN * NN
    total = 0
    for a in range(NN+1):
        for b in range(a,NN+1):
            if a == 0 and b == 0:
                continue
            if gcd(a, b) != 1:
                continue
            for delta in range(1,N+1):
                aa = a * delta
                bb = b * delta
                x = N // ((aa**2 + bb**2) // delta)
                if x == 0:
                    break
                if aa == 0:
                    total += bb * x
                elif aa == bb:
                    total += (aa + bb) * x 
                else:
                    total += 2 * (aa + bb) * x

    return int(total)

go = time()
print(euler153())
print(round(time()-go),'seconds')

# 10: 161
# 100: 16749
# 1000: 1752541
# 10000: 178231226
# 100000: 17924657155
# solution: 17971254122360635
