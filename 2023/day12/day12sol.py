import sys
# import re
# from copy import deepcopy
# from math import gcd
# from collections import defaultdict, Counter, deque
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]

data = open(sys.argv[1]).read().strip()
springs = [x.split()[0] for x in data.split('\n')]
bc_arr = [[int(j) for j in x.split()[1].split(',')] for x in data.split('\n')]
# i == current position within dots
# bi == current position within blocks
# current == length of current block of '#'
# state space is len(dots) * len(blocks) * len(dots)
DP = {}
def f(dots, blocks, i, bi, current):
    print(dots)
    key = (i, bi, current)
    #   if key in DP:
    #     return DP[key]
    print(i)
    if i==len(dots):
        if bi==len(blocks) and current==0:
            return 1
        elif bi==len(blocks)-1 and blocks[bi]==current:
            return 1
        else:
            return 0
    ans = 0
    for c in ['.', '#']:
        if dots[i]==c or dots[i]=='?':
            if c=='.' and current==0:
                ans += f(dots, blocks, i+1, bi, 0)
            elif c=='.' and current>0 and bi<len(blocks) and blocks[bi]==current:
                ans += f(dots, blocks, i+1, bi+1, 0)
            elif c=='#':
                ans += f(dots, blocks, i+1, bi, current+1)
    #   DP[key] = ans
    return ans

for part2 in [False,True]:
  ans = 0
#   for line in L:
  for idx,spring in enumerate(springs):    
    # dots,blocks = line.split()
    # print(dots)
    if False:
      dots = '?'.join([dots, dots, dots, dots, dots])
      blocks = ','.join([blocks, blocks, blocks, blocks, blocks])
    # blocks = [int(x) for x in blocks.split(',')]
    # print(len(blocks))
    DP.clear()
    score = f(spring, bc_arr[idx], 0, 0, 0)
    #print(dots, blocks, score, len(DP))
    ans += score
  print(ans)