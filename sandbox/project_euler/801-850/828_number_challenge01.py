#  -----------------------------------------------------------------------------
#  Numbers Challenge
#  Problem 828
#  https://projecteuler.net/problem=828
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def read_file():
    tot_and_six = []
    n = 0
    in_file = open("828_number_challenge.txt","r")
    try:
        for line in in_file.readlines():
            line = line.strip()
            target = line[:3]
            n1,n2,n3,n4,n5,n6 = line[4:].split(',')
            tot_and_six.append((int(target),int(n1),int(n2),int(n3),int(n4),int(n5),int(n6)))
            n += 1                  
    except IOError:
        print ("File Access Error")
    finally:
        in_file.close()
        print ("total number of records:\t",n)
    return tot_and_six
#  -----------------------------------------------------------------------------
def vals(tup):
    s = set()
    if len(tup) == 1:
        s.add(tup[0])
        return s
    else:
        for k in range(1, 2**len(tup)-1):
            g1 = []
            g2 = []
            for e in range(len(tup)):
                if (k>>e)%2==0:
                    g1.append(tup[e])
                else:
                    g2.append(tup[e])
            st1 = vals(tuple(g1))
            st2 = vals(tuple(g2))
            for v1 in st1:
                for v2 in st2:
                    s.add(v1+v2)
                    s.add(v1*v2)
                    if v1>v2:
                        s.add(v1-v2)
                    if v1%v2==0:
                        s.add(v1//v2)
        return s
#  -----------------------------------------------------------------------------        
def sp(goal, t):
    mi = 10000
    for k in range(1, 2**6):
        g = []
        for e in range(6):
            if (k>>e)%2==1:
                g.append(t[e])
        if goal in vals(tuple(g)):
            mi = min(mi, sum(g))
    if mi==10000:
        return 0
    return mi
#  -----------------------------------------------------------------------------
start = time()
total = 0
records = read_file()
for i,r in enumerate(records):
    g = r[0]
    t = r[1:]
    spgt = sp(g,t)
    total += 3**(i+1)*spgt
    
print(f'Solution: {total % 1005075251}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 148693670
#  -----------------------------------------------------------------------------
