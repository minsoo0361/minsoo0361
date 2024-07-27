def dfs(idx):
    global ans
    if idx >= len(chicken):
        if len(real_chicken) != M:
            return
        
        sum = 0
        for i in range(len(house)):
            min_dist = 3000
            for k in range(len(real_chicken)):
                min_dist = min(min_dist, abs(house[i][0] - real_chicken[k][0]) + abs(house[i][1] - real_chicken[k][1]))
            
            sum += min_dist
        ans = min(ans, sum)
        return

    real_chicken.append(chicken[idx])
    dfs(idx+1)
    real_chicken.pop()
    dfs(idx+1)    

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
real_chicken = []
ans = 9999
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i, j])
        if arr[i][j] == 2:
            chicken.append([i, j])

dfs(0)
print(ans)