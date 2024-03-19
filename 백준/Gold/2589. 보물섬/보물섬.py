import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))

    while queue:
        c_x, c_y = queue.popleft()

        for k in range(4):
            nx = c_x + dx[k]
            ny = c_y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == 'L':
                visited[nx][ny] = visited[c_x][c_y] + 1
                cnt = max(cnt, visited[nx][ny])
                queue.append((nx, ny))
    return cnt - 1


N, M = map(int, input().split())
arr = [list(input().rstrip())for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            result = max(result, bfs(i,j))
print(result)


