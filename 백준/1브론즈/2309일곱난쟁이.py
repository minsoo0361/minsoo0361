dwarf = []
for i in range(9):
    arr = int(input())
    dwarf.append(arr)
dwarf.sort()
sum_nm = sum(dwarf)
for i in range(len(dwarf)):
    for j in range(i+1, len(dwarf)):
        if sum_nm - dwarf[i] - dwarf[j] == 100:
            for k in range(len(dwarf)):
                if k == i or k == j:
                    continue
                else:
                    print(dwarf[k])
            exit()
