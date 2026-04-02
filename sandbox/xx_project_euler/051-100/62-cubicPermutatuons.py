################################################################################
##Cubic permutations
##Problem 62
##The cube, 41063625 (345^3), can be permuted to produce
##two other cubes: 56623104 (384^3) and 66430125 (405^33).
##In fact, 41063625 is the smallest cube which has exactly
##three permutations of its digits which are also cubes.
##
##Find the smallest cube for which exactly five permutations
##of its digits are cube.
################################################################################
listOfSortedStringCubes = []
listOfCubes = []
################################################################################
def sortStringCube(cube):
    cubeStrSorted = ''.join(sorted(str(cube)))
    return cubeStrSorted
################################################################################
def buildAndSearch():
    counter = 1
    while True:
        newCube = counter ** 3
        listOfCubes.append(newCube)
        temp = sortStringCube(newCube)
        listOfSortedStringCubes.append(temp)
        hits = listOfSortedStringCubes.count(temp)
        if hits == 5:
            indexPos = listOfSortedStringCubes.index(temp)
            return indexPos
        counter += 1
################################################################################
index = buildAndSearch()
print(listOfCubes[index])
################################################################################
#solution: 127035954683
################################################################################
