
"""
find the sum of the first 10 10-super-pandigital numbers
"""
from itertools import permutations

def convert_dec_to_base(n, base):
    chars = "0123456789"
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

def get_sum_of_first_n_super_pandigital(n):
    count = 0
    total = 0
    permutes = permutations("0123456789")
    for p in permutes:
        failed = False
        if p[0] == '0':
            continue
        candidate = int("".join(p))
        for base in range(2,11):
            if not is_pandigital_in_base(candidate,base):
                failed = True
                break
        if failed:
            continue
        total += candidate
        print(candidate)
        count += 1
        if count == n:
            return total
        
print('Sum of the first 10 10-super-pandigital numbers = ',get_sum_of_first_n_super_pandigital(10))
