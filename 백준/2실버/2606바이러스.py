import sys
input = sys.stdin.readline
def dfs(n):
    global cnt
    visited[n] = True
    for w in graph[n]:
        if not visited[w]:
            cnt += 1
            dfs(w)



N = int(input())
V = int(input())
visited = [False] * (N+1)
graph = [[] * N for _ in range(N+1)]
cnt = 0
for _ in range(V):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(cnt)

