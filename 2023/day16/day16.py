import numpy as np
import sys

# D = open(sys.argv[1]).read().strip()
with open(sys.argv[1]) as f:
    D = f.readlines()

lens_map_raw = [list(row.strip('\n')) for row in D]
lens_map_arr = np.array(lens_map_raw, ndmin=2)

"""
This anglle mirr '\' is actually '\\' when parsing

beam_dir = [[0,1]] STARTING DIRECTION
    This array is increase when the beam is split
    loop over this arr to keep track of all the beams
    
cur_idx = [[0,0]] STARTING BEAM LOCATION
    Also expand when beams are split
    Inside same loop 

-Increment cur_idx for each beam based on beam_dir
    -Check cur_idx for specific beam
        -If out of bounds pop or delete that beam 
    -Check symbol at new idx
    -update beam dir
        - '|' and '-' symbols will need to check current beam_dir
        - if perp append new beam to beam_dir and cur_idx
        - +1 (down row, right column),  -1(up row, left column)
    -for part one
        -for reach cur_idx if zeros array is 0 then make i 1
        -will use np.sum to count all interactions
"""
beam_dir = [[0,1]]
cur_beam = [[0,-1]]
light_count_arr = np.zeros_like(lens_map_arr, dtype=np.int32)
prev_light_count_arr = np.copy(light_count_arr)
print(light_count_arr)
chk_stop = 0
repeat_chk = 0
while len(cur_beam)>0 and chk_stop < 1000:
    # print(len(cur_beam))
    print(np.sum(light_count_arr))
    # print('='*40)
    for i,val in enumerate(cur_beam):
        # print(i)
        cur_beam[i] = np.array(val) + np.array(beam_dir[i])
        #Checking if beam has exited the map
        if cur_beam[i][0] < 0 or cur_beam[i][1]<0 or \
           cur_beam[i][0]>len(lens_map_arr)-1 or cur_beam[i][1]>len(lens_map_arr)-1:
               cur_beam.pop(i)
               beam_dir.pop(i)
               continue
        #keep track of where light has energized the map
        if light_count_arr[cur_beam[i][0],cur_beam[i][1]] == 0:
            light_count_arr[cur_beam[i][0],cur_beam[i][1]] = 1

        #Updating beam direction
        tile_sym = lens_map_arr[cur_beam[i][0], cur_beam[i][1]]
        if tile_sym == '/': 
            if beam_dir[i][0] == 0: #Moving along columns
                if beam_dir[i][1] == 1: #Moving right
                    beam_dir[i][0] = -1
                    beam_dir[i][1] = 0 
                elif beam_dir[i][1] == -1: #Moving left 
                    beam_dir[i][0] = 1
                    beam_dir[i][1] = 0 

            elif beam_dir[i][1] == 0: #Moving along rows 
                if beam_dir[i][0] == 1: #Moving down 
                    beam_dir[i][0] = 0 
                    beam_dir[i][1] = -1 
                elif beam_dir[i][0] == -1: #Moving up 
                    beam_dir[i][0] = 0 
                    beam_dir[i][1] = 1 

        elif tile_sym == '\\': 
            if beam_dir[i][0] == 0: #Moving along columns
                if beam_dir[i][1] == 1: #Moving right
                    beam_dir[i][0] = 1
                    beam_dir[i][1] = 0 
                elif beam_dir[i][1] == -1: #Moving left 
                    beam_dir[i][0] = -1
                    beam_dir[i][1] = 0 
            elif beam_dir[i][1] == 0: #Moving along rows 
                if beam_dir[i][0] == 1: #Moving down 
                    beam_dir[i][0] = 0 
                    beam_dir[i][1] = 1 
                elif beam_dir[i][0] == -1: #Moving up 
                    beam_dir[i][0] = 0 
                    beam_dir[i][1] = -1 
        elif tile_sym == r'|': 
            if beam_dir[i][0] == 0: #Moving along columns
                beam_dir[i][0] = 1
                beam_dir[i][1] = 0 
                cur_beam.append([cur_beam[i][0], cur_beam[i][1]])
                beam_dir.append([-beam_dir[i][0], beam_dir[i][1]])
        elif tile_sym == r'-': 
            if beam_dir[i][1] == 0: #Moving along rows
                beam_dir[i][0] = 0 
                beam_dir[i][1] = 1 
                cur_beam.append([cur_beam[i][0], cur_beam[i][1]])
                beam_dir.append([beam_dir[i][0], -beam_dir[i][1]])
    if np.all(prev_light_count_arr == light_count_arr):
        repeat_chk += 1
        if repeat_chk > 50:
            break
    else:
        repeat_chk = 0
    prev_light_count_arr = np.copy(light_count_arr)
        
            

    chk_stop += 1
print(np.sum(light_count_arr))
