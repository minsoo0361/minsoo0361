dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, z):
    if len(z) < 6:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                dfs(nx, ny, z + graph[nx][ny])
                

    elif len(z) == 6:
        return answer.add(z)
    

N = 5
graph = [list(input().split()) for _ in range(N)]
answer = set()

for i in range(N):
    for j in range(N):
        num = graph[i][j]
        dfs(i, j, num)

print(len(answer))