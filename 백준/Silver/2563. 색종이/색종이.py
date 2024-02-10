N = int(input())
total = 0
arr = [[0] * 100 for _ in range(100)]
for _ in range(N):
    x,y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            arr[i][j] = 1
for k in range(100):
    total += sum(arr[k])

print(total)
