from sympy import nextprime

def F(n):
    return((7*n+15)/(18*n+18))

simulated = 0
prime = 3
count = 0
while prime < 10**6:
    count += 1
    simulated += F(prime)
    prime = nextprime(prime)

print(f'Project Euler #826: {simulated/count:.10f}')

           
    
