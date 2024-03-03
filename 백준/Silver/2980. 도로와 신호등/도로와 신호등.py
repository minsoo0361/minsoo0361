import sys
input = sys.stdin.readline

N, L = map(int, input().split())
time = 0
local = 0
for _ in range(N):
    D, R, G = map(int, input().split())

    time += (D - local)
    local = D
    rg_t = time % (R + G)

    if R - rg_t > 0:
        time += (R - rg_t)

time += (L - local)
print(time)
