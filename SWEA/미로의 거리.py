dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def solution(maze, N):
    # 시작지점 2, 도착지점 3
    def get_point():
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    sx, sy = i, j
                elif maze[i][j] == 3:
                    ex, ey = i, j
        return sx, sy, ex, ey
    sx, sy, ex, ey = get_point()
    maze[ex][ey] = 0
    # BFS 탐색 방법으로 시작점에서부터 도착지점으로 도달할 수 있는가
    def bfs(sx, sy):
        # 미로에다가 내가 방문한 지점을 벽 1으로 만들기.
        queue = []
        maze[sx][sy] = 0   # 방문체크
        queue.append((sx, sy))

        # 큐가 빌 때 까지 (더 이상 방문할 수 있는 노드 X)
        while queue:
            # 큐에서 좌표값을 하나 꺼내오고
            x, y  = queue.pop(0)

            # 해당 좌표에서 상하좌우 탐색...
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 좌표가 바깥을 벗어난 경우나, 벽을 만난 경우는 무시
                if 0 > nx or 0 > ny or N <= nx or N <= ny or maze[nx][ny] >= 1:
                    continue
                # (nx, ny) 방문을 해줘야 하므로
                maze[nx][ny] = maze[x][y] + 1
                # (nx, ny) 좌표가 도착 지점일때 (= 3의 값을 가질때)
                if ex == nx and ey == ny:
                    return maze[ex][ey]

                queue.append((nx, ny))
        return 0

    # 도착지점에 도달한 경우를 참 거짓으로 반환
    result = bfs(sx, sy)
    # result 값이 0이라면 도달하지 못한 경우이다
    if result == 0 :
        return 0
    else:
        return result - 1
    # return
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    result = solution(maze, N)
    print(f'#{tc} {result}')




# def bfs(x, y):
#     visited[x][y] = True
#     q = []
#     q.append(visited[x][y])
#     global result
#     while q:
#         t = q.pop(0)
#         if t ==
#
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if  0 <= nx < 101 and 0 <= ny < 101 and maze[nx][ny] == 0 and visited[nx][ny] == False:
#             bfs(nx, ny)





