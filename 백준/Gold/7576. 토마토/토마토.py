from collections import deque
def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))

M, N = map(int, input().split())    # M과 N의 입력값이 반대 생각하기
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
cnt = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j))
bfs()
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    cnt = max(cnt, max(i))
print(cnt-1)