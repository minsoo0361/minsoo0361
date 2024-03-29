chess = [[0, 1, 0, 1, 0, 1, 0, 1],[1, 0, 1, 0, 1, 0, 1, 0]] * 4
N = 8
arr = []
cnt = 0
for _ in range(N):
    arr.append(list(input()))
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'F' and chess[i][j] == 0:
            cnt += 1
print(cnt)