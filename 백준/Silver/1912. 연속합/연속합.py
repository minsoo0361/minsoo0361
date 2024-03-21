N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
# dp 배열 생성
dp[0] = arr[0]
# dp의 첫번째 인덱스 = arr 첫번째 인덱스 해주는 이유
# 누적합을 계산해야하기 때문에 첫번째 원소는 필요
for i in range(1, N):
    dp[i] = max(arr[i], dp[i-1] + arr[i])
    # dp[1] = arr[1]과 dp[0] + arr[1]을 비교하여
    # 더 큰 것을 dp[1]에 넣기
    # arr[1] = -4, dp[0] + arr[1] = 6
    # i가 1일 때 dp = [10, 6, 0...]
print(max(dp))


