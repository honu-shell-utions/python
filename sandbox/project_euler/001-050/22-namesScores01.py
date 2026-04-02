##Names scores
##
##Problem 22
##
##Using names.txt (right click and 'Save Link/Target As...'),
##a 46K text file containing over five-thousand first names,
##begin by sorting it into alphabetical order. Then working out
##the alphabetical value for each name, multiply this value by
##its alphabetical position in the list to obtain a name score.
##
##For example, when the list is sorted into alphabetical order,
##COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name
##in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
##
##What is the total of all the name scores in the file?
## jim mccleery, november, 2021

inFile = open("22_names.txt", "r")
fileContent = inFile.read()
inFile.close()

temp = fileContent.replace('"','')
contentList = temp.split(",")
contentList.sort()

numNames = len(contentList)
grandTotal = 0

for i in range(numNames):
    wordTotal = 0
    name = contentList[i]
    for j in range(len(contentList[i])):
        wordTotal += ord(name[j])-64
    grandTotal += (i+1)*wordTotal

print('Total:',grandTotal)
#solution: 871198282
