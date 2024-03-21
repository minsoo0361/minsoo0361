dp = [0, 1, 1, 1, 2, 2]
for i in range(5, 101):
    dp[i] = dp[i-2] + dp[i-3]
    dp.append(i)
T = int(input())
for tc in range(T):
    n = int(input())
    print(dp[n])