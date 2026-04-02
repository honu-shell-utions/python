sdb={}
def srec(dleft,cleft=23,rem=0,st=[]):
    global lst
    if(dleft==0): return {}
    if(cleft>9*dleft): return {}
    if(dleft==1):
        return { (rem*10+cleft)%23 : 1 }

    key=(dleft,cleft,rem)
    try: return sdb[key]
    except: pass

    rdb={}
    lh=dleft>>1
    rh=dleft-lh
    for i in range(cleft+1):
        db=srec(lh,i,rem,st+[(0,i)])
        for r1,a in db.items():
            db2=srec(rh,cleft-i,r1,st+[(1,i)])
            for r2,b in db2.items():
                try: rdb[r2]+=a*b
                except: rdb[r2]=a*b
    
    for k in rdb: rdb[k]%=MOD
    sdb[key]=rdb
    return rdb
#=========================================
from time import time
start=time()
MOD = 10**99
print (srec(9)[0])
print (srec(42)[0])
MOD = 10**9
print (srec(11**12)[0])
print("Total time taken: %fs"%(time()-start))
