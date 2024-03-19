import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().rstrip()))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
            queue.append((nx, ny))
            arr[nx][ny] = arr[x][y] + 1

print(arr[N-1][M-1])
