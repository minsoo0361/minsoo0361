T = int(input())
for tc in range (1, T+1):
    dp = [[0] * (100001) for _ in range(2)]
    N = int(input())
    lst = [list(map(int, input().split())) for i in range(2)]
    if N == 1:
        print(max(lst[0][0], lst[1][0]))
        continue
    dp[0][0] = lst[0][0]
    dp[1][0] = lst[1][0]
    dp[0][1] = dp[1][0] + lst[0][1]    
    dp[1][1] = dp[0][0] + lst[1][1]

    for j in range(2, N):
        dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + lst[0][j]
        dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + lst[1][j]
    print(max(max(dp[0]),max(dp[1])))
