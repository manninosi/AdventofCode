
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
result = 0
for i, line in enumerate(page_number_data):#Through each input
    for j, pg_num in enumerate(line): #Through each page number
        if pg_num in page_order_rules: #Through each rule
            for k, rule_pg_num in enumerate(page_order_rules[pg_num]):
                if rule_pg_num not in line:
                    continue
                if(line.index(rule_pg_num)<j):
                    # print('*'*50)
                    # print("Page Rules")
                    # print(page_order_rules[pg_num])
                    # print("page number")
                    # print(pg_num)
                    # print("rule Broken")
                    # print(line)
                    # print("index: ", i)
                    invalid_flag = True
                    break
        if invalid_flag:
            break 
    if invalid_flag:
        invalid_flag = False
        continue
    else:
        result += int(line[len(line)//2])

print("Result: ",result)