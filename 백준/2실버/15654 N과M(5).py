import sys
input = sys.stdin.readline
def back(n):
    if n == M:
        print(*lst)
        return

    for i in range(N):
        if arr[i] in lst:
            continue
        lst.append(arr[i])
        back(n + 1)
        lst.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

lst = []
back(0)