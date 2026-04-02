# p020factorial_digit_sum.py
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
# Find the sum of the digits in the number 100!


n = 1
for i in range(100,0, -1):
    n *= i

s = str(n)
tally = 0
for i in s:
    tally += int(i)
print(tally)
#Solution: 648
