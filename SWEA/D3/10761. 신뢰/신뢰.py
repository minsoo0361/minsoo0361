T = int(input())
for tc in range (1, T + 1):
    arr = list(map(str, input().split()))
    N = int(arr[0])
    arr = arr[1:]

    processing = []
    for i in range(0, len(arr), 2):
        color = arr[i]
        pos = int(arr[i+1])
        processing.append((color, pos))

    O_nxt = []
    B_nxt = []
    for color, pos in processing:
        if color == 'O':
            O_nxt.append(pos)
        elif color == 'B':
            B_nxt.append(pos)

    time = 0
    O_pos = 1
    B_pos = 1

    while processing:
        O_actioned = False
        B_actioned = False

        if O_nxt:
            if O_pos < O_nxt[0]:
                O_pos += 1
                O_actioned = True
            elif O_pos > O_nxt[0]:
                O_pos -= 1
                O_actioned = True
        if B_nxt:
            if B_pos < B_nxt[0]:
                B_pos += 1
                B_actioned = True
            elif B_pos > B_nxt[0]:
                B_pos -= 1
                B_actioned = True

        if O_actioned == False and processing[0] == ('O', O_pos):
            O_nxt.pop(0)
            processing.pop(0)
        elif B_actioned == False and processing[0] == ('B', B_pos):
            B_nxt.pop(0)
            processing.pop(0)

        time += 1
    print(f'#{tc} {time}')


