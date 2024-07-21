def solution(triangle):
    dp = triangle
    N = len(dp)
    for i in range(1, N): # 1, 2, 3, 4
        for j in range(len(dp[i])): # 0, 1 / 0, 1, 2 / 0, 1, 2, 3 / 
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif i == j :
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    return max(dp[N-1])
    
    