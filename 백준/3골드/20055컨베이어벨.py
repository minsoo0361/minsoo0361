from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * N)
ans = 0
while True:     # 무한 루프
    cnt = 0
    belt.rotate(1)     # 벨트 한바퀴 회전
    robot.rotate(1)    # 로봇도 한바퀴 회전
    robot[-1] = 0      # 로봇 마지막은 떨어지니까 0
    if 1 in robot:     # 로봇 안에 1이 있다면 진행하거나 가만히 있거나
        for i in range(N-2, -1, -1):
            if (robot[i+1] == 0) and (belt[i+1] != 0) and robot[i] == 1:
                robot[i] = 0
                robot[i+1] = 1
                belt[i+1] -= 1
        robot[-1] = 0
    if (belt[0] != 0) and (robot[0] == 0):
        belt[0] -= 1
        robot[0] = 1

    for i in range(N*2):
        if belt[i] == 0:
            cnt += 1
    if cnt >= K:
        break
    ans += 1

print(ans+1)









