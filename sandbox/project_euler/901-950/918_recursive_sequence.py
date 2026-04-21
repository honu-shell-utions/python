import time

"""
https://projecteuler.net/problem=918
"""

def a(n):
    """
    Compute the nth term of the underlying sequence.

    The algorithm uses an efficient binary-walking method rather than
    building the sequence term by term.  At each stage we maintain a pair

        (a(m), a(m+1))

    and update that pair according to the next bit in the binary expansion
    of n.

    This makes the computation very fast, requiring only O(log n) steps.
    """
    # Initial terms of the sequence
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Begin with the known pair (a(1), a(2))
    x, y = 1, 2

    # Convert n to binary and skip the leading '0b1'.
    # The remaining bits tell us how to move from smaller indices
    # to the desired index n.
    for bit in bin(n)[3:]:
        if bit == '0':
            # Transition corresponding to appending a 0-bit:
            # from (a(m), a(m+1)) to (a(2m), a(2m+1))
            x, y = 2 * x, x - 3 * y
        else:
            # Transition corresponding to appending a 1-bit:
            # from (a(m), a(m+1)) to (a(2m+1), a(2m+2))
            x, y = x - 3 * y, 2 * y

    # After all bits have been processed, x = a(n)
    return x


def sum_seq(lim):
    """
    Compute the partial sum up to lim using a closed formula.

    Rather than summing terms one at a time, this function uses the identities

        S(2k)   = 4 - a(k)
        S(2k-1) = 4 - 3a(k)

    where S(lim) denotes the required partial sum.

    This reduces the problem to evaluating a single sequence term.
    """
    if lim == 0:
        return 0

    if lim % 2 == 0:
        # If lim = 2k, use S(2k) = 4 - a(k)
        return 4 - a(lim // 2)
    else:
        # If lim = 2k - 1, equivalently k = (lim + 1) // 2,
        # use S(2k - 1) = 4 - 3a(k)
        return 4 - 3 * a((lim + 1) // 2)


# Evaluate the partial sum at n = 10^12
n = 10**12

# Start timing the computation
start_time = time.perf_counter()

# Print the result
print('n =\t', n, '\tSum =', sum_seq(n))

# Stop timing
end_time = time.perf_counter()

# Report elapsed runtime
print(f"Execution time: {end_time - start_time:.6f} seconds\n")
