N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
dp = [0] * N
dp[0] = arr[0]
if N > 1: dp[1] = arr[0] + arr[1]
if N > 2: dp[2] = max(dp[1], arr[0] + arr[2], arr[1] + arr[2])
if N > 3:
    for i in range(3, N):
        dp[i] = max(dp[i-1], (arr[i]+dp[i-2]), (arr[i] + arr[i-1] + dp[i-3]))

print(dp[N-1])



