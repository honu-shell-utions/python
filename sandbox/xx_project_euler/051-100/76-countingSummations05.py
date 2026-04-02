target = 100
ways = [0]*(target+1)
ways[0] = 1

for i in range(1,len(ways)):
    for j in range(i,len(ways)):
        #print('before the update  ',ways)
        ways[j] += ways[j-i]
        #print('after ',j-i,'added to',j,ways)
        #print()
        
print('Solution for n =',target,'is',ways[target]-1)
