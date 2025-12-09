import numpy as np
import sys

fn = sys.argv[1]

data = np.genfromtxt(fn, dtype=str)
print(data)
rows = len(data)
col = len(data[0])
print(rows,col)
dataProcessed = np.zeros((rows,col))
for idx_row,row in enumerate(data):
    for idx_col,char in enumerate(row):
        if char == '@':
            dataProcessed[idx_row][idx_col] = 1

print(dataProcessed)

ans = 0
for i, row in enumerate(dataProcessed):
    for j, val in enumerate(row):
        # Check if a roll in present
        rollCount = 0
        if val == 1: # roll is present
            # NW
            if (i-1) >= 0 and (j-1) >= 0:
                rollCount += dataProcessed[i-1][j-1]
            # N
            if (i-1)>=0:
                rollCount += dataProcessed[i-1][j]
            # NE
            if (i-1)>=0 and (j+1) < col:
                rollCount += dataProcessed[i-1][j+1]
            # E
            if (j+1) < col:
                rollCount += dataProcessed[i][j+1]
            # SE
            if (i+1)<rows and (j+1) < col:
                rollCount += dataProcessed[i+1][j+1]
            # S
            if (i+1)<rows:
                rollCount += dataProcessed[i+1][j]
            # SW
            if (i+1)<rows and (j-1) >= 0:
                rollCount += dataProcessed[i+1][j-1]
            # W
            if (j-1) >= 0:
                rollCount += dataProcessed[i][j-1]


                
            if rollCount < 4: 
                ans += 1

print(f"Rolls that work: {ans}")



    # row[row=='.'] = 0 
