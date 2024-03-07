T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[False]*N for _ in range(N)]
    maze = [list(map(int, input().rstrip())) for _ in range(N)]
    result = 0
    # 상, 하, 좌, 우 방향을 나타내는 리스트
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j

    # DFS 함수 정의
    def DFS(x, y):
        visited[x][y] = True # 현재 위치를 방문 처리
        global result
        # 네 방향을 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 미로 범위 내에 있고, 아직 방문하지 않은 위치라면
            if nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == 0 and visited[nx][ny] == False:
                DFS(nx, ny) # DFS로 이동
            elif nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == 3:
                result = 1
        return result

    DFS(si, sj)
    print(f'#{tc} {result}')