"""
Jim McCleery
April 4, 2026
Kailua-Kona, HI

Credit to tolstopuz on Project Euler

----------------------------------------------------------------------
OVERVIEW
----------------------------------------------------------------------

This program computes a special sum arising from number theory.

The mathematics behind it is advanced. In particular, it uses:

    1. modular inverses
    2. the Kronecker symbol
    3. modular square roots
    4. lifting solutions from p to p^e
    5. binary quadratic forms
    6. reduction of forms
    7. cycles of reduced forms

Even though the mathematics is sophisticated, we can still organize
the code so that students can follow the FLOW of the computation.

----------------------------------------------------------------------
HIGH-LEVEL IDEA
----------------------------------------------------------------------

We loop over integers m and form

        n = m(m + 1).

For each such n, we build a certain quadratic form and compute
associated integer representatives.  From those representatives we
extract integers b satisfying specific parity and size conditions.

All valid b-values are stored in a set so duplicates are removed.
At the end we print the sum of all distinct values.

----------------------------------------------------------------------
PROGRAM STRUCTURE
----------------------------------------------------------------------

Part A.  Arithmetic helper functions
Part B.  Solving x^2 ≡ d (mod 4n)
Part C.  Binary quadratic forms
Part D.  Main search
"""

import math
import random
import itertools


# -------------------------------------------------------------------
# GLOBAL CONSTANT
# -------------------------------------------------------------------

# Upper bound used in the final search.
N_MAX = 10**10


# ===================================================================
# PART A. ARITHMETIC HELPER FUNCTIONS
# ===================================================================

def modular_inverse(a, modulus):
    """
    Return the multiplicative inverse of a modulo 'modulus'.

    In other words, this returns a number x such that

        a*x ≡ 1 (mod modulus)

    provided gcd(a, modulus) = 1.

    ---------------------------------------------------------------
    HOW IT WORKS
    ---------------------------------------------------------------
    This uses the extended Euclidean algorithm.

    If gcd(a, modulus) = 1, then there exist integers x and y such that

        ax + modulus*y = 1.

    Reducing mod 'modulus' gives

        ax ≡ 1 (mod modulus),

    so x is the modular inverse.

    ---------------------------------------------------------------
    NOTE
    ---------------------------------------------------------------
    The original code named this function 'egcd', but in practice
    it was being used specifically as a modular inverse routine.
    """
    x, y, u, v, original_modulus = 0, 1, 1, 0, modulus

    while modulus != 0:
        q = a // modulus
        a, modulus = modulus, a % modulus
        x, u = u - q * x, x
        y, v = v - q * y, y

    return u if u > 0 else u + original_modulus


def kronecker_symbol(m, n):
    """
    Compute the Kronecker symbol (m/n).

    ---------------------------------------------------------------
    WHY THIS MATTERS
    ---------------------------------------------------------------
    This is a generalization of the Legendre symbol and Jacobi symbol.
    In this program it is used to test whether a number is a quadratic
    residue modulo another number.

    Roughly speaking, it helps answer the question:

        "Does x^2 ≡ m (mod n) have a solution?"

    ---------------------------------------------------------------
    OUTPUT
    ---------------------------------------------------------------
    The function returns one of:

        1   if m behaves like a quadratic residue modulo n
       -1   if it behaves like a non-residue
        0   in certain degenerate divisibility cases
    """
    if n % 2 == 0 and m % 2 == 0:
        return 0

    sign = -1 if m < 0 and n < 0 else 1
    m, n = abs(m), abs(n)

    # Remove factors of 2 from n
    while n % 2 == 0:
        if m % 8 in (3, 5):
            sign = -sign
        n //= 2

    m %= n

    while m != 0:
        # Remove factors of 2 from m
        while m % 2 == 0:
            if n % 8 in (3, 5):
                sign = -sign
            m //= 2

        # Quadratic reciprocity sign change
        if m % 4 == 3 and n % 4 == 3:
            sign = -sign

        m, n = n % m, m

    return sign if n == 1 else 0


# ===================================================================
# PART B. SOLVING x^2 ≡ d (mod 4n)
# ===================================================================

def sqrt_mod_prime(r, p):
    """
    Solve the congruence

        x^2 ≡ r (mod p)

    where p is an odd prime.

    ---------------------------------------------------------------
    MATHEMATICAL IDEA
    ---------------------------------------------------------------
    This is a Tonelli-Shanks-type method for computing modular square
    roots.

    The code assumes a solution exists.

    ---------------------------------------------------------------
    OUTLINE
    ---------------------------------------------------------------
    1. Write p - 1 = m * 2^t with m odd
    2. Find a quadratic non-residue c mod p
    3. Use repeated corrections until the residue becomes 1
    4. Reconstruct the square root
    """
    m = p - 1
    t = 0

    while m % 2 == 0:
        t += 1
        m //= 2

    # Find a quadratic non-residue mod p.
    c = 1
    while kronecker_symbol(c, p) == 1:
        c = random.randrange(1, p)

    c_inverse = modular_inverse(c, p)

    residue_part = pow(r, m, p)
    correction_part = pow(c_inverse, m, p)

    exponent = 0
    i = 0

    while residue_part != 1:
        i += 1
        correction_part = pow(correction_part, 2, p)

        if pow(residue_part, 2 ** (t - i - 1), p) != 1:
            exponent += 2 ** i
            residue_part = (residue_part * correction_part) % p

    a = (r * pow(c_inverse, exponent, p)) % p
    return (pow(c, exponent // 2, p) * pow(a, (m + 1) // 2, p)) % p


def sqrt_mod_4p(d, p):
    """
    Solve x^2 ≡ d (mod 4p) in the basic prime case.

    This function is a helper used later when we solve modulo higher
    prime powers p^e.
    """
    if p == 2:
        # Special case for p = 2
        return 1 if d % 2 != 0 else 2 * ((d // 4) % 2)

    if d % p == 0:
        # If d is divisible by p, there is a simpler structure
        return 0 if d % 2 == 0 else p

    # Otherwise solve mod p and adjust parity so it works mod 4p
    r = sqrt_mod_prime(d, p)
    return r if r % 2 == d % 2 else p - r


def sqrt_mod_4prime_power(d, p, e):
    """
    Solve

        x^2 ≡ d (mod 4*p^e)

    and return all relevant solutions as a list.

    ---------------------------------------------------------------
    BIG PICTURE
    ---------------------------------------------------------------
    This is the heart of the modular-square-root machinery.

    There are three main cases:

    Case 1. d is divisible by p and e > 1
    Case 2. d is divisible by p but we are only at the base level
    Case 3. d is not divisible by p

    If no solution exists, return the empty list [].
    """
    if d % p == 0 and e > 1:
        # We look for the largest n such that p^(2n) divides d.
        n = 0
        while 2 * n + 2 <= e and d % p ** (2 * n + 2) == 0:
            n += 1

        # Adjustment for the special p = 2 case
        if p == 2 and n > 0 and (d // 2 ** (2 * n)) % 4 >= 2:
            n -= 1

        if n == 0:
            return []

        d0 = d // p ** (2 * n)
        e0 = e - 2 * n

        # Recursively solve the smaller problem
        if e0 == 0:
            smaller_solutions = [d0 % 2]
        else:
            smaller_solutions = sqrt_mod_4prime_power(d0, p, e0)

        return [
            p ** n * (x + 2 * k * p ** e0)
            for k in range(p ** n)
            for x in smaller_solutions
        ]

    elif d % p == 0:
        return [sqrt_mod_4p(d, p)]

    elif kronecker_symbol(d, p) == -1:
        # No square root exists mod p, so no lifted solution exists
        return []

    else:
        # Start with a base solution modulo 4p
        b = sqrt_mod_4p(d, p)
        b_inverse = modular_inverse(b, p)

        # Lift from p to p^2, p^3, ..., p^e
        for f in range(1, e):
            k = b_inverse * (d - b ** 2) // (4 * p ** f) % p
            b = (b + 2 * k * p ** f) % (2 * p ** (f + 1))

        x = b - 2 * p ** e if b > p ** e else b
        return [x, -x] if x != 0 else [x]


def factor_integer(n):
    """
    Return the prime factorization of n as a dictionary.

    Example:
        factor_integer(360) returns
            {2: 3, 3: 2, 5: 1}

    because
        360 = 2^3 * 3^2 * 5.
    """
    factors = {}

    for p in range(2, int(math.sqrt(n) + 1)):
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent:
            factors[p] = exponent

    if n > 1:
        factors[n] = 1

    return factors


def sqrt_mod_4n(d, n):
    """
    Solve

        x^2 ≡ d (mod 4n)

    by breaking n into prime powers.

    ---------------------------------------------------------------
    STRATEGY
    ---------------------------------------------------------------
    1. Factor n
    2. Solve separately modulo each prime power
    3. Recombine the solutions using a Chinese-remainder-style step
    4. Normalize the answer into a convenient range
    """
    factorization = factor_integer(n)

    # For each prime p dividing n, solve modulo 4*p^e
    local_solutions = {
        p: sqrt_mod_4prime_power(d, p, factorization[p])
        for p in factorization
    }

    # We need the modulus 4n, so powers of 2 must be handled carefully.
    if 2 not in factorization:
        local_solutions[2] = [d % 4]
        factorization[2] = 2
    else:
        factorization[2] += 2

    def normalize_solution(x):
        """
        Put x into a symmetric-looking interval.

        This does not change the congruence class mod 4n.
        It just gives a cleaner representative.
        """
        x %= 4 * n

        if x > 3 * n:
            return x - 4 * n
        elif x > n:
            return x - 2 * n
        else:
            return x

    # CRT-style recombination coefficients
    crt_coefficients = {
        p: (4 * n // p ** factorization[p]) *
           modular_inverse(4 * n // p ** factorization[p], p ** factorization[p])
        for p in factorization
    }

    # Build all combinations of local solutions
    all_combinations = itertools.product(
        *([(p, solution) for solution in local_solutions[p]] for p in local_solutions)
    )

    return [
        normalize_solution(sum(crt_coefficients[p] * solution for p, solution in combo))
        for combo in all_combinations
    ]


# ===================================================================
# PART C. BINARY QUADRATIC FORMS
# ===================================================================

def forms(discriminant, n):
    """
    Construct all forms of the shape

        (n, b, c)

    having the given discriminant.

    Recall that a binary quadratic form is written

        ax^2 + bxy + cy^2

    and its discriminant is

        D = b^2 - 4ac.

    Here a = n, so once b is known, c is forced by

        c = (b^2 - D) / (4n).
    """
    return [
        (n, b, (b ** 2 - discriminant) // (4 * n))
        for b in sqrt_mod_4n(discriminant, n)
    ]


def primitive_forms(discriminant, n):
    """
    Keep only primitive forms.

    A form (a, b, c) is primitive if gcd(a, b, c) = 1.
    """
    return [
        (a, b, c)
        for a, b, c in forms(discriminant, n)
        if math.gcd(math.gcd(abs(a), abs(b)), abs(c)) == 1
    ]


def shift_for_rho(form):
    """
    Compute the integer shift used in the rho transformation.
    """
    a, b, c = form

    value = (
        max(abs(c), math.sqrt(b ** 2 - 4 * a * c)) + b
    ) / (2 * abs(c))

    s = int(math.floor(value))
    return s if c > 0 else -s


def shift_for_normalize(form):
    """
    Compute the integer shift used in the initial normalization step.
    """
    a, b, c = form

    value = (
        max(abs(a), math.sqrt(b ** 2 - 4 * a * c)) - b
    ) / (2 * abs(a))

    s = int(math.floor(value))
    return s if a > 0 else -s


def matrix_multiply(A, B):
    """
    Multiply two 2x2 integer matrices.

    We store a matrix

        [a  b]
        [c  d]

    as the 4-tuple

        (a, b, c, d).
    """
    a1, b1, c1, d1 = A
    a2, b2, c2, d2 = B

    return (
        a1 * a2 + c1 * b2,
        b1 * a2 + d1 * b2,
        a1 * c2 + c1 * d2,
        b1 * c2 + d1 * d2
    )


def matrix_inverse(A):
    """
    Invert a 2x2 unimodular integer matrix.

    For a matrix

        [a  b]
        [c  d]

    with determinant ±1, the inverse is again integral.
    """
    a, b, c, d = A
    det = a * d - b * c
    return (d // det, -b // det, -c // det, a // det)


def normalize_form(form):
    """
    Perform the initial normalization step for a binary quadratic form.

    Returns:
        normalized form,
        associated transformation matrix
    """
    a, b, c = form
    s = shift_for_normalize(form)

    new_form = (
        a,
        b + 2 * s * a,
        a * s ** 2 + b * s + c
    )

    transform = (1, 0, s, 1)

    return new_form, transform


def rho(form, transform):
    """
    Perform one reduction step.

    In the theory of binary quadratic forms, this moves one form to
    another equivalent one, while updating the transformation matrix.
    """
    a, b, c = form
    s = shift_for_rho(form)

    r, u, t, v = transform

    new_form = (
        c,
        -b + 2 * s * c,
        c * s ** 2 - b * s + a
    )

    new_transform = (
        t,
        v,
        -r + s * t,
        -u + s * v
    )

    return new_form, new_transform


def is_reduced(form):
    """
    Test whether a form is reduced.

    This uses the exact criterion from the original program.
    """
    a, b, c = form
    sqrt_D = math.sqrt(b ** 2 - 4 * a * c)
    return abs(sqrt_D - 2 * abs(a)) < b < sqrt_D


def reduce_form(form):
    """
    Reduce a form by:
        1. normalizing it
        2. repeatedly applying rho until it is reduced
    """
    current_form, current_transform = normalize_form(form)

    while not is_reduced(current_form):
        current_form, current_transform = rho(current_form, current_transform)

    return current_form, current_transform


def cycle_of_form(start_form):
    """
    Follow the rho-orbit starting from a reduced form until the cycle
    closes.

    Returns:
        cycle_map      dictionary from forms to transformation matrices
        automorphism   the transformation corresponding to one full loop
    """
    cycle_map = {}
    current_form = start_form
    current_transform = (1, 0, 0, 1)

    while True:
        cycle_map[current_form] = current_transform
        current_form, current_transform = rho(current_form, current_transform)

        if current_form == start_form:
            return cycle_map, current_transform


def representatives(base_form, n):
    """
    Compute integer representatives associated with the given base form.

    ---------------------------------------------------------------
    IDEALIZED DESCRIPTION
    ---------------------------------------------------------------
    1. Normalize the base form
    2. Compute all primitive forms of the same discriminant
    3. Reduce each primitive form
    4. Check whether it lands in the reduction cycle of the base form
    5. If it does, recover integer matrix data that yields a pair [x, y]

    ---------------------------------------------------------------
    IMPORTANT
    ---------------------------------------------------------------
    This is conceptually the most difficult part of the program.
    Students should not expect to understand every number-theoretic
    detail immediately.  The main programming lesson is to observe
    how a complicated mathematical process can still be broken into
    named steps.
    """
    result = []

    base_form, base_transform = normalize_form(base_form)
    a, b, c = base_form
    discriminant = b ** 2 - 4 * a * c

    all_primitive_forms = primitive_forms(discriminant, n)
    cycle_map, automorphism = cycle_of_form(base_form)

    for form in all_primitive_forms:
        reduced_form, reduction_transform = reduce_form(form)

        if reduced_form in cycle_map:
            current_cycle_transform = cycle_map[reduced_form]

            while True:
                composed = matrix_multiply(
                    base_transform,
                    matrix_multiply(
                        current_cycle_transform,
                        matrix_inverse(reduction_transform)
                    )
                )

                if composed[0] > 3 * N_MAX or composed[1] > 3 * N_MAX:
                    break

                result.append([composed[0], composed[1]])
                current_cycle_transform = matrix_multiply(
                    automorphism,
                    current_cycle_transform
                )

    return result


# ===================================================================
# PART D. MAIN SEARCH
# ===================================================================

def main():
    """
    Execute the full computation.

    ---------------------------------------------------------------
    WHAT HAPPENS HERE
    ---------------------------------------------------------------
    For each m from 1 up to sqrt(N_MAX):

        n = m(m + 1)

    Then for each square divisor k^2 of n, we compute representatives
    attached to the form

        (m, 0, -m - 1)

    but at the reduced level n / k^2.

    The resulting x, y pairs are converted into integers a, b.
    Only those meeting the parity and size conditions are kept.

    All admissible b-values are stored in a set to avoid duplicates.
    """
    values = set()

    for m in range(1, int(math.sqrt(N_MAX)) + 1):
        n = m * (m + 1)
        discriminant = 4 * n

        for k in range(1, int(math.sqrt(n)) + 1):
            if n % (k ** 2) == 0:
                base_form = (m, 0, -m - 1)
                reduced_n = n // (k ** 2)

                for x, y in representatives(base_form, reduced_n):
                    # Undo the earlier square-factor scaling
                    x *= k
                    y *= k

                    # If both are negative, flip signs so we use a
                    # standard representative.
                    if x < 0 and y < 0:
                        x = -x
                        y = -y

                    # These parity conditions guarantee that a and b
                    # below are integers.
                    if (x - m - 1) % 2 == 0 and (y + m) % 2 == 0:
                        a = (x - m - 1) // 2
                        b = (y + m) // 2

                        # Keep only the values satisfying the final
                        # order and size conditions.
                        if a >= b and b <= N_MAX:
                            values.add(b)

    print(sum(values))


# -------------------------------------------------------------------
# Standard Python entry point
# -------------------------------------------------------------------
if __name__ == "__main__":
    main()
