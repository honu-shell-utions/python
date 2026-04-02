# 117_red_grn_blu_tiles.py
# Using a combination of grey square tiles and oblong tiles chosen from:
# red tiles (measuring two units), green tiles (measuring three units),
# and blue tiles (measuring four units), it is possible to tile a row
# measuring five units in length in exactly fifteen different ways.
#
# How many ways can a row measuring fifty units in length be tiled?
# a(n) = a(n-1)+a(n-2)+a(n-3)+a(n-4)

from time import time

start = time()
f_list = [0,1,2,4,8]

for n in range(5,51):
    f_list.append(f_list[n-1]+f_list[n-2]+f_list[n-3]+f_list[n-4])

print('Solution:',f_list[50],'Run Time:',time()-start)

#sollution: 100808458960497
