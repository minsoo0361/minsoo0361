N = int(input())
dp = [[0]*1001 for _ in range(1001)]
for i in range(10):
    dp[0][i] = 1
for i in range(1, 1001):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
print(sum(dp[N-1]) % 10007)