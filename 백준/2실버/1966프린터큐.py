import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = deque(map(int, input().split()))
    ord = [i for i in range(N)]
    cnt = 0

    while True:
        if arr[0] == max(arr):
            cnt += 1
            if ord[0] == M:
                print(cnt)
                break
            else:
                ord.pop(0)
                arr.popleft()
        else:
            ord.append(ord[0])
            ord.pop(0)
            arr.append(arr[0])
            arr.popleft()






