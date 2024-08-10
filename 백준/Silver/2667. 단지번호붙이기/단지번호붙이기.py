def bfs(x, y):
    global cnt  
    visited[x][y] = True
    queue = []
    queue.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        cx, cy = queue.pop(0)
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == 1:
                cnt += 1
                visited[nx][ny] = True
                queue.append((nx, ny))               
    return cnt

        

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[False] * (N) for _ in range(N)]
answer = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] > 0:
            cnt = 1
            bfs(i, j)
            answer.append(bfs(i, j))
answer.sort()
print(len(answer))
for i in answer:
    print(i)

# def dfs(x, y):
#     global cnt  
#     visited[x][y] = True
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > 0 and not visited[nx][ny]:
#             cnt += 1
#             dfs(nx, ny)

# N = int(input())
# arr = [list(map(int, input())) for _ in range(N)]
# visited = [[False] * (N) for _ in range(N)]
# answer = []
# for i in range(N):
#     for j in range(N):
#         cnt = 0
#         if not visited[i][j] and arr[i][j] > 0:
#             cnt += 1
#             dfs(i, j)
#             answer.append(cnt)
# answer.sort()
# print(answer)