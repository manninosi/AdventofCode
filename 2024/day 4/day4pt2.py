import sys
import re
import numpy as np
from scipy.ndimage import rotate
from collections import defaultdict, Counter

D = open(sys.argv[1]).read().strip()
L = D.split('\n')


data = np.zeros((len(L), len(L[0])), dtype = str)
for idx, line in enumerate(L):
    x = [k for k in line ]
    data[idx] = x 
result = 0
for i, row in enumerate(data):
    if i == 0 or i+2> len(data):#skip first line
        continue
    for q,letter in enumerate(row):
        if q == 0 or q+2 > len(row):
            continue
        if letter == 'A':
            #Check left x
            if (data[i-1, q-1] == 'M' and data[i+1, q+1] == 'S') or (data[i-1, q-1] == 'S' and data[i+1, q+1] == 'M'):
                #check right X
                if (data[i+1, q-1] == 'M' and data[i-1, q+1] == 'S') or (data[i+1, q-1] == 'S' and data[i-1, q+1] == 'M'):
                    result += 1


print("Found X's: ", result)