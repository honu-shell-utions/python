# 48-selfPowers.py
#
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

limit = 1000

tally = 0
for i in range(1, limit+1):
    tally += i**i
print(tally)
print()
print(str(tally)[-10:])  # ans: 9110846700
