import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, start):
    nm = [0] * (N+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        w = queue.popleft()
        for i in graph[w]:
            if i not in visited:
                nm[i] = nm[w] + 1
                visited.append(i)
                queue.append(i)
    return sum(nm)



N, M = map(int, input().split())
graph = [[] * N for _ in range(N+1)]
cnt = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
for i in range(1, N+1):
    result.append(bfs(graph, i))

print(result.index(min(result))+1)
