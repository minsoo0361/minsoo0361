K = int(input())
arr = []
for _ in range(6):
    arr.append(list(map(int, input().split())))
garo = 0
garo_idx = 0
sero = 0
sero_idx = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][0] == 1 or arr[i][0] == 2:
            if garo < arr[i][1]:
                garo = arr[i][1]
                garo_idx = i
        elif arr[i][0] == 3 or arr[i][0] == 4:
            if sero < arr[i][1]:
                sero = arr[i][1]
                sero_idx = i
a = (garo_idx + 3) % 6
b = (sero_idx + 3) % 6

big_rec = garo * sero
small_rec = arr[a][1] * arr[b][1]
t = big_rec - small_rec
print(t*K)










