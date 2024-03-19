N = int(input())
arr = []
for _ in range(N):
    s, f = map(int, input().split())
    arr.append((s, f))

arr.sort(key = lambda x : (x[1], x[0]))

cnt = 1
end_time = arr[0][1]
for i in range(1, N):
    if end_time <= arr[i][0]:
        cnt += 1
        end_time = arr[i][1]

print(cnt)


