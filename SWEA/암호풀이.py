from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1,11):
    T = int(input())
    scr_lst = list(map(int, input().split()))
    dq = deque(scr_lst)

    while 1:
        for i in range(1,6):
            dq[0] -= i
            dq.rotate(-1)
            if dq[-1] <= 0:
                dq[-1] = 0
                break
        if dq[-1] == 0:
            break
    print(f'#{T}', *dq)