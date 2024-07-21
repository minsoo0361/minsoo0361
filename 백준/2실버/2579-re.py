N = int(input())
scores = list(int(input())for _ in range(N))
dp = [0] * N
dp[0] = scores[0]
dp[1] = scores[0] + scores[1]
dp[2] = max(scores[0] + scores[2] , scores[1]+scores[2])

for i in range(3, N):
    dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i] + scores[i-1])
print(dp)
print(dp[N-1])