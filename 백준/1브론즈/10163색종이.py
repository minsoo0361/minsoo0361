N = int(input())
arr = [[0] * 1002 for _ in range (1002)]
for a in range(1, N + 1):
    x, y, m, h = map(int, input().split())
    for i in range(x, x + m):
        for j in range(y, y + h):
            arr[i][j] = a

for s in range(1, N + 1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == s:
                cnt += 1
    print(cnt)

