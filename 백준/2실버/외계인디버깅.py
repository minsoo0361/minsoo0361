N, P = map(int, input().split())
stack = [[] for  in range(7)]
cnt = 0

for  in range(N):
    line, fret = map(int, input().split())
    #만약에 스택의 길이가 0이거나, 넣을 멜로디와 번줄이 같고 프렛이 오름차순으로 유지된다면?
    if not stack[line] or (stack[line] and fret > stack[line][-1]):
        stack[line].append(fret)
        cnt += 1

    # 만야에 스택에 인자가 존재하고 넣을 프렛이 마지막 프렛보다 작을 경우
    elif stack[line] and fret < stack[line][-1]:
        while stack[line] and fret < stack[line][-1]:
            stack[line].pop()
            cnt += 1
            if not stack[line] or stack[line][-1] < fret:
                stack[line].append(fret)
                cnt += 1

print(cnt)