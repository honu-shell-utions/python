target = 6
ways = [1] + [0]*target

for n in range(1,target):
    for i in range(n, target+1):
        ways[i] += ways[i-n]
        print('ways',ways[target],'n',n,'i',i,'i-n',i-n,end=', ')
    print()

print("Number of ways", target,"can be written as a \nsum \
of at least two positive integers:", ways[target])

print(ways)

## It is possible to write five as a sum in exactly six different ways:
##
## 4 + 1
## 3 + 2
## 3 + 1 + 1
## 2 + 2 + 1
## 2 + 1 + 1 + 1
## 1 + 1 + 1 + 1 + 1
##
