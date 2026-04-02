#  -----------------------------------------------------------------------------
#  Shifted Pythagorean Triples
#  Problem 730
#  https://projecteuler.net/problem=730
#  -----------------------------------------------------------------------------
import sys
sys.setrecursionlimit(10**4)

def gcd(a,b):
   """ greatest common divisor of a and b """
   while b!=0:
      a,b  = b,a%b
   return a

def nsols(a,b,c,P):
   """ number of solutions with starting triple (a,b,c) and a+b+c<=P """
   if a+b+c>P: return 0
   S = 1 if a>0 else 0
   S += nsols(-2*a+b+2*c,-a+2*b+2*c,-2*a+2*b+3*c,P);
   if a>0: 
      S += nsols(2*a+b+2*c,a+2*b+2*c,2*a+2*b+3*c,P);
   if (a==0 and b>0 and b<c) or (a>0 and b>a):
      S += nsols(a-2*b+2*c,2*a-b+2*c,2*a-2*b+3*c,P);
   return S
   
def sols(a,b,c,P):
   """ all (generalized) solutions with starting triple (a,b,c) and c<=P """
   if c>P: return []
   S = [(a,b,c)]
   S += sols(-2*a+b+2*c,-a+2*b+2*c,-2*a+2*b+3*c,P);
   if a>0: 
      S += sols(2*a+b+2*c,a+2*b+2*c,2*a+2*b+3*c,P);
   if (a==0 and b>0 and b<c) or (a>0 and b>a):
      S += sols(a-2*b+2*c,2*a-b+2*c,2*a-2*b+3*c,P);
   return S

def findall(k,n):
   """ find all solutions (a,b,c) of a²+b²+k = c², with 0 <= a <= b <= c <= n and c>0 and gcd(a,b,c)=1 """
   L = list()
   for c in range(1,n+1):
      for b in range(0,c+1):
         for a in range(0,b+1):
            if gcd(a,gcd(b,c))==1 and a**2+b**2+k==c**2:
               L.append((a,b,c))
   return L
      
def findroots(k):
   """ find starting triples that generate all solutions of a²+b²+k = c² """
   n = k//2+2
   L = sorted(findall(k,n), key=lambda x:sum(x))
   R = []
   S = set()
   for a,b,c in L:
      if (a,b,c) not in S:
         R.append((a,b,c))
         S |= set(sols(a,b,c,n))
   return R
       
def S(m,n):
   s = 0
   for k in range(0,m+1):
      R = findroots(k)
      print("k={} --> roots={}".format(k,R))
      for a,b,c in R:
         s += nsols(a,b,c,n)
   return s

print(S(10**2,10**8))
#  -----------------------------------------------------------------------------
#  solution: 1315965924
#  -----------------------------------------------------------------------------
