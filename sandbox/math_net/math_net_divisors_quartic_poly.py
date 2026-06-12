# =============================================================================
# Jim McCleery
# June 12, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2025_e0e454
# =============================================================================

# Calculate the target number directly based on the mathematical problem.
# Equation used: 3 * (n + 3) * (n**2 + 9) where n = -2
# 3 * (-2 + 3) * ((-2)**2 + 9) -> 3 * 1 * (4 + 9) = 39
target = 39

# Initialize a variable to keep track of the running sum of valid 'n' values.
divisor_sum = 0

# Loop through all integers 'n' from 1 up to and including the target number.
# range(1, target + 1) starts at 1 and stops right before target + 1 (which includes target).
for n in range(1, target + 1):
    
    # We want to check if (target) is perfectly divisible by (n + 2).
    # In Python, the modulo operator (%) calculates the remainder of a division.
    # If the remainder is 0, it means (n + 2) divides evenly into the target.
    if target % (n + 2) == 0:
        # If it divides evenly, add the current value of 'n' to our running total.
        divisor_sum += n

# Print the final calculated result to the screen.
print(divisor_sum)
