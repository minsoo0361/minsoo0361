N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))

    if N == 1 :
        print(max(arr) ** 2)
        break
    else:
        print(min(arr) * max(arr))
        break

