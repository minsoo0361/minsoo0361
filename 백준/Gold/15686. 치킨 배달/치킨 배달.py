def dfs(idx):
    global answer
    if idx >= len(chicken):
        if len(now_chicken) != M:
            return
        sum = 0
        for i in range(len(house)):
            minimun_size = 3000
            for k in range(len(now_chicken)):
                minimun_size = min(minimun_size, abs(house[i][0] - now_chicken[k][0]) + abs(house[i][1] - now_chicken[k][1]))
            sum += minimun_size

        answer = min(answer, sum)
        return

    now_chicken.append(chicken[idx])
    dfs(idx+1)
    now_chicken.pop()
    dfs(idx+1)

N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
answer = 9999
house = []
chicken = []
now_chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i, j])
        if arr[i][j] == 2:
            chicken.append([i, j])
dfs(0)
print(answer)

