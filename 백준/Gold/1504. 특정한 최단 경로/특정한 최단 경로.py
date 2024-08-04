import heapq
def dijkstra(start):
    distance = [INF] * (N + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for v,w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))
    return distance
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int, input().split())

dist_start, dist_v1, dist_v2 = dijkstra(1), dijkstra(v1), dijkstra(v2)
tmp1 = dist_start[v1] + dist_v1[v2] + dist_v2[N]
tmp2 = dist_start[v2] + dist_v2[v1] + dist_v1[N]
if tmp1 >= INF and tmp2 >= INF:
    print(-1)
else:
    print(min(tmp1, tmp2))