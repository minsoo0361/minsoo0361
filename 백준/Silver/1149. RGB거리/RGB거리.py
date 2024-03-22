N = int(input())
dp = [0] * 3
color = list(map(int, input().split()))
for i in range(1, N):
    R, G, B = map(int, input().split())
    dp[0] = R + min(color[1], color[2])
    dp[1] = G + min(color[0], color[2])
    dp[2] = B + min(color[0], color[1])
    for j in range(3):
        color[j] = dp[j]
print(min(dp))


