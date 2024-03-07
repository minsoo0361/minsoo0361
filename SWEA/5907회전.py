T = int(input())
for tc in range (1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    # 1. 선형큐
    #
    # for _ in range(M):
    #     x = num.pop(0)   # dequeue , 시간복잡도  0(N)
    #     num.append(x)    # enqueue,, 시간복잡도  0(1)
    # print(f'#{tc} {num[0]}')


    # 2. 원형큐  : front, rear 변수...
    # 0, 1, 2, 3, 4, ..-> n-1 -> 0.. 인덱스가 순회
    # 초기화
    # q = [0] + num
    #
    # # 데이터가 꽉 차있는 상태..!
    # front = 0
    from collections import deque
    q = deque[num]

    # M번 dequeue -> enqueue 반복 수행
    for _ in range(M):
        x = q.popleft()
        q.append(x)
    print(q[0])
    #     # dequeue 과정
    #     front = (front + 1) % len(q)
    #     x = q[front]
    #     # enqueue 과정
    #     rear = (rear + 1) % len(q)
    #     q[rear] = x





    # 인덱스를 통해서 M번 순회하는 방법
    # front = 0
    # for _ in range(M):
    #     front = (front + 1) % N
    # 출력
    # print(f'#{tc} {num[0]}')