##Given line passing through origin, let
##s = # points on line
##L = # points on line to left of origin
##R = # points on line to right of origin
##a = # points to left of line
##b = # points to right of line
##
##Add
##s * (2ab - nCr(a,2) - nCr(b,2)) + (a+b) * (nCr(R,2) + nCr(L,2) - 2LR)
##to sum
##
##sum will be the number of triangles containing the origin multiplied by 6.
##Why?
##because one will add 2,2,2 for each valid triangle, and either 2,-1,-1 or
##-1,0.5,0.5 for each invalid triangle.

from time import time

start = time()
N = 2*10**6
x,y = 1,1
P = []
for n in range(N):
    x = x * 1248 % 32323
    y = y * 8421 % 30103
    P.append((x-16161,y-15051))
P.sort(key=lambda a: (1,a[1]) if a[0]==0 else (0,float(a[1])/a[0]))

i = 0
Q = []
while i < N:
    t = [P[i]]
    j = i+1
    while j < N and P[i][0]*P[j][1] == P[i][1]*P[j][0]:
        t.append(P[j])
        j += 1
    Q.append(t)
    i = j

a,b = 0,0
slope = float(P[0][1])/P[0][0]
for point in P:
    if P[0][0]*point[1] == P[0][1]*point[0]:
        if point[point[0]==0] > 0:
            a += 1
        else:
            b += 1
    elif point[1] > slope * point[0]:
        a += 1
    else:
        b += 1

ans = 0
pL,pR = 0,0
for line in Q:
    s = len(line)
    if line[0][0] == 0:
            L = sum(point[1]<0 for point in line)
    else:
            L = sum(point[0]<0 for point in line)
    R = len(line) - L
    a,b = a + pL - R, b + pR - L
    pL,pR = L,R
    ans += s * (2*a*b - a*(a-1)//2 - b*(b-1)//2) + (a+b) * (R*(R-1)//2 + L*(L-1)//2 - 2*L*R)

print(ans//6,time()-start)
#solution: 333333208685971546
