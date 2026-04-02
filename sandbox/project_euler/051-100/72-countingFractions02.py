def find_factor(n) :
    for i in range(2, int(n**0.5 + 1)) :
        if n % i == 0 :
            return i
    return n
    
def find_factors(n) :
    factors = []
    while n != 1 :
        fac = find_factor(n)
        if fac not in factors :
            factors.append(fac)
        n /= fac
    return factors

def totient(n) :
    for factor in find_factors(n) :
        n = n * (factor - 1) / factor       
    return n
    
sum = 0
for i in range(2, 1000001) :
    sum += totient(i)
    
print(int(sum))
#303963552391
