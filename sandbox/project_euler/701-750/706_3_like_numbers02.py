from collections import defaultdict

n = 10 ** 5

mod = 10 ** 9 + 7

tab = defaultdict( int, { (0, 0, 1, 0) : 3, (0, 0, 0, 1) : 3, (1, 1, 0, 0) : 3 } )
ntab = defaultdict( int )

for i in range( 1, n ):
    while tab:
        (seqs, s0, s1, s2), amt = tab.popitem()
        ntab[( seqs + s0 + 1 ) % 3, ( s0 + 1 ) % 3, s1, s2] += 4 * amt % mod
        ntab[( seqs + s2 ) % 3, s2, ( s0 + 1 ) % 3, s1] += 3 * amt % mod
        ntab[( seqs + s1 ) % 3, s1, s2, ( s0 + 1 ) % 3] += 3 * amt % mod
    tab, ntab = ntab, tab

print( sum( amt for (s, s0, s1, s2), amt in tab.items() if not s ) % mod )
