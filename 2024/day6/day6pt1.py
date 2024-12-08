import sys
import re
import numpy as np
from scipy.ndimage import rotate
from collections import defaultdict, Counter

D = open(sys.argv[1]).read().strip()
L = D.split('\n')

with open(sys.argv[1]) as f:
    maze_raw = f.readlines()
maze_raw = [list(row.strip('\n')) for row in maze_raw]
maze_2d_arr = np.array(maze_raw, ndmin=2)

row_len = maze_2d_arr.shape[0]
col_len = maze_2d_arr.shape[1]
# map_data = np.loadtxt(sys.argv[1], dtype=str)
print(maze_2d_arr)
start_loc = np.argwhere(maze_2d_arr=='^')[0]