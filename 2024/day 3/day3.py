import sys
import re
import numpy as np
from collections import defaultdict, Counter

D = open(sys.argv[1]).read().strip()
L = D.split('\n')
x = []
inst = []
mul_flag = True
for line in L:
    #Matching mul(3digits,3digits)
    str_2_search = line #Will reduce variable
    mul_match = re.search( r'mul\(\d+\,\d+\)', str_2_search)
    do_match = re.search(r'do\(\)',str_2_search)
    dont_match = re.search(r'don\'t\(\)',str_2_search)

    while(mul_match or do_match or dont_match):
        if(mul_match) and mul_flag: #Ignore ind if mul_flag is off
            mul_ind = mul_match.start()
        else:
            mul_ind = 9999
        if(do_match):
            do_ind = do_match.start()
        else:
            do_ind = 9999
        if(dont_match):
            dont_ind = dont_match.start()
        else:
            dont_ind = 9999
        
        #Indice Defition
        #0 - Multiplier Function
        #1 - Enable Multiplier flag
        #2 - Disable Multiplier flag
        start_inds = np.asarray([mul_ind, do_ind, dont_ind])
        choice = np.argmin(start_inds)
        if choice == 0 and mul_flag:
            x.append(mul_match.group(0))
            end = mul_match.end()
        elif choice == 1:
            mul_flag = True
            end = do_match.end()
        elif choice == 2:
            mul_flag = False
            end = dont_match.end()
        str_2_search = str_2_search[end-1:]
        mul_match = re.search( r'mul\(\d+\,\d+\)', str_2_search)
        do_match = re.search(r'do\(\)',str_2_search)
        dont_match = re.search(r'don\'t\(\)',str_2_search)

#Multiplying and Adding Values
result = 0
for phrase in x:
    data = re.findall(r'\d+', phrase)
    result += int(data[0]) * int(data[1])

print(result)