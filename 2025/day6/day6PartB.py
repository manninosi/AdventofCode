import numpy as np
import sys
import re
cephMatrix = np.array([None])   
np.set_printoptions(threshold=sys.maxsize) 
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        # if line[0] == '*' or line[0] == '+':
        #     break
        # pattern = r'\S+\s*(?=\s|$)'
        # matches = line.split(' ')
        # matches = re.findall(pattern,  line)
        matches = np.array(list(line),dtype='U1')
        print(matches[0:10])
        if np.all(cephMatrix == None):
            cephMatrix = matches
        else:
            print('here')
            print(matches)
            cephMatrix = np.vstack([cephMatrix,  matches])
        # exit()
# ta  = np.genfromtxt(sys.argv[1], dtype='U10')

ans = 0
subAns = 0
multFlag = True
for idx, strNum in enumerate(cephMatrix.T):
    if strNum[-1] == '+':
        subAns = 0 
        multFlag = False
    elif strNum[-1] == '*':
        subAns = 1
        multFlag = True

    subString = "".join(strNum[:-1])
    print(subString)
    if len(subString.strip())==0:
        ans += subAns
        continue
    else:
        subStringInt = int(subString)
        if multFlag:
            print("multy")
            subAns *= subStringInt 
        else:
            print("add")
            subAns += subStringInt 
print(ans+subAns) 
    # print(subStringInt)
    

exit()

# exit()
rawData = open(sys.argv[1]).read().split('\n')
# column1 = np.array(rawData[0].split(), dtype=str)
# column2 = np.array(rawData[1].split(), dtype=str)
# column3 = np.array(rawData[2].split(), dtype=str)
# column4 = np.array(rawData[3].split(), dtype=str)
# cephMatrix = np.matrix([column1, column2, column3, column4])
ans = 0
for colNum, operator in enumerate(rawData[4].split()):
    strLengthArray = np.char.str_len(cephMatrix[:,colNum])
    maxStrLength = np.max(strLengthArray)
    num1 = cephMatrix[:,colNum][0]
    num2 = cephMatrix[:,colNum][1]
    num3 = cephMatrix[:,colNum][2]
    num4 = cephMatrix[:,colNum][3]

    if operator == '+':
        subAns = 0
    else:
        subAns = 1

    if len(num1) < maxStrLength:
        num1 = ' '*(maxStrLength - len(num1)) + num1
        # num1 += ' '*(maxStrLength - len(num1))
    if len(num2) < maxStrLength:
        num2 = ' '*(maxStrLength - len(num2)) + num2
        # num2 += ' '*(maxStrLength - len(num2))
    if len(num3) < maxStrLength:
        num3 = ' '*(maxStrLength - len(num3)) + num3
        # num3 += ' '*(maxStrLength - len(num3))
    if len(num4) < maxStrLength:
        num4 = ' '*(maxStrLength - len(num4)) + num4
        # num4 += ' '*(maxStrLength - len(num4)) 
    
    for i in range(maxStrLength):
        print('*'*50)
        print(colNum)
        strAns = ''
        print(num1)
        print(num2)
        print(num3)
        print(num4)
        # if  len(num1) >= (maxStrLength - i):
        #     strAns += num1[maxStrLength-(i+1)]
        # if  len(num2) >= (maxStrLength - i):
        #     strAns += num2[maxStrLength-(i+1)]
        # if  len(num3) >= (maxStrLength - i):
        #     strAns += num3[maxStrLength-(i+1)]
        strAns += num1[i]
        strAns += num2[i]
        strAns += num3[i]
        strAns += num4[i]
        print(f"Current String Answer: {strAns}")
        print(f"The operator {operator}")
        if len(strAns.strip()) == 0:
            continue
        if operator == '+':
            subAns += int(strAns)
        else:
            subAns *= int(strAns)
    ans += subAns


#     if operator == '+':
#         ans += np.sum(cephMatrix[:,colNum])
#     else:
#         ans += np.prod(cephMatrix[:,colNum])

print(f"Total Value: {ans}")

# 12348086321500 - Too Low
# 12377436852367 - Too Low
# 12422382216609 - Too High
# 1879826418