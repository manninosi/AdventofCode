import numpy as np
import sys

dataInput = np.loadtxt(sys.argv[1], dtype=str)

print(dataInput)

dialNumber = 50
zeroCounter = 0
zeroCounterB = 0
for dialTurn in dataInput:
    zeroFlag = False
    if dialNumber == 0:
        zeroFlag = True
    print('*'*50)
    direction = dialTurn[0]
    dialClick = int(dialTurn[1:])
    print(f"Number of clicks: {dialClick}")

    if direction == 'L':
        dialNumber = (dialNumber-dialClick) 
        print(f"Left dial turn: {dialNumber}")

        if dialNumber < 0:
            if zeroFlag:
                zeroCounterB +=  int(dialNumber/-100)
            else:
                zeroCounterB +=  1 + int(dialNumber/-100)
            dialNumber = (dialNumber %100) 
            if dialNumber == 0:
                zeroCounterB -= 1
    else:
        dialNumber += dialClick
        print(f"Right dial turn: {dialNumber}")
        if (dialNumber%100 == 0):
            zeroCounterB -= 1
            zeroCounterB += int(dialNumber/100) 
        else:
            zeroCounterB += int(dialNumber/100) 
        dialNumber = (dialNumber) % 100 
    if dialNumber == 0:
        zeroCounter += 1
        zeroCounterB += 1
    print(f"Correct Dial number: {dialNumber}")
    print(f"Current Counter Number: {zeroCounterB}")
print(f"Number of 0 hits for part A: {zeroCounter}")
print(f"Number of 0 hits for part B: {zeroCounterB}")
#6204 -- too high
# 6230 --  still too high duh
# 5854 -- Too low 
# 6126 -- Incorrect