import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
queue = deque()
for i in range(N):
    arr = list(map(str, input().split()))
    if arr[0] == 'push_front':
        queue.appendleft(int(arr[1]))
    elif arr[0] == 'push_back':
        queue.append(int(arr[1]))
    elif arr[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif arr[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif arr[0] == 'size':
        print(len(queue))
    elif arr[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif arr[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
