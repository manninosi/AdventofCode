import sys
import re
import numpy as np
from collections import defaultdict, Counter
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
data_matrix = [x.split() for x in L]
# data_matrix = np.loadtxt(sys.argv[1], dtype=int)
# data_matrix = np.genfromtxt(sys.argv[1], delimiter = " ")
result_1 = 0 

# diff_matrix = np.diff(data_matrix)

for i, raw_row in enumerate(data_matrix):
    row = np.asarray(raw_row, dtype=int)
    row = np.diff(row)
    if (np.all(row>0)):
        if (np.all(row<=3) ):
            result_1 +=1
    elif (np.all(row<0)):
        if (np.all(np.abs(row)<=3)):
            result_1 += 1
    else:
        print("*"*50)
        print(raw_row)
        for lvl_idx in range(len(raw_row)):
            row = np.asarray(raw_row, dtype=int)
            new_row = np.delete(row,lvl_idx)
            new_row = np.diff(new_row)
            if (np.all(new_row>0)): #All increasing
                if (np.all(new_row<=3) ):
                    result_1 +=1
                    print("Safe")
                    break
                else:
                    print(lvl_idx)
                    print(new_row)
                    continue
            elif (np.all(new_row<0)): #All decreasing
                if (np.all(np.abs(new_row)<=3)):
                    result_1 += 1
                    print("Safe")
                    break
                else:
                    print(lvl_idx)
                    print(new_row)
                    continue
            else:
                print(lvl_idx)
                print(new_row)

print("Total Number of Safe Reports: ", result_1)

    
