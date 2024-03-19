def dfs(x, y):
    global cnt
    visited[x][y] = True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] >0:
            cnt += 1
            dfs(nx, ny)



N = int(input())
arr = [list(map(int, input()))for _ in range(N)]
visited = [[False] * (N) for _ in range(N)]
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] > 0:
            cnt = 1
            dfs(i, j)
            result.append(cnt)
result.sort()
print(len(result))
for i in result:
    print(i)