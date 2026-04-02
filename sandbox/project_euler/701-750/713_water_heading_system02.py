from math import factorial,comb

def T(N, m):
  k = m - 1
  res = (k - N % k)*comb(N//k,2) + (N % k)*comb(N//k+1,2)
  return res

def L(N):
  total = 0
  for m in range(2,N+1):
    total += T(N,m)
  return total

print('T(3,2)=',T(3,2))
print('T(8,4)=',T(8,4))
print('L(10**3)=',L(10**3))
print('L(10**7)=',L(10**7))
#  solution: 788626351539895
