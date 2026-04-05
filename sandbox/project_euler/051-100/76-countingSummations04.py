import time 

def PE076():
    res = dp();
    print(res)
    
def dp():
    limit = 10
    ways = [0]*(limit+1)
    ways[0] = 1 
    for n in range(1,limit):
        for k in range(n,limit+1):
            ways[k] += ways[k-n]
    return ways[limit]

t0 = time.time()
PE076()
print("running time={0}s".format((time.time()-t0)))
