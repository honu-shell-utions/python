"""
Project Euler 286
Barbara's basketball problem

Jim McCleery
April 6, 2026
Kailua-Kona, HI

Problem summary
---------------
Barbara takes 50 shots, one each from distances x = 1, 2, ..., 50.

For a fixed real number q > 50, the probability of making the shot
from distance x is

    P(make from distance x) = 1 - x / q

We are told that the probability Barbara scores exactly 20 points
(i.e. makes exactly 20 of the 50 shots) is 2%, or 0.02.

Our goal is to determine the value of q.

Mathematical strategy
---------------------
For a fixed q, we compute:

    P(exactly 20 makes in 50 shots)

Then we use binary search to find the value of q for which that
probability is 0.02.
"""


def probability_of_exactly_20_makes(q: float) -> float:
    """
    Return the probability that Barbara makes exactly 20 shots.

    Explanation
    -----------
    We process the 50 shots one at a time.

    Let dp[k] mean:
        the probability that Barbara has made exactly k shots
        after processing some number of distances.

    Initially, before any shots are taken:
        dp[0] = 1
        dp[k] = 0 for k >= 1

    For each distance x, the probability of making the shot is

        p = 1 - x / q

    Then:
        - if she misses, the number of makes stays the same
        - if she makes, the number of makes increases by 1

    So the update rule is:

        new_dp[k] = old_dp[k] * (1 - p) + old_dp[k-1] * p

    To avoid needing a second array, we update backwards from k = 20 down to 1.
    """
    dp = [0.0] * 21
    dp[0] = 1.0

    for x in range(1, 51):
        p_make = 1.0 - x / q
        p_miss = 1.0 - p_make

        # Update backwards so that dp[k - 1] still refers to the previous step.
        for k in range(20, 0, -1):
            dp[k] = dp[k] * p_miss + dp[k - 1] * p_make

        # Probability of still having made 0 shots after this attempt.
        dp[0] *= p_miss

    return dp[20]


def find_q(target_probability: float = 0.02, tolerance: float = 1e-12) -> float:
    """
    Return the value of q for which

        P(exactly 20 makes) = target_probability

    using binary search.

    Why binary search works
    -----------------------
    As q increases, the shot probabilities increase, so Barbara tends
    to make more baskets.  The probability of getting exactly 20 makes
    changes smoothly enough that binary search is effective here.

    We search on an interval [low, high] and repeatedly cut it in half.
    """
    low = 50.0
    high = 1000.0

    # Make sure the upper endpoint is far enough out.
    # We want the target value to lie between the probabilities at low and high.
    while probability_of_exactly_20_makes(high) > target_probability:
        high *= 2.0

    for _ in range(100):
        mid = (low + high) / 2.0
        probability = probability_of_exactly_20_makes(mid)

        if probability > target_probability:
            low = mid
        else:
            high = mid

        if high - low < tolerance:
            break

    return (low + high) / 2.0


def main() -> None:
    """
    Compute q and print it to 10 decimal places.
    """
    q = find_q()
    print(f"{q:.10f}")


if __name__ == "__main__":
    main()
