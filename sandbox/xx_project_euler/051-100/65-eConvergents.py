################################################################################
##Convergents of e
##Problem 65
#NOTE: we are computing the denominators but not doing anything with them
################################################################################
aList = []
pList = []
qList = []
################################################################################
def loadLists(num):

    aList.append(1)
    aList.append(1)
    aList.append(2)

    pList.append(2)
    pList.append(3)
    pList.append(8)

    qList.append(1)
    qList.append(1)
    qList.append(3)

    for i in range(3,num):
        if i % 3 == 2:
            aList.append(2 + aList[i-3])
        else:
            aList.append(1)
        pList.append(aList[i]*pList[i-1] + pList[i-2])
        qList.append(aList[i]*qList[i-1] + qList[i-2])           
################################################################################
MAX = 100
loadLists(MAX)
for i in range(MAX):
    print(i+1,aList[i],pList[i])
    
total = 0
topN = str(pList[MAX-1])
for i in topN:
    total += int(i)
print('Solution:',total)
################################################################################
#solution = 272
################################################################################
