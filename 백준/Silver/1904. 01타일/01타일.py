def dp_f(n):
    dp = [0] * 1000001
    dp[1] = 1
    dp[2] = 2

    if n > 2:
        for i in range(3, N+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 15746
    return dp[n]



N = int(input())
print(dp_f(N))