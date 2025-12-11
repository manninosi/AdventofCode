import numpy as np
import sys

rawData = open(sys.argv[1]).read().split('\n')
print(len(rawData))
column1 = np.array(rawData[0].split(), dtype=int)
column2 = np.array(rawData[1].split(), dtype=int)
column3 = np.array(rawData[2].split(), dtype=int)
column4 = np.array(rawData[3].split(), dtype=int)
cephMatrix = np.matrix([column1, column2, column3, column4])
print(np.sum(cephMatrix[:,0]))

ans = 0
for colNum, operator in enumerate(rawData[4].split()):
    if operator == '+':
        ans += np.sum(cephMatrix[:,colNum])
    else:
        ans += np.prod(cephMatrix[:,colNum])
