#Project Euler Problem 88

def prodsum(p, s, c, start):
    k = p - s + c     # product - sum + number of factors
    if k < kmax:
        if p < n[k]:
            n[k] = p
        for i in range(start, kmax//p * 2):
            prodsum(p*i, s+i, c+1, i)

kmax = 12_000
n = [2*kmax] * kmax    # the minimal product-sum is < 2*k + 1 
prodsum(1, 1, 1, 2)

#  convert to set to remove duplicates from slice of n
print("Project Euler 88 Solution =", sum(set(n[2:])))

# k=2: 4 = 2 × 2 = 2 + 2
# k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
# k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
# k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
# k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6
