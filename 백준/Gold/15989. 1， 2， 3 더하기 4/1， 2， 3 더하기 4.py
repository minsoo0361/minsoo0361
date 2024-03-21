# 모든 수는 1을 n만큼 곱한 것을 가지므로 dp배열을 [1]로 생성
dp = [1] * 10001
#print(dp)
for i in range(2, 10001):
    # 다음 2로 더해질때 하나씩 추가
    dp[i] += dp[i-2]
#print(dp)
for i in range(3, 10001):
    # 다음 3으로 더해질때 하나씩 추가
    dp[i] += dp[i-3]
#print(dp)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(dp[N])


