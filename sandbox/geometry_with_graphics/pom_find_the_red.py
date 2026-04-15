from math import pi, cos, sin
import matplotlib.pyplot as plt


def area_polygon(points):
    return abs(sum(
        x1 * y2 - y1 * x2
        for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1])
    )) / 2

"""
https://youtu.be/d3c07VPHNv8?si=7fD2fdJs9qrSAE8C

figure out the side of the little equilateral triangle
sqrt(3) = 1/2*s*s*sin(60)
sqrt(3) = 1/2*s*s*sqrt(3)/2
4 = s*s
s = 2
us s to find the length of the two equal segments, law of cosines,
call it a.
52 = (s+a)**2 + a**2 -2(s+a)(a)*cos(60)
a = 6
"""

s = 2
a = 6

p0 = (0, 0)
p1 = (s, 0)
p2 = (a, 0)
p3 = ((s + a) * cos(pi / 3), (s + a) * sin(pi / 3))
p4 = (s * cos(pi / 3), s * sin(pi / 3))

triangle = [p1, p2, p3]
x, y = zip(*(triangle + [triangle[0]]))
area = area_polygon(triangle)

plt.fill(x, y, color="red", edgecolor="red", linewidth=2)

for A, B in [(p0, p2), (p3, p2), (p0, p3), (p1, p4), (p1, p3)]:
    plt.plot([A[0], B[0]], [A[1], B[1]], color="black")

plt.title(f"Size of the red area: {area:.3f}")
plt.axis("equal")
plt.show()
