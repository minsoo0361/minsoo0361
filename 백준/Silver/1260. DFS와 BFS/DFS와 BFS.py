import sys
input = sys.stdin.readline
from collections import deque

def dfs(i):
    visited_dfs[i] = True
    print(i, end = ' ')
    for w in graph[i]:
        if not visited_dfs[w]:
            dfs(w)


def bfs(i):
    queue = deque()
    visited_bfs[i] = True
    queue.append(i)

    while queue:
        n = queue.popleft()
        print(n, end = ' ')
        for w in graph[n]:
            if not visited_bfs[w]:
                visited_bfs[w] = True
                queue.append(w)


N, M, V = map(int, input().split())
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for k in graph:
    k.sort()

dfs(V)
print()
bfs(V)



