import sys


f = open(sys.argv[1]).read().split('\n')

maxCheck = False
answer = 0
for line in f:
    """
    - Use rfind to find where the maximum character is
    - If it is the last idx, re-run and  and find the next maximum 
    - Use that value and the maximum value to make the combination
        - This should be the maximum value
    """
    maxChar = max(line)
    idx = line.find(maxChar)
    if idx == len(line)-1:
        secondChar = line[idx]
        maxChar = max(line[:-1])
        idx = line.find(maxChar)
        firstChar = line[idx]
        maxCombo = firstChar+secondChar
    else:
        firstChar = line[idx]
        updatedString = line[idx+1:]
        maxChar = max(updatedString)
        idx = updatedString.find(maxChar)
        secondChar = updatedString[idx]
        maxCombo = firstChar+secondChar
    print(maxCombo)
    answer += int(maxCombo)
    

print(answer)
