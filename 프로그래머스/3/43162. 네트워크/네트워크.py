from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(i, n, computers, visited)
    return answer

def bfs(start_node, n, computers, visited):
    queue = deque([start_node])
    visited[start_node] = True
    
    while queue:
        u = queue.popleft()
        
        for v in range(n):
            if computers[u][v] == 1 and u != v and not visited[v]:
                visited[v] = True
                queue.append(v)
            
