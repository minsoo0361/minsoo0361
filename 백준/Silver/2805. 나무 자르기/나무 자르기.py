N, M = map(int, input().split())
height = list(map(int, input().split()))
answer = []
low = 0
high = max(height)

while low <= high:
    middle = (low + high) // 2

    cnt = 0
    for i in height:
        if i >= middle:
            cnt += i - middle
    if cnt >= M:
        low = middle + 1
    else:
        high = middle - 1

print(low-1)
