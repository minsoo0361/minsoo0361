N = 9
arr = [list(map(int, input().split()))for _ in range(N)]
mx_nm = 0
row = 0
col = 0
for i in range(N):
    for j in range(N):
        if mx_nm <= arr[i][j]:
            mx_nm = arr[i][j]
            row = i + 1
            col = j + 1
print(mx_nm)
print(row, col)