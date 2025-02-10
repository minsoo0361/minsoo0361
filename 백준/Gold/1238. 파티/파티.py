import heapq

def dijstra_end(end): # 여기에는 파라미터 값으로 X넣기
    INF = 1e9
    end_dist = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, end))
    end_dist[end] = 0

    while q:
        distance, node = heapq.heappop(q)
        if distance > end_dist[node]:
            continue
        for n in graph[node]:
            new_cost = n[1] + end_dist[node]
            if new_cost < end_dist[n[0]]:
                end_dist[n[0]] = new_cost
                heapq.heappush(q, (new_cost, n[0]))               
    return end_dist

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))
    # graph[1]에서 2로 갈 때 가중치 4, 3으로 갈 때 2, 4로 갈때 7
    # 도착지점이 X라면 정지. 없다면 경유해서 가도록.
    # 2에서 출발해서 1로 도착할때는 1, 3으로 도착할땐 3, 4로 도착할게 없으면
    # 1로 경유해서 4로 가도록.
dijstra_end(X)
answer = dijstra_end(X)
lst = []
for i in range(1, N+1):
    result = dijstra_end(i)
    lst.append(answer[i] + result[X])
print(max(lst))
  