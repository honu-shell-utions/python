################################################################################
##Largest exponential
##Problem 99
##Comparing two numbers written in index form like 2^11 and 3^7
##is not difficult, as any calculator would confirm that
##2^11 = 2048 < 3^7 = 2187.
##
##However, confirming that 632382^518061 > 519432^525806 would
##be much more difficult, as both numbers contain over three million digits.
##
##Using base_exp.txt (right click and 'Save Link/Target As...'),
##a 22K text file containing one thousand lines with a
##base/exponent pair on each line, determine which line number has
##the greatest numerical value.
##
##NOTE: The first two lines in the file represent the numbers
##in the example given above.
################################################################################
def processPairs():
    import csv
    MAX = -1
    saveLineNumber = 0
    lineNumber = 0
    with open('99-base-exp.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lineNumber += 1
            base = int(row[0])
            exp = int(row[1])
            result = exp * log(base)
            if result > MAX:
                MAX = result
                saveLineNumber = lineNumber

    return(saveLineNumber,MAX)

################################################################################
from math import log

print(processPairs())

################################################################################
#solution: (709, 6919995.552420337)
################################################################################
