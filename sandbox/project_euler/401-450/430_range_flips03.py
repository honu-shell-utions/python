def E(n,k):
    return n/2 + n/(4*k+2)-1/2

print(round(E(3,1),2),10/9)
print(round(E(3,2),2),5/3)
print(round(E(10,4),2),5.157)
print(round(E(100,10),2),51.893)
print(round(E(10**10,4000),2),5000624921.38)
