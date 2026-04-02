##Pandigital products
##Problem 32
##We shall say that an n-digit number is pandigital if it
##makes use of all the digits 1 to n exactly once; for example,
##the 5-digit number, 15234, is 1 through 5 pandigital.
##
##The product 7254 is unusual, as the identity, 39 × 186 = 7254,
##containing multiplicand, multiplier, and product is 1 through 9 pandigital.
##
##Find the sum of all products whose multiplicand/multiplier/product
##identity can be written as a 1 through 9 pandigital.
##
##HINT: Some products can be obtained in more than one way so be sure
##to only include it once in your sum.
##

answersProducts = set()
answersStrings = set()
for i in range(1,10000):
    for j in range(1,10000):
        flag = True
        testString = str(i)+str(j)+str(i*j)
        if len(testString) == 9:
            for ch in "123456789":
                if ch not in testString:
                    flag = False                    
            if flag:
                answersProducts.add(i*j)
                str1 = str(i)+'*'+str(j)+' = '+str(i*j)
                str2 = str(j)+'*'+str(i)+' = '+str(i*j)
                if str1 not in(answersStrings) and str2 not in(answersStrings):
                    answersStrings.add(str(i)+'*'+str(j)+' = '+str(i*j))

answersStringsList = list(answersStrings)
print('Pandigital Products')
for i in range(len(answersStrings)):           
    print(answersStringsList[i])
print('Sum of pandigital numbers without duplicates:',sum(answersProducts))
#solution: 45228





