import sys
input = sys.stdin.readline

def dfs(start, count):
    global flag
    visited[start] = True
    if start == B:
        flag = True
        print(count)
    for w in graph[start]:
        if not visited[w]:
            dfs(w, count+1)


N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] * N for _ in range(N+1)]
visited = [False] * (N+1)
flag = False
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(A, 0)
if flag == False:
    print(-1)


