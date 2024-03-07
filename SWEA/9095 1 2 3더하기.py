def dfs(cnt, sm):
    global total
    if sm == n:
        total += 1
        return
    if cnt == n:

        return
    dfs(cnt + 1, sm + 1)
    dfs(cnt + 1, sm + 2)
    dfs(cnt + 1, sm + 3)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    total = 0

    dfs(0, 0)
    print(total)
