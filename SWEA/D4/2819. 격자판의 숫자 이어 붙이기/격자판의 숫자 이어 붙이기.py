def dfs(depth, x, y):
    if depth == 7:
        lst.add(''.join(visited))
        return

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 4 and 0 <= ny < 4:
            visited[depth] = arr[nx][ny]
            dfs(depth+1, nx, ny)
            visited[depth] = 0

T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    lst = set()
    visited = [0] * 7
    for i in range(4):
        for j in range(4):
            visited[0] = arr[i][j]
            dfs(1, i, j)
    print(f'#{tc} {len(lst)}')

