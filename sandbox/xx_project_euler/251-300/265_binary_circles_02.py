#  -----------------------------------------------------------------------------
#  Binary Circles
#  Problem 265
#  https://projecteuler.net/problem=265
#  -----------------------------------------------------------------------------
import time

def S(circle, circles, repository, n):
    total = 0
    if (len(repository) == 0):
        # Combine substrings if this is a valid circle
        if (circle[-1][1:] == circle[0][:n-1]):
            str_rep = ""
            for s in circle: str_rep += s[0]
            total += int(str_rep, 2)
        return total
    for i in range(len(repository)):
        s = repository[i]
        if (circle[-1][1:] == s[:n - 1]):
            repository.pop(i)
            total += S(circle + [s], circles, repository, n)
            repository.insert(i, s)
    return total

n = 5
start_time = time.time()
# Generate all binary representations of the numbers from 0 to 2^n - 1 with leading zeros
repository = []
for x in range(1, 2 ** n):
    s = bin(x)[2:]
    repository.append((n - len(s)) * "0" + s)
circles = []
print(S(["0" * n], circles, repository, n))
print(time.time() - start_time)
#  -----------------------------------------------------------------------------
#  solution: 209110240768
#  -----------------------------------------------------------------------------
