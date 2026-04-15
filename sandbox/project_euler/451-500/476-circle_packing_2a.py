from math import sqrt, pi
import time
"""
https://projecteuler.net/problem=476

Let R(a,b,c) be the maximum area covered by three non-overlapping circles
inside a triangle with edge lengths a, b and c.

Let S(n) be the average value of R(a,b,c) over all integer triplets (a,b,c)
such that 1 <= a <= b <= c < a+b <= n.

You are given S(2) = R(1,1,1) = 0.31998, S(5) = 1.25899.

Find S(1803) rounded to 5 decimal places behind the decimal point.
"""
# -----------------------------------------------------------------------------
def packed_circles_data(a, b, c):
    """
    Return optimal radii and area for three packed circles.
    """
    a, b, c = sorted((a, b, c))

    r0 = inradius(a, b, c)
    sA, sB, _ = half_angle_sines(a, b, c)

    kA = corner_scale(sA)
    kB = corner_scale(sB)

    # Correct decision rule
    if sB <= (2 * sA) / (1 + sA * sA):
        radii = [r0, kA * r0, kB * r0]
        mode = "A+B"
    else:
        radii = [r0, kA * r0, (kA * kA) * r0]
        mode = "A+A"

    area = pi * sum(r * r for r in radii)
    return {
        "radii": radii,
        "mode": mode,
        "area": area,
        "sA": sA,
        "sB": sB,
    }
# -----------------------------------------------------------------------------
def semiperimeter(a, b, c):
    return 0.5 * (a + b + c)
# -----------------------------------------------------------------------------
def half_angle_sines(a, b, c):
    """
    For sorted sides a <= b <= c, let A,B,C be the opposite angles.
    Return sin(A/2), sin(B/2), sin(C/2).
    """
    s = semiperimeter(a, b, c)
    sA = sqrt((s - b) * (s - c) / (b * c))
    sB = sqrt((s - a) * (s - c) / (a * c))
    sC = sqrt((s - a) * (s - b) / (a * b))
    return sA, sB, sC
# -----------------------------------------------------------------------------
def corner_scale(sh):
    """
    If a circle of radius r is tangent to both sides of an angle,
    then the next smaller tangent circle in the same corner has
    radius k*r where k = (1 - sin(theta/2)) / (1 + sin(theta/2)).
    """
    return (1 - sh) / (1 + sh)
# -----------------------------------------------------------------------------
def R(a, b, c):
    return packed_circles_data(a, b, c)["area"]
# -----------------------------------------------------------------------------
def inradius(a, b, c):
    s = semiperimeter(a, b, c)
    return sqrt(((s - a) * (s - b) * (s - c)) / s)
# -----------------------------------------------------------------------------
def valid_triples(n):
    for a in range(1, n // 2 + 1):
        for b in range(a, n - a + 1):
            for c in range(b, a + b):
                yield a, b, c
# -----------------------------------------------------------------------------
n = 1803
start_time = time.perf_counter()
total = 0.0
count = 0
for a, b, c in valid_triples(n):
    total += R(a, b, c)
    count += 1
print('n = '+str(n)+', average area = '+str(round(total / count, 5)))
end_time = time.perf_counter()
print(f"Execution time: {end_time - start_time:.4f} seconds")
# -----------------------------------------------------------------------------
