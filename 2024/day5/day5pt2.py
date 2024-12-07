
import sys
import re
import numpy as np
from scipy.ndimage import rotate
from collections import defaultdict, Counter

D = open(sys.argv[1]).read().strip()
L = D.split('\n')

"""
-Put first group of 'page ordering rules' in a dictionary
    - Each key will represent the page number
    - Result will be a list of page numbers that must come after

-Loop through each set of page number inputs
-Loop through each page number 
    -Use page number to as key to set up dictionary
    -Check if index value of current page number is less than
        -If yes, continue to next line
    -If all page numbers are ``valid" find the middle value and add to result
""" 
def incorrect_order(pg_list, pg_num_idx, pg_rules_list):
    #Returns True if the rules are broken
    for i, pg_rule in enumerate(pg_rules_list):
        if pg_rule not in pg_list:
            continue
        if(pg_list.index(pg_rule)<pg_num_idx):
            return True,pg_rule
    return False, 0
#Setting up page order rules dict
page_order_rules = {}
for i, line in enumerate(L):
    if line == "":
        break
    temp = line.split("|")
    if temp[0] in page_order_rules:
        page_order_rules[temp[0]].append(temp[1])
    else:
        page_order_rules[temp[0]]=[temp[1]]


page_number_data_raw = D.split('\n\n')[1].split('\n')
page_number_data = [x.split(',') for x in page_number_data_raw]
invalid_flag = False
reorder_flag = False #Turn on if anything was reordered
result = 0
for i, line in enumerate(page_number_data):#Through each input
    pg_idx = 0
    reorder_list = list(line)
    while (pg_idx < len(line)):
        if reorder_list[pg_idx] not in page_order_rules:
            pg_idx +=1
            continue
        else:
            order_check, invalid_num_val = incorrect_order(reorder_list, pg_idx, page_order_rules[reorder_list[pg_idx]])
            if order_check:
                #Swap the invalid number with original
                invalid_idx = reorder_list.index(invalid_num_val)
                cur_pg_num = reorder_list[pg_idx]
                reorder_list[invalid_idx] = cur_pg_num
                reorder_list[pg_idx] = invalid_num_val 
                pg_idx = 0
            else:
                pg_idx += 1
        # pg_idx +=1 
    if not line == reorder_list:
        result += int(reorder_list[len(reorder_list)//2])

print("Result: ",result)