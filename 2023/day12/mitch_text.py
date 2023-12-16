#Trying recursive and dynamic programming

fn = 'day12ex.txt'

data = open(fn).read().strip()
springs = [x.split()[0] for x in data.split('\n')]
bc_arr = [[int(j) for j in x.split()[1].split(',')] for x in data.split('\n')]
DP = {}






def find_occ(spring, bc, i, bi, cur_broken):
    # key = (i,bi,cur_broken)
    # if key in DP:
    #     return DP[key]
    print(i)
    if i==len(spring): #Base case (reached end of string)
        print('here')
        # if bi == len(bc) and cur_broken > 0:
        #     return 0
        if bi==len(bc) and cur_broken==0: #Found number of consecutive broken springs
            return 1
        elif bc[bi] == cur_broken and bi==len(bc)-1:
            return 1
        else:
            return 0 #did not find broken srpings
    ans = 0
    for next_sym in ['.', '#']:
        if springs[i] == next_sym or spring[i]=='?':
            if next_sym == '.' and cur_broken == 0:
                ans += find_occ(spring, bc, i+1, bi, 0)
            elif next_sym == '.' and cur_broken > 0  and cur_broken == bc[bi] and bi<len(bc): #Found at least one hash tag previous
                ans += find_occ(spring, bc, i+1, bi+1, 0)
            elif next_sym == '#': #It is hashtag
                ans += find_occ(spring, bc, i+1, bi, cur_broken+1)
    # DP[key] = ans
    return ans
            

result = 0 
for idx, spring in enumerate(springs):
    # break
    print('='*60) 
    # print(find_occ(spring, bc_arr[i],0,0,0))

    result += find_occ(spring, bc_arr[idx], 0,0,0)
    DP.clear()
print(DP)
print(result)