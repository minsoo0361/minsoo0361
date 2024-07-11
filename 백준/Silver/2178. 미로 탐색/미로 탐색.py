def bfs(x, y):
    queue.append([0, 0])
    while queue:    
        x, y = queue.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                queue.append([nx, ny])
                arr[nx][ny] = arr[x][y] + 1
    print(arr[N-1][M-1])

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = []

bfs(0, 0)
 