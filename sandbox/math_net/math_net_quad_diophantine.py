"""
Jim McCleery
May 5, 2026
Kailua-Kona, HI

Problem:
Find the number of ordered integer pairs (x, y), where
-100 <= x <= 100 and -100 <= y <= 100, satisfying

    12x^2 - xy - 6y^2 = 0

Source:
https://mathnet.mit.edu/explorer.html?p=usa_2025_cbdc6c
"""

BOUND = 100


def in_bounds(x: int, y: int, bound: int = BOUND) -> bool:
    """Return True if both coordinates are between -bound and bound."""
    return -bound <= x <= bound and -bound <= y <= bound


def main() -> None:
    """
    The equation factors as

        12x^2 - xy - 6y^2 = (3x + 2y)(4x - 3y)

    Therefore, every solution lies on one of two lines:

        3x + 2y = 0, giving (x, y) = (2k, -3k)
        4x - 3y = 0, giving (x, y) = (3k, 4k)

    We generate all integer points on both lines within the required bounds.
    A set is used so that the shared point (0, 0) is counted only once.
    """

    solutions: set[tuple[int, int]] = set()

    # Vertices/points on Line 1: 3x + 2y = 0
    # Parametric form: (x, y) = (2k, -3k)
    for k in range(-BOUND, BOUND + 1):
        x, y = 2 * k, -3 * k
        if in_bounds(x, y):
            solutions.add((x, y))

    # Vertices/points on Line 2: 4x - 3y = 0
    # Parametric form: (x, y) = (3k, 4k)
    for k in range(-BOUND, BOUND + 1):
        x, y = 3 * k, 4 * k
        if in_bounds(x, y):
            solutions.add((x, y))

    print(f"Number of solutions: {len(solutions)}")


if __name__ == "__main__":
    main()
