import sys
input = sys.stdin.readline
def back(n):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(n, N):
        if arr[i] not in lst:
            lst.append(arr[i])
            back(i + 1)
            lst.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

lst = []
print(arr)
back(0)
