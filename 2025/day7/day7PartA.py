import numpy as np
import sys

# rawData = np.genfromtxt(sys.argv[1], dtype='U1')
with open(sys.argv[1]) as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        dataToAppend = np.array(list(line.strip('\n')),dtype='U1')
        if idx == 0:
            rawData = np.array(dataToAppend)
        else:
            rawData = np.vstack([rawData,np.array(dataToAppend)])

startPos = np.argwhere(rawData== 'S')
totalRows = len(rawData)
totalCols = len(rawData[0])


def tachyon_travel(startPos, tachMap, ans=0, returnedAnswer = 0):
    #continue downwards
    print(tachMap)
    print(f"Starting Position: {startPos}")
    newPos = [startPos[0]+1, startPos[1]]
    print(f"Current Answer: {ans}")
    if newPos[0] > totalRows-1 or newPos[1] > totalCols-1 or newPos[1]<0:
        print('here')
        print(ans)
        return ans

    if tachMap[newPos[0]][newPos[1]] == '|':
        print('1')
        return ans 
    if tachMap[newPos[0]][newPos[1]] == '.':
        print('2')
        tachMap[newPos[0]][newPos[1]] = '|'
        ans = tachyon_travel([newPos[0], newPos[1]],tachMap, ans)
    else:
        ans += 1
        tachMap[newPos[0]][newPos[1]+1] = '|'
        tachMap[newPos[0]][newPos[1]-1] = '|'
        ans = tachyon_travel([newPos[0], newPos[1]+1],tachMap, ans)
        ans = tachyon_travel([newPos[0], newPos[1]-1],tachMap, ans)
    return ans 

ans1 = tachyon_travel(startPos[0], rawData)
print('*'*50)
print(ans1)