N = int(input())
arr = [[0] * 102 for _ in range (102)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(N):
    left, under = map(int, input().split())
    for i in range(left, left + 10):
        for j in range(under, under + 10):
            arr[i][j] = 1

cnt = 0
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1:
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if arr[nx][ny] == 0:
                    cnt += 1
print(cnt)