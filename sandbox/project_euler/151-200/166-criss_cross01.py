from itertools import product
from time import time

go = time()
ans=0
the_sevens = list(product(range(10), repeat=7))
for n in range(37):
    for A, B, C, D, E, F, G in the_sevens:
        if (0<= n-A-C-F <= 9 and
            0<= n-D-E-G <= 9 and
            0<= B+C-G <=9 and
            0<= A+B-E <=9 and
            0<= n-A-B-D <=9 and
            0<= D+E+G-B-C <=9 and
            0<= n-A-B-C <=9 and
            0<= n-A-B-D+E-F <=9 and
            0<= 2*A+B+C+D-E+F-n <=9):
                ans += 1

print(f'{ans:<,} runtime: {time()-go}  {7130034==ans}')
