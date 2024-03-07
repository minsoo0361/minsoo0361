import sys
sys.stdin = open('input.txt', 'r')
T = 10
for _ in range (1, T+1):
    tc = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range (N)]
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sx, sy = i, j
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]



    def BFS(x, y):
        global maze
        queue = []
        queue.append([x, y])
        visited[x][y] = True
        if maze[x][y] == 3:
            return 1
        while queue:
            x, y = queue.pop(0)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == 0 and visited[nx][
                    ny] == False:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                elif nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[nx][ny] == 3:
                    return 1
        return 0
    print(f'#{tc}', BFS(sx, sy))
