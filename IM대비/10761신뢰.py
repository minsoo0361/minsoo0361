# 테스트케이스 수 T
T = int(input())
for tc in range(1, T + 1):
    # 입력
    # "4 B 2 O 1 O 2 B 4"
    arr = input().split()  # ["4", "B", "2", "O", "1" ,"O" ,"2" ,"B", "4"]
    # 눌러야하는 버튼의 갯수 N
    N = int(arr[0])  # 4
    arr = arr[1:]  # ["B", "2", "O", "1" ,"O" ,"2" ,"B", "4"]

    # 해야할 일 processing
    processing = []
    for i in range(0, len(arr), 2):
        color = arr[i]  # B랑 O를 구분
        pos = int(arr[i + 1]) # 이동할 위치
        processing.append((color, pos))

    # 현재 시간을 0으로 초기화
    time = 0

    # 로봇이 필요로하는 변수들 초기화 (현재 위치)
    O_pos = 1
    B_pos = 1

    # 로봇이 각각 다음으로 갈 좌표들 (리스트)
    O_nxts = []
    B_nxts = []
    for color, pos in processing:
        if color == 'O':
            # 오렌지 로봇이 가야할 다음 좌표
            O_nxts.append(pos)
        elif color == 'B':
            # 블루 로봇이 가야할 다음 좌표
            B_nxts.append(pos)

    # 로직
    # 모든 일이 마무리 될 때까지 반복 (1초 증가)
    while processing:
        O_actioned = False
        B_actioned = False
        # 로봇을 1행동(1이동/버튼 누르거나/아무것도x)

        # 1이동시킨다...!
        # 내가 다음 위치로 이동할 수 있다면...!
        if O_nxts:
            # 내 위치에서 앞으로 한칸 (해당 좌표와 1 가까워지기)
            if O_pos < O_nxts[0]:
                O_pos += 1
                O_actioned = True
            elif O_pos > O_nxts[0]:
                O_pos -= 1
                O_actioned = True

        # 블루 로봇 또한 위와 동일하게
        if B_nxts:
            if B_pos < B_nxts[0]:
                B_pos += 1
                B_actioned = True
            elif B_pos > B_nxts[0]:
                B_pos -= 1
                B_actioned = True

        # 버튼을 누르는 경우 (이동을 했을 때에는 제외!)
        if O_actioned == False and processing[0] == ('O', O_pos):
            # 오렌지 로봇이 버튼을 누른다~!
            # (-> 내가 다음으로 가려는 좌표들에서 현재 좌표를 빼주고!
            #                               processing에서도 제외!)
            O_nxts.pop(0)
            processing.pop(0)
        elif B_actioned == False and processing[0] == ('B', B_pos):
            # 블루 로봇이 버튼을 누르는 경우!
            B_nxts.pop(0)
            processing.pop(0)

        # 1초 증가시킨다.
        time += 1

    # 출력
    print(f"#{tc} {time}")