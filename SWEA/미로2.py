T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[False]*N for _ in range(N)]
    maze = [list(map(int, input().rstrip())) for _ in range(N)]
    cnt = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                ri, rj = i, j


    def DFS(x, y):
        visited[x][y] = True
        global cnt

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == 0 and visited[nx][ny] == False:
                DFS(nx, ny)
                cnt += 1
            elif nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == 3:
                break
        return cnt

    DFS(ri, rj)
    print(f'#{tc} {cnt}')