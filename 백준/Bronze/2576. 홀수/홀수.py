n = 7
arr = []
for _ in range(n):
    num = int(input())
    if num % 2 != 0:
        arr.append(num)
    arr.sort()
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])