##Digit cancelling fractions
##
##Problem 33
##The fraction 49/98 is a curious fraction, as an inexperienced
##mathematician in attempting to simplify it may incorrectly
##believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
##
##We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
##
##There are exactly four non-trivial examples of this type of fraction,
##less than one in value, and containing two digits in the numerator and denominator.
##
##If the product of these four fractions is given in its lowest common
##terms, find the value of the denominator.

def gcd(num, den):
    for i in range(1, num+1):
        if((num % i == 0) and (den % i == 0)):
            gcd = i             
    return gcd
  
prodTop = 1
prodBot = 1

for num in range(10,100):
    for den in range(num+1,100):
        if num % 10 != 0 and den % 10 != 0:
            oldFraction = num/den
            top = str(num)
            bot = str(den)
            a = top[0]
            b = top[1]
            c = bot[0]
            d = bot[1]
            noChange = True
            if a == c:
                newFraction = int(b)/int(d)
                noChange = False
            elif a == d:
                newFraction = int(b)/int(c)
                noChange = False
            elif b == c:
                newFraction = int(a)/int(d)
                noChange = False
            elif b == d:
                newFraction = int(a)/int(c)
                noChange = False

            if noChange == False and oldFraction == newFraction:
                prodTop *= num
                prodBot *= den
                print(str(num)+'/'+str(den))

print(str(prodTop)+'/'+str(prodBot))                
greatestCD = gcd(prodTop,prodBot)
print(str(int(prodTop/greatestCD))+'/'+str(int(prodBot/greatestCD)))
#solution 100
