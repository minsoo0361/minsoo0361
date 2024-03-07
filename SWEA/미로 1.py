T = int(input())
for tc in range(1, T+1):
    N = int(input())
    for _ in range(N):
        maze = int(input())
        is_success = False    # 도착지점에 도달한 경우 False
        dx = [0, 0 ,-1, 1]
        dy = [-1, 1, 0, 0]
        # 방문체크를 할 N * N 배열
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:   #시작점
                sx, sy = (i, j)
            elif maze[i][j] == 3:
                ex, ey = (i, j)


    def dfs(x, y):
        if x == ex and y == ey:
            is_success = True
            return
        # 상하좌우 탐색
        for d in range(4):
            # 다음 이동할 좌표 (nx, ny)
            nx = x + dx[d]
            ny = y + dy[d]

            # 해당 좌표가 갈 수 있는 좌표인지
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    dfs(nx, ny)


    # 시작점에서부터 모든 경로를 탐색
    dfs(sx, sy)
    if is_success:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')