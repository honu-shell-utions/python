
# Jim McCleery
# June 19, 2026
# Kailua-Kona, HI
#
# Solution for Project Euler Problem 832: Symmetric XOR Triples
# Problem URL: https://projecteuler.net/problem=832

MOD = 1_000_000_007

def get_triple_sum(n):
    """
    Finds the combined sum of the triple (a, b, a ^ b) generated in round 'n'.
    This function uses a base-4 recursive pattern hidden within the sequence.
    """
    # Base case: Round 0 means nothing happens, so the sum is 0.
    if n == 0:
        return 0
        
    # Pattern 1: If n divided by 4 leaves a remainder of 2,
    # the sum scales up by 4 without adding a constant offset.
    elif n % 4 == 2:
        return (get_triple_sum((n + 2) // 4) * 4) % MOD
        
    # Pattern 2: For all other remainders (0, 1, 3), the sum scales up by 4
    # and adds a base offset of 6.
    else:
        return (get_triple_sum((n + 2) // 4) * 4 + 6) % MOD


def M(n):
    """
    Calculates the total sum of all numbers written on the paper after 'n' rounds.
    The function uses structural math shortcuts so it can calculate huge values 
    (like 10^18) instantly instead of counting up one-by-one.
    """
    # Base case: If 0 rounds have passed, the sum is 0.
    if n == 0:
        return 0
        
    # Shortcut block: If n divided by 4 does NOT leave a remainder of 1,
    # we take the sum of this current round's triple and add it to the 
    # cumulative total of all previous rounds (n - 1).
    elif n % 4 != 1:
        return (get_triple_sum(n) + M(n - 1)) % MOD
        
    # Ultra-Fast Block Shortcut: If n % 4 == 1, we hit a perfect geometric 
    # boundary. We can skip thousands of calculations by scaling up a 
    # smaller, previously solved block (n // 4) using a factor of 16.
    else:
        high_bits_contribution = 6 * (n - n // 4)
        scaled_previous_blocks = 16 * M(n // 4)
        return (high_bits_contribution + scaled_previous_blocks) % MOD


# --- Test Cases & Verification ---

print(f"M(1)    = {M(1)}")        # Expected: 6
print(f"M(10)   = {M(10)}")       # Expected: 642
print(f"M(1000) = {M(10**3)}")    # Expected: 5432148

# Final Answer: Calculate M(10^18) MOD 1_000_000_007 .
final_answer = M(10**18) % MOD
print(f"M(10^18) modulo {MOD} = {final_answer}")

