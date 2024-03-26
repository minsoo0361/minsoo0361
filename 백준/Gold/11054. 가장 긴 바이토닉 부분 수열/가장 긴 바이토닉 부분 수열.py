N = int(input())
arr = list(map(int, input().split()))
reverse_arr = arr[::-1]
dp = [1] * N
reverse_dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
        if reverse_arr[i] > reverse_arr[j]:
            reverse_dp[i] = max(reverse_dp[i], reverse_dp[j]+1)
r_dp = reverse_dp[::-1]
result = []
for i in range(N):
    result.append(dp[i] + r_dp[i])
print(max(result)-1)