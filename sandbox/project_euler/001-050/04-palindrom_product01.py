##################################################################################
#jim mccleery, november, 2021
##################################################################################
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two
#2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of
#two 3-digit numbers.
##################################################################################
def flip(num):
    length = len(str(num))
    strIn = str(num)
    strOut = ''
    for i in range(length-1,-1,-1):
        strOut += strIn[i]
    return(int(strOut))
##################################################################################
def isPalindrome(num):
    if flip(num) == num:
        return True
    else:
        return False
##################################################################################
def doTheTest(num):
    pal = 1
    for i in range(num,100,-1):
        for j in range(num,100,-1):
            if isPalindrome(i*j) and i*j > pal:
                pal = i*j
            if j * j < pal:
                break
        if i * i < pal:
            break
    return(pal)
##################################################################################
print(doTheTest(999))
##################################################################################
#solution: 906609 
