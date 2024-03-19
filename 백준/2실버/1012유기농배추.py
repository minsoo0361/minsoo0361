
# dfs : 재귀의 특징을 이용해서 짜는것..
        # 스택 구조를 이용해서 짜는것데

def dfs(v, graph, visited):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(w, graph, visited)

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
# graph[1] = [2, 3]
# graph[2] = [1, 3]
# graph[3] = [1, 2]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)



# 스택 => 재귀 함수!! 이용 => 시스템 프그램의 스택을 이용함.
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] > 0: # 배열 범위 안이고 방문하지 않았을떄
            dfs(nx, ny)


# 큐를 사용 => deque()
from collections import deque
def bfs(x, y):
    cnt = 0
    visited = [[0] for _ in range(N)]
    visited[x][y] = 1 # 방문 처리
    dq = deque()
    dq.append((x, y))

    while dq:
        c_x, c_y = dq.popleft()
        cnt += 1

        if arr[c_x][c_y] == 3:

            return visited[nx][ny]

        for d in range(4):
            nx = c_x + dx[d]
            ny = c_y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] > 0:  # 배열 범위 안이고 방문하지 않았을떄
                visited[nx][ny] = visited[c_x][c_y] + 1
                dq.append((nx, ny))


    return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] > 0:
            cnt = 0
            dfs(i, j)
            result.apend(cnt)

