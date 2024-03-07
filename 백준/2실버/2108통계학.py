N = int(input())
arr = []
cnt = 0
lst = [0] * 8001
for _ in range(N):
    nm = int(input())
    arr.append(nm)
arr.sort()
a = sum(arr) // N
b = arr[N//2]
for i in range (len(lst)):



print(lst)
