################################################################################
##Counting block combinations I
##Problem 114
##A row measuring seven units in length has red blocks
##with a minimum length of three units placed on it,
##such that any two red blocks (which are allowed to be different lengths)
##are separated by at least one grey square. There are exactly seventeen
##ways of doing this.
##
##How many ways can a row measuring fifty units in length be filled?
##
##NOTE: Although the example above does not lend itself
##to the possibility, in general it is permitted to mix
##block sizes. For example, on a row measuring eight units
##in length you could use red (3), grey (1), and red (4).
################################################################################

################################################################################
def to_binary(n, num_bits):
    binary = ''
    i = 2**num_bits // 2
    while i > 0:
        binary += '1' if (n & i) else '0'
        i = i // 2
    return binary
################################################################################
def is_solution(bit_string):
    #total the ones
    total = 0
    for bin_digit in bit_string:
        total += int(bin_digit)
        
    #build min red size string
    min_red_block = '111'
         
    #all zeros or all ones
    if total == len(bit_string) or total == 0: return True
        
    #else must have at least one min red size of reds
    if bit_string.find(min_red_block) == -1: return False

    #single & double reds, not at the ends
    if bit_string.find('010') != -1: return False
    if bit_string.find('0110') != -1: return False
    
    #single reds, at the ends
    if bit_string[:2] == '10': return False
    if bit_string[len(bit_string)-2:] == '01': return False

    #double reds, at the ends
    if bit_string[:3] == '110': return False
    if bit_string[len(bit_string)-3:] == '011': return False

    #looks good
    return True
################################################################################
for grey_tile_size in range(7,51):
    solutions = 0
    for i in range(2**grey_tile_size):
        bar = to_binary(i,grey_tile_size) 
        if is_solution(bar):
            solutions += 1
    print(grey_tile_size,solutions)
################################################################################
#solution: 
################################################################################
