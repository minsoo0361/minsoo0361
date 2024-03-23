def dfs(start):
    global cnt
    visited[start] = cnt
    graph[start].sort()

    for w in graph[start]:
        if visited[w] == 0:
            cnt += 1
            dfs(w)


import sys
sys.setrecursionlimit(150000)
N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(R)

for i in range(1, N + 1):
    print(visited[i])
