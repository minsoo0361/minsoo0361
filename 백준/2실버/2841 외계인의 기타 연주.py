N, P = map(int, input().split())
stack = [[] for _ in range(7)]# [[] [1] [2] [3] [4] [5] [6] ]
cnt = 0
for i in range(1, N + 1):
    line, plat = map(int, input(). split())

    if len(stack[line]) == 0:   # 2, 8
        stack[line].append(plat)
        cnt += 1
    elif len(stack[line]) != 0:
        while plat < stack[line][-1]:
            stack[line].pop()
            cnt += 1
            if len(stack[line]) == 0:
                stack[line].append(plat)
                cnt += 1
        if plat == stack[line][-1]:
            continue
        else:
            stack[line].append(plat)
            cnt += 1

print(cnt)
