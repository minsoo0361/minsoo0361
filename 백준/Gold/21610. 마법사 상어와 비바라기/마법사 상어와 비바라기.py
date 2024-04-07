N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]
cloud = [(N-1, 0), (N-1, 1), (N-2,0), (N-2, 1)]

# 이동 방향 순서대로
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for m in move:
    d, s = m[0]-1, m[1] % N
    removed_cloud = []
    while cloud:
        x, y = cloud.pop()
        nx = (x + dx[d] * s) % N
        ny = (y + dy[d] * s) % N
        arr[nx][ny] += 1
        removed_cloud.append((nx, ny))

    for x, y in removed_cloud:
        cnt = 0
        for dir in range(1, 8, 2):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny]:
                    cnt += 1
        arr[x][y] += cnt

    for i in range(N):
        for j in range(N):
            if (i, j) not in removed_cloud:
                if arr[i][j] >= 2:
                    cloud.append((i, j))
                    arr[i][j] -= 2

total = 0
for lst in arr:
    total += sum(lst)
print(total)



