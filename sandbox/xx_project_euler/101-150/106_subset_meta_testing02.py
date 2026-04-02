from math import factorial

def catalan(n,s):
    f1 = factorial(n)/(factorial(s)*factorial(n-s))
    f2 = factorial(n-s)/(factorial(s)*factorial(n-2*s))
    f3 = factorial(2*s)/(factorial(s)*factorial(s))
    f4 = factorial(n)/(factorial(2*s)*factorial(n-2*s))

    return .5*f1*f2 - 1/(s+1) * f3 * f4

print(4,2,catalan(4,2))
print(5,2,catalan(5,2))
print(6,2,catalan(6,2))
print(6,3,catalan(6,3))
print(7,2,catalan(7,2))
print(7,3,catalan(7,3))
print(12,2,catalan(12,2))
print(12,3,catalan(12,3))
print(12,4,catalan(12,4))
print(12,5,catalan(12,5))
print(12,6,catalan(12,6))

  
