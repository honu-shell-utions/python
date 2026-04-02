#  p149_max_sum_subsequence.py
#  searching for a maximum-sum subsequence
#
#  Looking at the table below, it is easy to verify that the maximum
#  possible sum of adjacent numbers in any
#  direction (horizontal, vertical, diagonal
#  or anti-diagonal) is 16 (= 8 + 7 + 1).
#
#     −2	 5   3	2
#      9	−6   5	1
#      3	 2   7	3
#      1	 8  −4	8
#
#  Now, let us repeat the search, but on a much larger scale:
#
#  First, generate four million pseudo-random numbers using a specific
#  form of what is known as a "Lagged Fibonacci Generator":
#
#  For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007k^3] (modulo 1000000) − 500000.
#  For 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.
#
#  Thus, s10 = −393027 and s100 = 86613.
#
#  The terms of s are then arranged in a 2000×2000 table, using the first
#  2000 numbers to fill the first row (sequentially), the next 2000 numbers
#  to fill the second row, and so on.
#
#  Finally, find the greatest sum of (any number of) adjacent entries
#  in any direction (horizontal, vertical, diagonal or anti-diagonal).

from time import time
# https://github.com/nayuki/Project-Euler-solutions

go = time()


def compute():
    SIZE = 2000

    # generate the pseudorandom sequence according to the lagged Fibonacci generator
    lst = []
    for i in range(SIZE ** 2):
        k = i + 1
        if k <= 55:
            lst.append((100003 - 200003 * k + 300007 * k * k * k) % 1000000 - 500000)
        else:
            lst.append((lst[-24] + lst[-55]) % 1000000 - 500000)

    # reshape the sequence into a 2D array
    grid = [lst[i * SIZE: (i + 1) * SIZE] for i in range(SIZE)]

    # For the sequence of numbers in the grid at positions (x, y), (x+dx, y+dy), (x+2*dx, y+2*dy), ... until the
    # last in-bounds indices, this function returns the maximum sum among all possible substrings of this sequence.
    def get_max_substring_sum(x, y, dx, dy):
        result = 0
        current = 0
        while 0 <= x < SIZE and 0 <= y < SIZE:
            current = max(current + grid[y][x], 0)  # reset the running sum if it goes negative
            result = max(current, result)           # best seen running sum
            x += dx
            y += dy
        return result

    # scan along all line directions and positions
    ans = max(
        max(get_max_substring_sum(0, i, +1, 0),          # horizontal from left edge
            get_max_substring_sum(i, 0, 0, +1),          # vertical from top edge
            get_max_substring_sum(0, i, +1, +1),         # diagonal from left edge
            get_max_substring_sum(i, 0, +1, +1),         # diagonal from top edge
            get_max_substring_sum(i, 0, -1, +1),         # anti-diagonal from top edge
            get_max_substring_sum(SIZE - 1, i, -1, +1))  # anti-diagonal from right edge
        for i in range(SIZE))
    return str(ans)


ans = compute()
print(f'greatest substring sum = {ans} runtime: {time()-go}')  # 52852124

