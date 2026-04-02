# p163-cross-hatched_triangles.py
#
# Consider an equilateral triangle in which straight lines are drawn from each
# vertex to the middle of the opposite side, such as in the size 1 triangle in
# the sketch below.  (see pdf)
#
# Sixteen triangles of either different shape or size or orientation or
# location can now be observed in that triangle. Using size 1 triangles as
# building blocks, larger triangles can be formed, such as the size 2 triangle
# in the above sketch. One-hundred and four triangles of either different
# shape or size or orientation or location can now be observed in that size 2
# triangle.
#
# It can be observed that the size 2 triangle contains 4 size 1 triangle
# building blocks. A size 3 triangle would contain 9 size 1 triangle building
# blocks and a size n triangle would thus contain n2 size 1 triangle building
# blocks.
#
# If we denote T(n) as the number of triangles present in a triangle of
# size n, then
#    T(1) = 16
#    T(2) = 104
# Find T(36).
# -----------------------------------------------------------------------------
# https://oeis.org/A210687
# a(n) = (1678 * n^3 + 3117 *n^2+88*n-345*Mod[n,2]-320*Mod[n,3]-90*Mod[n,4]-288*Mod[n^3-n^2+n,5])/240
def euler163(n):
    return (1678*n**3 + 3117*(n**2) + 88*n-345*(n% 2) -
            320*(n%3) - 90*(n%4)-288*((n**3 - n**2 + n) % 5)) // 240


ans = euler163(1)
print(f'{ans:8,}  {ans==16}')
ans = euler163(2)
print(f'{ans:8,}  {ans==104}')
ans = euler163(36)
print(f'{ans:8,}  {ans==343047}')

# -----------------------------------------------------------------------------
# solution: 343047  https://oeis.org/A210687
# -----------------------------------------------------------------------------
