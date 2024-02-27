import sys
input = sys.stdin.readline
from collections import deque
queue = deque()

N = int(input())
for _ in range(N):
    command = list(input().split())
    if command[0] == '1':
        queue.appendleft(command[1])
    elif command[0] == '2':
        queue.append(command[1])

    elif command[0] == '3':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == '4':
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == '5':
        print(len(queue))
    elif command[0] == '6':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == '7':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == '8':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)

