import sys
import numpy as np
import matplotlib.pyplot as plt
D = open(sys.argv[1]).read().strip()

fn = sys.argv[1]
with open(fn) as f:
    mirror_map_raw = f.readlines()

mirror_map_raw = [list(row.strip('\n')) for row in mirror_map_raw]

rock_map = np.array(mirror_map_raw, ndmin=2)
#"rotate" by using transform
#start at end and switch indices with 'O' and '.' until end or '#'
def rotate_rocks(rock_map_raw, dir='N'):
    rock_map_copy = np.copy(rock_map_raw)
    if dir == 'N' or dir == 'S':
        rock_to_rot = np.copy(rock_map_copy.T)
    else:
        rock_to_rot = np.copy(rock_map_copy)
    for idx, row_T in enumerate(rock_to_rot):
        if dir == 'N' or dir =='W':
            row = np.flip(row_T)
        else:
            row = row_T
        no_swp = 0 #Don't stop until there were no swaps
        while not no_swp:
            no_swp = 1
            for i,rock in enumerate(row[:-1]):
                temp1 = rock
                temp2 = row[i+1] 
                if temp1 == 'O' and temp2 == '.':
                    row[i] = '.'
                    row[i+1] = 'O'
                    no_swp = 0
        if dir == 'N' or dir =='W':
            rock_map_copy[idx] = np.flip(row)
        else:
            rock_map_copy[idx] = (row)

    if dir == 'N' or dir == 'S':
        return rock_map_copy.T
    else:
        return rock_map_copy

#Do one rotation
rock_map_final = np.copy(rock_map)
for dir in ['N', 'W', 'S', 'E']:
    rock_map_final = rotate_rocks(rock_map_final, dir=dir)

result_arr = [] 
for i in range(1000):
    rock_final_copy = np.copy(rock_map_final)
    for dir in ['N', 'W', 'S', 'E']:
        rock_map_final = rotate_rocks(rock_map_final, dir=dir)

    #Count cirlces
    result = 0
    for i, row_cnt in enumerate(rock_map_final):
        rock, cnts = np.unique(row_cnt, return_counts=True)  
        rocks_present = (bool(np.argwhere(rock=='O')))
        if rocks_present > 0:
            result += cnts[np.argwhere(rock=='O')] * (len(rock_map_final)-i)
    result_arr.append(result[0])
fig,ax = plt.subplots()
print(result_arr)
ax.plot(np.arange(len(result_arr)), result_arr, 'o')
plt.show()
print(result)

        