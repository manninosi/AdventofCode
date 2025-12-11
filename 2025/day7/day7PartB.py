import numpy as np
import functools
import sys


lines = open(sys.argv[1]).read().splitlines()

startPos = (0, lines[0].index("S"))           # find initial beam
totalRows = len(lines)
totalCols = len(lines[0])

@functools.lru_cache(maxsize=None)
def tachyon_travel(row, col):
    if col  < 0 or col >= totalCols:
        return 0
    if row == totalRows:
        return 1
    cell = lines[row][col] 
    if cell == '.':
        return tachyon_travel(row+1, col)

    if cell == '^':
        return tachyon_travel(row+1, col-1) + tachyon_travel(row+1, col+1)
    else:
        return 0
    

ans = tachyon_travel(startPos[0]+1, startPos[1])
print(ans)

# CORRECT ANSWER - 305999729392659