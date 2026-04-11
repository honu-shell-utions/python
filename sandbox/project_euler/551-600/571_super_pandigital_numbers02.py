# https://projecteuler.net/problem=571
# takes about an hour but it does the job

from itertools import permutations

def convert_dec_to_base(n, base):
    chars = "0123456789AB"
    result = ""
    while n > 0:
        n, remainder = divmod(n, base)
        result = chars[remainder] + result
    return result or "0"

def is_pandigital_in_base(n,base):
    n_str = convert_dec_to_base(n,base)
    dig_set = set()
    for ch in n_str:
        dig_set.add(ch)
    if len(dig_set) == base:
        return True
    else:
        return False

def base12_to_base10(candidate_str):
    total = 0
    exp = len(candidate_str)-1
    for ch in candidate_str:
        if ch == 'A':
            digit_value = 10
        elif ch == 'B':
            digit_value = 11
        else:
            digit_value = int(ch)
        total += digit_value*12**exp
        exp -= 1

    return(total)
    
def get_sum_of_first_n_super_pandigitals(n):
    count = 0
    total = 0
    permutes = permutations('0123456789AB')
    for p in permutes:
        failed = False
        if p[0] == '0':
            continue
        candidate_str = "".join(p)
        candidate_dec = base12_to_base10(candidate_str)
        for base in range(3,12):
            if not is_pandigital_in_base(candidate_dec,base):
                failed = True
                break
        if failed:
            continue
        total += candidate_dec
        count += 1
        print(count,candidate_dec,total)
        if count == n:
            return total
        
print(get_sum_of_first_n_super_pandigitals(10))
