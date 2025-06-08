M = int(input())
arr = [1, 2, 3]
for _ in range(M):
    X, Y = map(int, input().split())
    x = arr.index(X)
    y = arr.index(Y)
    arr[x], arr[y] = arr[y], arr[x]
print(arr[0])
