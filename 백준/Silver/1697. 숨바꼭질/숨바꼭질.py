from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        v = queue.popleft()
        if v == K:
            print(visited[v])
            break
            
        for next_to in (v-1, v+1, v*2):
            if 0<= next_to < (10**5+1)and not visited[next_to]:
                visited[next_to] = visited[v] + 1
                queue.append(next_to)

N, K = map(int, input().split())
visited = [0] * (10**5 +1)
bfs()


