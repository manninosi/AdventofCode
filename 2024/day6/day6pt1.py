import sys
import re
import numpy as np
from scipy.ndimage import rotate
from collections import defaultdict, Counter


class GuardPiece():
    def __init__(self, pos_x, pos_y, dir='N'):
        self.x = pos_x
        self.y = pos_y
        self.dir = dir

class Maze():
    def __init__(self, Guard, maze_map, obj_loc):
        self.Guard = Guard
        self.start = (Guard.x, Guard.y)
        self.maze_map = maze_map #numpy matrix
        self.new_map = np.copy(maze_map) #Will update for each obstacle
        self.blocker = '#'
        self.max_rows = len(maze_map[0])
        self.max_cols = len(maze_map[1])
        self.obs_sets = set() #Track location and direction to provide numb of loop objects
        self.obj_loc = obj_loc #Where new obstacle can be set
        self.pt2_results = 0

    def go_E(self):
        while (self.Guard.y < self.max_cols):
            self.maze_map[self.Guard.x,self.Guard.y] = 'X' 
            self.Guard.y += 1 #Going right in map
            if self.Guard.y >= self.max_cols:
                break
            self.obs_sets.add((self.Guard.x,self.Guard.y,self.Guard.dir) )
            if (self.maze_map[self.Guard.x,self.Guard.y] == '#'):
                self.Guard.y -= 1
                self.Guard.dir = 'S'
                break
        if self.Guard.y >= self.max_cols:
            self.Guard.y -=1
            self.obs_sets.add((self.Guard.x,self.Guard.y,self.Guard.dir) )
            self.maze_map[self.Guard.x,self.Guard.y] = 'X' 
            return False
        else:
            return True

    def go_W(self):
        while (self.Guard.y >= 0):
            self.maze_map[self.Guard.x,self.Guard.y] = 'X' 
            self.Guard.y -= 1 #Going up in map
            if self.Guard.y < 0:
                break
            self.obs_sets.add((self.Guard.x,self.Guard.y,self.Guard.dir) )
            if (self.maze_map[self.Guard.x,self.Guard.y] == '#'):
                self.Guard.y += 1
                self.Guard.dir = 'N'
                break
        if self.Guard.y < 0:
            self.Guard.y += 1
            self.maze_map[self.Guard.x,self.Guard.y] = 'X' 
            return False
        else:
            return True

    def go_S(self):
        while (self.Guard.x < self.max_rows):
            self.maze_map[self.Guard.x,self.Guard.y] = 'X' 
            self.Guard.x += 1 #Going down in map
            if self.Guard.x >= self.max_rows:
                break
            self.obs_sets.add((self.Guard.x,self.Guard.y,self.Guard.dir) )
                
            if (self.maze_map[self.Guard.x,self.Guard.y] == '#'):
                self.Guard.x -= 1
                self.Guard.dir = 'W'
                break
        if self.Guard.x >= self.max_rows:
            self.Guard.x -= 1
            self.maze_map[self.Guard.x,self.Guard.y] = 'X' 
            # self.maze_map[self.Guard.x,self.Guard.y] = 'X' 
            return False
        else:
            return True

    def go_N(self):
        while (self.Guard.x >= 0):
            self.maze_map[self.Guard.x,self.Guard.y] = 'X' 
            self.Guard.x -= 1 #Going up in map
            if self.Guard.x < 0:
                break
            self.obs_sets.add((self.Guard.x,self.Guard.y,self.Guard.dir) )
            if (self.maze_map[self.Guard.x,self.Guard.y] == '#'):
                self.Guard.x += 1
                self.Guard.dir = 'E'
                # self.obs_sets.add((self.Guard.x,self.Guard.y,self.Guard.dir) )
                break
        if self.Guard.x < 0:
            self.Guard.x += 1
            self.maze_map[self.Guard.x,self.Guard.y] = 'X' 
            return False
        else:
            return True
    
    def run_maze(self):
        guard_place_chk = True#Goes false when off map
        while guard_place_chk:
            if self.Guard.dir == 'N':
                guard_place_chk = self.go_N()
            elif self.Guard.dir == 'S':
                guard_place_chk = self.go_S()
            elif self.Guard.dir == 'E':
                guard_place_chk = self.go_E()
            else:
                guard_place_chk = self.go_W()
    def run_maze_pt2(self): 
        #Update map with new object
        for new_obstacle in self.obj_loc: 
            self.maze_map = np.copy(self.new_map)
            self.maze_map[new_obstacle] = '#'
            #Reset startin guard loc and dir
            self.Guard.x,self.Guard.y = self.start
            if(self.start == new_obstacle):
                continue
            self.Guard.dir = 'N'

            self.obs_sets = set() #Track location and direction to provide numb of loop objects
            guard_place_chk = True#Goes false when off map
            while guard_place_chk:
                if self.Guard.dir == 'N':
                    guard_place_chk = self.go_N()
                elif self.Guard.dir == 'S':
                    guard_place_chk = self.go_S()
                elif self.Guard.dir == 'E':
                    guard_place_chk = self.go_E()
                else:
                    guard_place_chk = self.go_W()

                if guard_place_chk:
                    if (self.Guard.x,self.Guard.y,self.Guard.dir) in self.obs_sets:
                        self.pt2_results+=1 
                        break
                    self.obs_sets.add((self.Guard.x,self.Guard.y,self.Guard.dir) )

                

#Reading Original Map
D = open(sys.argv[1]).read().strip()
L = D.split('\n')

with open(sys.argv[1]) as f:
    maze_raw = f.readlines()
maze_raw = [list(row.strip('\n')) for row in maze_raw]
maze_2d_arr = np.array(maze_raw, ndmin=2)

#Reading Solved map to use as new obs locations
D = open(sys.argv[2]).read().strip()
L = D.split('\n')

with open(sys.argv[2]) as f:
    obj_raw = f.readlines()

obj_map_raw = [list(row.strip('\n')) for row in obj_raw]
obj_map_arr = np.array(obj_map_raw, ndmin=2)
x_obs, y_obs = np.where(obj_map_arr == 'X')
obs_locs = list(zip(x_obs, y_obs))

row_len = maze_2d_arr.shape[0]
col_len = maze_2d_arr.shape[1]
# map_data = np.loadtxt(sys.argv[1], dtype=str)
start_loc = np.argwhere(maze_2d_arr=='^')[0]
guard_obj = GuardPiece(start_loc[0], start_loc[1])
maze_obj = Maze(guard_obj,maze_2d_arr, obs_locs) 
        
# maze_obj.run_maze()
# print("Total Spots: ", np.sum(maze_obj.maze_map=='X'))
maze_obj.run_maze_pt2()
print(maze_obj.maze_map)
# np.savetxt("maze_pt1_EXAMPLE.txt", maze_obj.maze_map, delimiter="", fmt='%c')
print("Total Potential Obstacles: ", maze_obj.pt2_results)