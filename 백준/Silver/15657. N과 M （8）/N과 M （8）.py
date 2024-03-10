def back(n):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(n, N):
        lst.append(arr[i])
        back(i)
        lst.pop()


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
lst = []
back(0)