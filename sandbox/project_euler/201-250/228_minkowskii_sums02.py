from fractions import Fraction

def main():
    min = 1864
    max = 1909
    s = set()
    for q in range(min, max+1):
        for p in range(1, q+1):
            s.add(Fraction(p, q))
    print(len(s))

main()
# 86226
