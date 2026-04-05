with open('oeisA181061.txt') as fil:
    oeis = fil.readlines()
lst = [int(n.strip()) for n in oeis]

print(len(lst))
print(sum(lst[:-1]))
