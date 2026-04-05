################################################################################
##Integer right triangles
##
##Problem 39
##If p is the perimeter of a right angle triangle with
##integral length sides, {a,b,c}, there are exactly three
##solutions for p = 120.
##
##{20,48,52}, {24,45,51}, {30,40,50}
##
##For which value of p ≤ 1000, is the number of solutions maximized?
##
################################################################################
def pythagTriples(perimeter):
    count = 0
    for a in range(3,perimeter):
        for b in range(a+1,perimeter):
            for c in range(b+1,perimeter):
                if a + b + c == perimeter and a**2 + b**2 == c**2:
                    count += 1
    return(count)
################################################################################
maxHits = 0
keepPer = 0
for i in range(1001):
    hits = pythagTriples(i)
    if hits > maxHits:
        maxHits = hits
        keepPer = i
print('Max hits: ',maxHits,'for perimeter equal to:',keepPer)
################################################################################
#solution: 840 
################################################################################
