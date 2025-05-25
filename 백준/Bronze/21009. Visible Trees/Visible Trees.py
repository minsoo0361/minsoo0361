N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lst_col = []
lst_row = []

for j in range(N):
    num = arr[0][j]
    cnt = 1
    for i in range(N):
        if arr[i][j] > num:
            num = arr[i][j]
            cnt += 1
    lst_row.append(cnt)
print(*lst_row)

        
for i in range(N):
    num = arr[i][0]
    cnt = 1
    for j in range(1, N):
        if arr[i][j] > num:
            num = arr[i][j]
            cnt += 1
    lst_col.append(cnt)
for i in range(len(lst_col)):
    print(lst_col[i])