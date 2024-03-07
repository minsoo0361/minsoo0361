M = int(input())
N = int(input())
arr = []
for num in range(M, N+1):
    cnt = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
                break
        if cnt == 0:
            arr.append(num)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])

