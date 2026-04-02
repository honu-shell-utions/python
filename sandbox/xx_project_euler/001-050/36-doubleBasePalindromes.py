##Double-base palindromes
## 
##Problem 36
##The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
##
##Find the sum of all numbers, less than one million, which are
##palindromic in base 10 and base 2.
##
##(Please note that the palindromic number, in either base, may
## not include leading zeros.)
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
    palList = []
    for i in range(num):
        tmpString = str(bin(i))
        binInt = int(tmpString[2:])
        if isPalindrome(i) and isPalindrome(binInt):
            palList.append(i)
    return(palList)
##################################################################################
print(sum(doTheTest(1_000_000)))
#solution: 872187 (sum of decimal values)
