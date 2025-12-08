import sys


f = open(sys.argv[1]).read().split('\n')

maxCheck = False
answer = 0
joltageLength = len(f[0])
maxSkipChars = joltageLength - 12 
assembledJolt = ''
skippedChars = 0
skippedCharsTotal = 0
currentIdx = 0
oldIdx = 0
fileTrack = 0

while  skippedChars <= maxSkipChars and fileTrack < len(f):
    # Next data line
    line = f[fileTrack]

    # Must update maximum skip chars by reducing the number of already skipped chars 
    maxChar = max(line[oldIdx:oldIdx+maxSkipChars-skippedChars+1])
    currentIdx = line[oldIdx:oldIdx+maxSkipChars-skippedChars+1].find(maxChar)
    skippedChars += currentIdx 

    # Skipped the maximum number of characters
    if skippedChars >= maxSkipChars:

        # Need to step back until we grab sufficient enough of values to reach 12 length
        assembledJolt += line[oldIdx+(maxSkipChars-skippedChars)+currentIdx:]
        answer += int(assembledJolt)

        # Reset the parameters
        fileTrack += 1
        currentIdx = 0
        oldIdx = 0
        skippedChars = 0
        assembledJolt = ''
        continue

    # Add max value to Jolt
    assembledJolt+=maxChar

    if len(assembledJolt) >= 12:
        # Reached end where last numbers are the same or less
        answer += int(assembledJolt)
        fileTrack += 1
        currentIdx = 0
        oldIdx = 0
        skippedChars = 0

        assembledJolt = ''
        continue

    # Reseting search index to be next number from where current max char was found
    oldIdx += currentIdx+1
    currentIdx += 1
    

print(f"Total Joltage: {answer}")

#Tried Answers and Relative Result
# 22644765129481 - Too Low
# 1587134661268929787958477472602502390512165103897942380599174451112657279770487648019275886392 - Too High
# 132566151943790778362183346494170708456264111238858404216861233259003305607931798643752921 - Also Not right
# 49247718162772 - Too Low
# 167384358365132 - CORRECT ANSWER
# 167302616519692