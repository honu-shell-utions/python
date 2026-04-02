################################################################################
import time
################################################################################
def readData(filename):
    fl = open(filename)
    data =[]
    for row in fl:
        row = row.split(',')
        line = [int(i) for i in row]
        data.append(line)
    fl.close()  
    return data
################################################################################
def next_steps(pos):
    (i,j) = pos
    if j+1 < size:
        right = minnum[i,j] + data[i][j+1]
        if right < minnum[i,j+1]:
            minnum[i,j+1] = right 
            next_list.append((i,j+1))
    if i+1 < size:
        down = minnum[i,j] + data[i+1][j]
        if down < minnum[i+1,j]:
            minnum[i+1,j] = down
            next_list.append((i+1,j))
    if j-1 > -1:
        left = minnum[i,j] + data[i][j-1]
        if left < minnum[i,j-1]:
            minnum[i,j-1] = left
            next_list.append((i,j-1))
    if i-1 > -1:
        up = minnum[i,j] + data[i-1][j]
        if up < minnum[i-1,j]:
            minnum[i-1,j] = up
            next_list.append((i-1,j))
################################################################################   
#to get started
start = time.time()         
filename = '83-matrix.csv'
data = readData(filename)
size = 80
infinity = 10**10

#build the minnum dictionary & load with infinity
minnum = {}
for i in range(0,size):
    for j in range(0,size):
        minnum[i,j] = infinity
        
next_list = []        
minnum[0,0] = data[0][0]
test = [(0,0)]

while test!=[]:
    next_list = []
    for el in test:
        next_steps(el)
    test = next_list
    
print('Solution:',minnum[size-1,size-1],'Running time:',time.time()-start)
################################################################################
#Solution: 425185
################################################################################
