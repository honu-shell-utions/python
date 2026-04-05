#from: https://oeis.org/search?q=9%2C18%2C270%2C603%2C8307&language=english&go=Search
def a(n):
    r=[0, 9, 18, 270, 603]
    for i in range(n):
        r.append(-((1440+720*i)*r[i]+(-3024-1152*i)*r[1+i]+(1668+448*i)*r[2+i]+(-28-4*i)*r[3+i]+(-61-13*i)*r[4+i])//(5+i))
    return r[n]

MOD = 10**9+7
print(a(2022)%MOD)
