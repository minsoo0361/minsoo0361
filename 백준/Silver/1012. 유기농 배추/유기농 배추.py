import sys
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = True
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny]== 1:
            dfs(nx, ny)


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]


    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)