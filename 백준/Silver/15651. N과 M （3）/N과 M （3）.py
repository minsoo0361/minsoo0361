def back():
    if len(arr) == M:
        print(*arr)
        return
    else:
        for i in range(1, N+1):
            arr.append(i)
            back()
            arr.pop()


N, M = map(int, input().split())
arr = []
back()


# N = 3일때, arr = [1, 2, 3]
# 하나선택해서