#  -----------------------------------------------------------------------------
#  Polymorphic Bacteria
#  Problem 666
#  https://projecteuler.net/problem=666
#  -----------------------------------------------------------------------------
def r(n):
    ans = 306
    for i in range(n): 
            ans = ans**2 % 10007
    return ans
#  -----------------------------------------------------------------------------
k,m = 500,10
p = 1/float(m)
q = [[(r(c*m+j) % 5) for j in range(m)] for c in range(k)]
vec = [0.5 for char in range(k)]
vec2 = list(vec)

for count in range(10**3):
    for col in range(k):
        vec2[col] = 0
        for term in range(m):
            q_val = q[col][term]					
            if q_val == 0: vec2[col] += p
            if q_val == 1: vec2[col] += p * vec[col]**2
            if q_val == 2: vec2[col] += p * vec[(col*2) % k]
            if q_val == 3: vec2[col] += p * vec[(col**2 + 1) % k]**3
            if q_val == 4: vec2[col] += p * vec[col] * vec[(col+1) % k]
    vec = list(vec2)
    
print(round(vec[0],8))
#  -----------------------------------------------------------------------------
#  solution: 0.48023168
#  -----------------------------------------------------------------------------
