import numpy as np
import sys

fn = sys.argv[1]

D = open(fn).read().strip()

hash_code = D.split(',')

def part1_hash(code, result = 0):
    for c in code: #go through each character
        result += ord(c)
        result *= 17
        result = result %256
    return result

def part2_get_box(code):
    result = 0
    if code[-1] == '-': #
        rng_val = len(code[:-1])
    else:
        rng_val = code.rfind('=')


    for c in range(rng_val): #go through each character
        result += ord(code[c])
        result *= 17
        result = result %256
    return result

result = 0
box_dict = {}
#Setting up box numbers
for box_num in np.arange(256):
    box_dict[box_num] = {}
labels = []
for code in hash_code:
    box_num = (part2_get_box(code))
    if code[-2] == '=': #Add lense 
        box_dict[box_num][code[:2]] = int(code[-1])
    else: # remove
        test = box_dict[box_num].pop(code[:2], False)
        # if test:
        #     del box_dict[box_num][code[:2]]
print(box_dict)
result = 0 
for box_num in box_dict:
    labels = list(box_dict[box_num].keys())
    for lbl in labels:
        result += ((1+box_num) * (labels.index(lbl)+1) * box_dict[box_num][lbl])
        
#32172 - Too low!!
#47823 - Too low!
print(result)