#-------------------------------------------------------------------------------
# 244_sliders.py
#
# You probably know the game Fifteen Puzzle. Here, instead of numbered tiles,
# we have seven red tiles and eight blue tiles.
#
# A move is denoted by the uppercase initial of the direction
# (Left, Right, Up, Down) in which the tile is slid, e.g. starting from
# configuration (S), by the sequence LULUR we reach the configuration (E):
# (see pdf pic)
#
# For each path, its checksum is calculated by (pseudocode):
# checksum = 0
# checksum = (checksum × 243 + m1) mod 100 000 007
# checksum = (checksum × 243 + m2) mod 100 000 007
#    …
# checksum = (checksum × 243 + mn) mod 100 000 007
# where mk is the ASCII value of the kth letter in the move sequence and the 
# ASCII values for the moves are:
#
# L	76
# R	82
# U	85
# D	68
#
# For the sequence LULUR given above, the checksum would be 19761398.
#
# Now, starting from configuration (S), find all shortest ways to reach 
# configuration (T).  (see pdf pic)
#
# What is the sum of all checksums for the paths having the minimal length?
# {ans == 96356848}
#-------------------------------------------------------------------------------
import queue
strt = tuple("wrbbrrbbrrbbrrbb")
slvd = tuple("wbrbbrbrrbrbbrbr")
visited = {strt}
mod = 10 ** 8 + 7
q = queue.Queue()
q.put((0,strt, 0))
while True:
    chksm, pos, white = q.get()
    if pos == slvd:
        print(chksm)
        break
    else:
        p = list(pos)
        for m, cond, i in zip("UDRL",(lambda x: x < 12,
                                      lambda x: x > 3,
                                      lambda x: x % 4,
                                      lambda x: (x + 1) % 4),
                              (4,-4,-1,1)):
            if cond(white):
                p[white + i], p[white] = p[white], p[white + i]
                if tuple(p) not in visited:
                    visited.add(tuple(p))
                    q.put(((chksm * 243 + ord(m)) % mod, tuple(p), white + i))
                p[white + i], p[white] = p[white], p[white + i]
#-------------------------------------------------------------------------------
# min paths: 560
# solution: 96_356_848
#-------------------------------------------------------------------------------
