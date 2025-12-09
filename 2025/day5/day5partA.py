import numpy as np 
import sys

rawData = open(sys.argv[1]).read().split('\n\n')
idRanges = rawData[0].split('\n')
ingredientList =rawData[1].split('\n') 

# for id in idRanges:
#     print('here')
#     rangeList = id.split('-')


ans = 0
for ingedientID in ingredientList:

    for id in idRanges:
        idRange = id.split('-')
        if int(ingedientID) >= int(idRange[0]) and int(ingedientID) <= int(idRange[1]):
            ans+=1
            break

print(f"Total Fresh Ingredients: {ans}")
