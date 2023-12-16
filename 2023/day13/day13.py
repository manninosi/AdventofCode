import numpy as np

# fn = "day13.in"
fn = "day13.ex"

with open(fn) as f:
    mirror_map_raw = f.readlines()

mirror_map_raw = [(row.strip('\n')) for row in mirror_map_raw]
list_store = []
list_final = [[]]
for rows in mirror_map_raw:
    if len(rows) == 0: #Blank row
        list_final[-1] = list_store
        list_final.append([])
        list_store = []
        continue
    list_store.append(np.array(list(rows),ndmin=2))
list_final[-1] = list_store

# mir_2d_arr = np.array(list_final, ndmin=3)

result = 0
print("length of section: ", len(list_final))
for section_raw in list_final: #Going through each section
    print('='*30)
    section = np.array(section_raw, ndmin=2)
    #Loop through each row
    found_reflection = 0
    for i, row in enumerate(section[:-1]):
        if np.all(row == section[i+1]):#Find first reflection point
            end_chk = 0
            U_idx = i
            B_idx = i+1
            while U_idx>0 and B_idx < len(section)-1 and np.all(section[U_idx] == section[B_idx]):
                print(U_idx)
                print(B_idx)
                print(section[U_idx])
                print(section[B_idx])
                U_idx -= 1
                B_idx += 1
                end_chk = 1
            if np.all(section[U_idx] == section[B_idx]):
                print("Reflection found!")
                found_reflection = 1 
                    

            if found_reflection == 1:
                #REFLECTION FOUND
                print("index: ", i)
                result += 100*(i+1)
                break
                pass

    #Loop through each column
    print('result: ', result)
    if found_reflection == 0: #No rows found            
        for i, col in enumerate(section.T[:-1]):
            if np.all(col == section.T[i+1]):#Find reflection point
                end_chk = 0
                L_idx = i
                R_idx = i+1
                while L_idx>0 and R_idx<len(section.T)-1 and np.all(section.T[L_idx] == section.T[R_idx]):
                    L_idx -= 1
                    R_idx += 1
                    # if L_idx <= 0 or R_idx >= len(section.T)-1 :
                    #     if L_idx < 0:
                    #         L_idx = 0
                    #     if R_idx > len(section.T) - 1:
                    #         R_idx = len(section.T) - 1
                if np.all(section.T[L_idx] == section.T[R_idx]):
                    print("Reflection found!")
                    found_reflection = 1 
                    end_chk = 1
            if found_reflection == 1:
                #REFLECTION FOUND
                print("index: ", i)
                result += (i+1)
                break
print(result)

