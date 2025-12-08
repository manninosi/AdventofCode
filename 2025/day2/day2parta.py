import numpy as np
import re
import sys

f = open(sys.argv[1], 'r').read()
dataRanges = f.split(',')
answerA = 0
for rawRange in dataRanges:
    rangeValues = rawRange.split('-')
    print(rangeValues)
    for number in range(int(rangeValues[0]), int(rangeValues[1])+1):
        stringedValue = str(number)
        lenId = len(stringedValue)
        if lenId % 2 == 0:
            if stringedValue[:lenId//2] == stringedValue[lenId//2:]:
                answerA += int(stringedValue)
print(answerA)