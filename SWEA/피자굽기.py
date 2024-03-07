T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕 크기, 피자 개수
    pizza = list(map(int, input().split()))
    cheese = []

    for i in range(M):
        cheese.append([i + 1, pizza[i]])  # 인덱스 & 치즈 양 정보 apppend

    bake = cheese[:N]  # 화덕에 들어가는 피자
    wait = cheese[N:]  # 대기 중인 피자

    while len(bake) != 1:  # 마지막 피자 하나 남을 때까지
        melt = bake.pop(0)  # 일단 맨앞 피자 꺼냄
        melt[1] //= 2  # melt[0]은 인덱스, melt[1]은 치즈의 양
        if melt[1] == 0:  # 꺼내봤을 때 0이라면, 대기 중인 피자 넣음
            if wait:
                bake.append(wait.pop(0))
        else:  # 치즈가 다 녹지 않았다면, 다시 넣음
            bake.append(melt)

    print(f'#{tc} {bake[0][0]}')