#  -----------------------------------------------------------------------------
#  Polymorphic Bacteria
#  Problem 666
#  https://projecteuler.net/problem=666
#  -----------------------------------------------------------------------------
import itertools
#  -----------------------------------------------------------------------------
def solve(k, m):
    rand = [306]
    for i in range(k * m):
        rand.append(rand[-1] ** 2 % 10007)

    possibilities = [0.5] * k
    for iteration in itertools.count(1):
        new_p = []

        for i in range(k):
            p = 0
            for j in range(m):
                q = rand[i * m + j] % 5
                if q == 0:
                    p += 1
                elif q == 1:
                    p += possibilities[i] ** 2
                elif q == 2:
                    p += possibilities[2 * i % k]
                elif q == 3:
                    p += possibilities[(i * i + 1) % k] ** 3
                elif q == 4:
                    p += possibilities[i] * possibilities[(i + 1) % k]
            p /= m
            new_p.append(p)

        if max(abs(p1 - p2) for p1, p2 in zip(possibilities, new_p)) < 1e-10:
            break
        possibilities = new_p
        
    return round(possibilities[0],8)
#  -----------------------------------------------------------------------------
print(solve( 2, 2))
print(solve( 4, 3))
print(solve(10, 5))
print(solve(500, 10))
#  -----------------------------------------------------------------------------
#  solution: 0.48023168
#  -----------------------------------------------------------------------------
