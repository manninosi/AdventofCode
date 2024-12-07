import sys
import re
import numpy as np
from scipy.ndimage import rotate
from collections import defaultdict, Counter

D = open(sys.argv[1]).read().strip()
L = D.split('\n')
print(len(L))
print(len(L[0]))
data = np.zeros((len(L), len(L[0])+len(L[0])), dtype = str)
for idx, line in enumerate(L):
    x = [k for k in line + ' '*len(L[0])]
    print(x)
    data[idx] = x 
print(data)
print("Finding Vertical")
result = 0
for horiz in data:
    full_str = ''.join(horiz)
    result += full_str.count('XMAS')
    result += full_str.count('SAMX')

print("Finding Horizontal")
for horiz in np.rot90(data):
    full_str = ''.join(horiz)
    result += full_str.count('XMAS')
    result += full_str.count('SAMX')
 
#First Diagonal
diag_data_1 = np.copy(data)
for i,val in enumerate(diag_data_1):
    diag_data_1[i] = np.roll(diag_data_1[i],i)

diag_data_2 = np.copy(data)
for i,val in enumerate(diag_data_2):
    diag_data_2[i] = np.roll(diag_data_2[i],-i)

for horiz in np.rot90(diag_data_1):
    full_str = ''.join(horiz)
    result += full_str.count('XMAS')
    result += full_str.count('SAMX')

for horiz in np.rot90(diag_data_2):
    full_str = ''.join(horiz)
    result += full_str.count('XMAS')
    result += full_str.count('SAMX')

print(result)
# data = np.loadtxt(sys.argv[1], dtype=str)
