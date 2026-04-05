# Jim McCleery
# April 2, 2026
# Kailua-Kona, HI
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6, and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

LIMIT = 1000
total = 0

# Check every number from 1 up to (but not including) 1000.
for i in range(1, LIMIT):
    # Add the number if it is divisible by 3 or by 5.
    if i % 3 == 0 or i % 5 == 0:
        total += i

# Display the final sum.
print(total)

# Solution: 233168
