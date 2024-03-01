C, R = map(int, input().split())
K = int(input())

arr = [[0] * C for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1
k = 0

sx = R - 1
sy = 0
arr[sx][sy] = 1

while True:
    # 기저조건
    if cnt == C * R:
        break
    nx = sx + dx[k]
    ny = sy + dy[k]

    if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == 0:
        cnt += 1
        arr[nx][ny] = cnt
        sx = nx
        sy = ny

    else:
        k += 1
        if k >= 4:
            k = k % 4

for i in range(R):
    for j in range(C):
        if arr[i][j] == K:
            print(j+1, R-i)

if  K > C * R:
    print(0)



