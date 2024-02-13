N = int(input())
arr = []
for i in range(N):
    nm = list(map(int, input().split()))
    arr.append(nm)
arr.sort()
for i in arr:
    print(i[0], i[1])
