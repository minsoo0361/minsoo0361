def dfs(cnt, sum_height):
    # 기저 조건
    if sum_height >= B:
        ans.append(sum_height)
        return

    if cnt == N:
        return

    # 쌓을 때
    dfs(cnt+1, sum_height+height[cnt])

    # 안쌓을때
    dfs(cnt+1, sum_height)


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    ans = []

    dfs(0, 0)
    print(f'#{tc} {min(ans)-B}')
