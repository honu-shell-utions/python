################################################################################
##Champernowne's constant 
##Problem 40
##An irrational decimal fraction is created by concatenating
##the positive integers:
##
##0.123456789101112131415161718192021...
##
##It can be seen that the 12th digit of the fractional part is 1.
##
##If dn represents the nth digit of the fractional part, find the value
##of the following expression.
##
##d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
################################################################################
def buildBigChamp():
    strChamp = '.'
    i = 1
    while len(strChamp) < 1_000_001:
        strChamp += str(i)
        i += 1
    return(strChamp)
################################################################################
resultString = buildBigChamp()
position = 1
product = 1
for i in range(1,8):
    digit = resultString[position]
    print(digit,end=',')
    position *= 10
    product *= int(digit)
print(' product',product)    
################################################################################
#solution: 210
################################################################################
