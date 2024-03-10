import sys
input = sys.stdin.readline
N, M = map(int, input(). split())
limit_speed = [0] * 101
over_speed = [0] * 101
tmp = 0
for _ in range(N):
    height, speed = map(int, input().split())
    for i in range(tmp, tmp+height+1):
        if limit_speed[i] == 0:
            limit_speed[i] = speed
    tmp += height
tcp = 0
for _ in range(M):
    height, speed = map(int, input().split())
    for i in range(tcp, tcp+height+1):
        if over_speed[i] == 0:
            over_speed[i] = speed
    tcp += height

answer = 0
for i in range(101):
    mx = over_speed[i] - limit_speed[i]
    if mx > answer:
        answer = mx
print(answer)




