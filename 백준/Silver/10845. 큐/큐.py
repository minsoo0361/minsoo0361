import sys
input = sys.stdin.readline
N = int(input())
queue = []
for i in range(N):
    lst = list(map(str, input().split()))
    if lst[0] == "push":
        queue.append(int(lst[1]))
    elif lst[0] == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif lst[0] == "size":
        print(len(queue))
    elif lst[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif lst[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif lst[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)