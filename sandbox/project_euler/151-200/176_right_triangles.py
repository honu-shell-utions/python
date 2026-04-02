#-------------------------------------------------------------------------------
##Right-angled triangles that share a cathetus
##Problem 176
##The four right-angled triangles with sides (9,12,15), (12,16,20),
##(5,12,13) and (12,35,37) all have one of the shorter
##sides (catheti) equal to 12. It can be shown that no other
##integer sided right-angled triangle exists with one of the
##catheti equal to 12.
##
##Find the smallest integer that can be the length of a cathetus
##of exactly 47547 different integer sided right-angled triangles.
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# 2*47547 + 1 = 95095 = 5 * 7 * 11 * 13 * 19
# formula (2e_1 - 1)(2e_2 + 1)... we get
# n = 2^10 * 3^6 * 5^5 * 7^3 * 11^2 = 96818198400000

# http://oeis.org/A046079
ans = 2**10 * 3**6 * 5**5 * 7**3 * 11**2
print(ans, 96818198400000 == ans)





#-------------------------------------------------------------------------------
#solution: 96818198400000
#-------------------------------------------------------------------------------
