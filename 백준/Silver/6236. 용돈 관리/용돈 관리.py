N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
end = sum(arr)
start = max(arr)
while start <= end:
    mid = (start + end) // 2
    money = mid
    cnt = 1

    for i in arr:        
        if money - i >= 0:
            money = money - i         
        else:
            money = mid - i
            cnt += 1
    if cnt <= M:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)
