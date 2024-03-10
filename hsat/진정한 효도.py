import sys
input = sys.stdin.readline
N = 3
arr = [list(map(int, input().split()))for _ in range(N)]
dx, dy = [0, 1]
di, dj = [1, 0]
lst = []
for i in range(N):
    cnt = 0
    for j in range(N):
        nx = i + dx
        ny = j + dy
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] > arr[i][j]:
                cnt += arr[nx][ny] - arr[i][j]
                if arr[i][0] == arr[i][N-1] and arr[i][0] != arr[nx][ny]:
                    cnt = 1
                    break
                if cnt > 3:
                    cnt -= 2

            elif arr[nx][ny] < arr[i][j]:
                cnt += arr[i][j] - arr[nx][ny]
                if arr[i][0] == arr[i][N-1] and arr[i][0] != arr[nx][ny]:
                    cnt = 1
                    break
                if cnt > 3:
                    cnt -= 2
    lst.append(cnt)

for j in range(N):
    tmp = 0
    for i in range(N):
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] > arr[i][j]:
                if arr[0][j] == arr[N-1][j] and arr[0][j] != arr[ni][nj]:
                    tmp = 1
                    break
                tmp += arr[ni][nj] - arr[i][j]
                if tmp > 3:
                    tmp -= 2

            elif arr[ni][nj] < arr[i][j]:
                tmp += arr[i][j] - arr[ni][nj]
                if arr[0][j] == arr[N-1][j] and arr[0][j] != arr[ni][nj]:
                    tmp = 1
                    break
                if tmp > 3:
                    tmp -= 2
    lst.append(tmp)
print(min(lst))
