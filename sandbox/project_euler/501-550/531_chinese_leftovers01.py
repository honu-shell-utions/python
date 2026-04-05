#  -----------------------------------------------------------------------------
#  Chinese leftovers
#  Problem 531
#  https://projecteuler.net/problem=531
#  
#  Let g(a,n,b,m) be the smallest non-negative solution x to the system:
#  x = a mod n
#  x = b mod m
#  if such a solution exists, otherwise 0.
#  
#  E.g. g(2,4,4,6)=10, but g(3,4,4,6)=0.
#  
#  Let φ(n) be Euler's totient function.
#  
#  Let f(n,m)=g(φ(n),n,φ(m),m)
#  
#  Find ∑ f(n,m) for 1000000 ≤ n < m < 1005000
#  -----------------------------------------------------------------------------
from sympy.ntheory.factor_ import totient
from sympy.ntheory.modular import solve_congruence
from time import time
#  -----------------------------------------------------------------------------
class euler_531:
    def __init__(self,n,m):
        self.a = totient(n)
        self.n = n
        self.b = totient(m)
        self.m = m
    #  ------------------------------------------------------------------------
    def get_sol(self):
        temp = solve_congruence((self.a,self.n),(self.b,self.m))
        if temp is not None:
            return temp[0]
        else:
            return 0
#  -----------------------------------------------------------------------------
bot = 10**6
top = bot + 5*10**3
result = 0
for m in range(bot+1,top):
    if m % 250 == 0:
        print(m, result)
    for n in range(bot,m):
        instance = euler_531(n,m)
        result += instance.get_sol()
print(result)
#  -----------------------------------------------------------------------------
#  solution: 4515432351156203105
#  -----------------------------------------------------------------------------
