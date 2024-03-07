N = 5
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)
    arr.sort()
print(sum(arr) // N)
print(arr[2])

