import sympy as sy

answer, num = 0,10001
while not answer:
    liste=[i for i in str(num)]
    numara=[i for i in liste if liste.count(i)==3]
    if numara:
        count=0
        if sy.isprime(num)==True:
            if int(numara[0])==int(str(num)[0]):
                for z in range(1,10):
                    if sy.isprime(int(str(num).replace(numara[0], str(z)))) == True:
                        count += 1
            if int(numara[0])!=int(str(num)[0]):
                for z in range(10):
                    if sy.isprime(int(str(num).replace(numara[0],str(z))))==True:
                        count+=1
            if count==8:
                answer = num

    num+=2
print(answer)
