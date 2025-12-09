import numpy as np 
import sys

rawData = open(sys.argv[1]).read().split('\n\n')
idRanges = rawData[0].split('\n')
ingredientList =rawData[1].split('\n') 

# for id in idRanges:
#     print('here')
#     rangeList = id.split('-')


ans = 0
minRangeArray = np.zeros(len(idRanges))
maxRangeArray = np.zeros(len(idRanges))
"""
Sort all ranges with respect to the minimum value.
"""
for idx, id in enumerate(idRanges):
    idRange = id.split('-')
    minRangeArray[idx] = int(idRange[0])
    maxRangeArray[idx] = int(idRange[1])
sortIndices = np.argsort(minRangeArray)
minRangeArray = minRangeArray[sortIndices]
maxRangeArray = maxRangeArray[sortIndices]

"""
Continuously loop until all arrays are observed. Since the ranges are not merged if
the n+1 minimum value is below the n maximum value, the maximum value for the n array 
can be updated ONLY IF the x+1 value is greater. Delete those array entries, break the loop 
and run through everyhting again.
"""

notAllArrays = True
while notAllArrays:
    keep = False
    for arrIdx, minVal in enumerate(minRangeArray):
        if arrIdx == 0:
            continue
        if minVal <= maxRangeArray[arrIdx-1]:
            keep = True
            if maxRangeArray[arrIdx] > maxRangeArray[arrIdx-1]:
                maxRangeArray[arrIdx-1] = maxRangeArray[arrIdx]
            minRangeArray = np.delete(minRangeArray, arrIdx)
            maxRangeArray = np.delete(maxRangeArray, arrIdx)
            break
    if not keep:
        notAllArrays = False

# Take diff and add one to all
answer = np.sum(np.subtract(maxRangeArray, minRangeArray)+1)


print(f"Total Number of fresh IDs: {answer}")

# 304173101922355 - Too Low
# 347468726696961