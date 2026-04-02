#-------------------------------------------------------------------------------
##Using up to one million tiles how many different "hollow"
##square laminae can be formed?
##Problem 173
##We shall define a square lamina to be a square outline
##with a square "hole" so that the shape possesses vertical
##and horizontal symmetry. For example, using exactly thirty-two
##square tiles we can form two different square laminae:
##
##With one-hundred tiles, and not necessarily using all of the
##tiles at one time, it is possible to form forty-one different square laminae.
##
##Using up to one million tiles how many different square laminae can be formed?
#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
start = time()
limit = 10**6
count = 0

for hole_edge in range(1,limit//4):
    layer_edge = hole_edge + 2
    layer_accumulations = 0
    while True:
        layer_area = layer_edge**2 - layer_accumulations - hole_edge**2
        layer_accumulations += layer_area
        if layer_accumulations > limit:
            break
        else:
            count += 1
        layer_edge += 2
    
print(f'Solution: {count}, Run-Time:{time()-start}')
#-------------------------------------------------------------------------------
#solution: 1572729
#-------------------------------------------------------------------------------
