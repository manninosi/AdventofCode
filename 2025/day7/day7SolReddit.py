#!python
# coding utf8
"""
.......S....... 
...............
.......^.......
...............
......^.^...... 
...............



.......S.......         
.......|.......         
......|^|......         
......|.|......
.....|^|^|.....
.....|.|.|.....

Timelines
0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
.  .  .  .  .  .  .  S  .  .  .  .  .  .  .         index('S') => i=7, beam[i] = 1
.  .  .  .  .  .  .  1  .  .  .  .  .  .  .         
.  .  .  .  .  .  1  ^  1  .  .  .  .  .  .         line[7]=='^' => split beam -> 
                                                    beam[i-1]+=beam[i]; beam[i+1]+=beam[i]; del beam[i]
.  .  .  .  .  .  1  .  1  .  .  .  .  .  .
.  .  .  .  .  1  ^  2  ^  1  .  .  .  .  .         for i in beam.keys() 
.  .  .  .  .  1  .  2  .  1  .  .  .  .  .             
.  .  .  .  1  ^  3  ^  3  ^  1  .  .  .  .             
.  .  .  .  1  .  3  .  3  .  1  .  .  .  .
.  .  .  1  ^  4  ^  3  3  1  ^  1  .  .  .         
.  .  .  1  .  4  .  3  3  1  .  1  .  .  .
.  .  1  ^  5  ^  4  3  4  ^  2  ^  1  .  .
.  .  1  .  5  .  4  3  4  .  2  .  1  .  .
.  1  ^  1  5  4  ^  7  4  .  2  1  ^  1  .
.  1  .  1  5  4  .  7  4  .  2  1  .  1  .
1  ^  2  ^ 10  ^ 11  ^ 11  ^  2  1  1  ^  1
1  .  2  . 10  . 11  . 11  .  2  1  1  .  1
"""

from collections import defaultdict
import sys
lines = open(sys.argv[1]).read().splitlines()
splitters = 0
beams = defaultdict(int)
beams[lines[0].index("S")] = 1          # find initial beam
chk = 0
for line in lines[::2]:                 # due to how puzzle is we can skip every other line
    chk += 1
    for i in tuple(beams.keys()):
        if line[i] == "^":
            splitters += 1
            beams[i-1] += beams[i]
            beams[i+1] += beams[i]
            del beams[i]

print(f"P1: {splitters}")
print(f"P2: {sum(beams.values())}")
