#  -----------------------------------------------------------------------------
#  x**y = y**x (mod n)
#  Problem 801
#  https://projecteuler.net/problem=801
#  -----------------------------------------------------------------------------
import matplotlib.pyplot as plt
from random import randint
#  -----------------------------------------------------------------------------
def f(n):
    count = 0
    xy = []
    for x in range(1,n**2-n+1):
        for y in range(1,n**2-n+1):
            if x == y:
                count += 1
                xy.append((x,y))
                continue
            lhs = pow(x,y,n)
            rhs = pow(y,x,n)
            if lhs == rhs:
                count += 1
                xy.append((x,y))
    return count,xy
#  -----------------------------------------------------------------------------
fig, ax = plt.subplots()
#plt.axis('off')
ax.set_aspect('equal', adjustable='datalim')
count,xy = f(5)
for x,y in xy:
    plt.plot(x,y,'o') 
ax.plot()
plt.show() 
plt.close(fig)
print(count)
#  -----------------------------------------------------------------------------
#  solution: 638129754
#  -----------------------------------------------------------------------------
