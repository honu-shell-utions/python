from math import factorial

def nCr(n, r):
    top = factorial(n)
    btm = factorial(n-r)*factorial(r)
    return top // btm


def F(m,n):
    Sum = 1
    for i in range(1,n):
        for k in range(i,n-i+1-(m-1)*i+1):
            Sum += nCr(k-1,i-1) * nCr(n-i+1-(m-1)*i-k+i,i)
    return Sum

n = 50
while F(50,n) < 1000000:
	n+=1
print (n)
