
size = 1000 # number of rows
grid = [[0]*size for _ in range(size)] # a bit wasteful, but memory is cheap

def rng(numElements):
    t = 0
    for k in range(0,numElements):
        t = ((615949*t)+797807) % 2**20
        yield t - 2**19

gen = rng(size*(size+1)//2)
for y in range(0,size):
    for x in range(0,y+1): grid[y][x] = next(gen)
    
tbase = [[0]*(size+1) for _ in range(size)]        
for y in range(0, size):
    for x in range(0,y+1):
        tbase[y][x+1]= tbase[y][x] + grid[y][x]

minV= 0
for y in range(0,size-1):
    for x in range(0,y+1):
        sumSoFar = grid[y][x]
        for depth in range(1,size-y):
            sumSoFar += tbase[y+depth][x+depth+1] - tbase[y+depth][x]
            if sumSoFar < minV:
                minV = sumSoFar

print(minV)
#solution: -271248680
