import numpy as np
import re
import sys

f = open(sys.argv[1], 'r').read()
dataRanges = f.split(',')
answerA = 0
seenNumbers = set()
for rawRange in dataRanges:
    rangeValues = rawRange.split('-')
    for number in range(int(rangeValues[0]), int(rangeValues[1])+1):
        stringedValue = str(number)
        lenId = len(stringedValue)

        # Looping through various sized segments
        for stringSequenceLength in range(1,lenId+1):
            # print(stringSequenceLength)
            # Check the segment size produces equal sized strings
            if lenId%stringSequenceLength  == 0:
                segmentSteps = lenId//stringSequenceLength
                if segmentSteps == lenId:
                    continue
                # print('*'*50)
                # print(segmentSteps)
                # print(stringedValue)
                # print(stringedValue[:segmentSteps])
                oldValue = stringedValue[:segmentSteps]
                correctCheck = True
                for stepRange in range(0, lenId, segmentSteps):
                    newValue=stringedValue[stepRange:stepRange+segmentSteps]
                    if oldValue == newValue:
                        continue
                    else:
                        correctCheck = False
                        break
                    oldValue = newValue
                if correctCheck:
                    if number not in seenNumbers:
                        answerA += number
                        seenNumbers.add(number)
                        print(number)


            


        # if lenId % 2 == 0:
        #     if stringedValue[:lenId//2] == stringedValue[lenId//2:]:
        #         answerA += int(stringedValue)
print(answerA)