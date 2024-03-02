T = int(input())
for tc in range(T):
    arr = list(map(int, input().split()))
    cnt = 0
    for _ in range(len(arr)):
        for j in range(2, len(arr)):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                cnt += 1
            else:
                continue
    print(arr[0], cnt)