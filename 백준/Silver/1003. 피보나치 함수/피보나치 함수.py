T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    ans = 0
    dp = [0] * 42
    dp[0] = 1
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4, 42):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N],dp[N+1])


