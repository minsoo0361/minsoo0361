N = 10     # 큐 생성

q = [0] * 10

front = rear = -1  # 초기화

# 큐 삽입 연산 enqueue
def enqueue(item):
    global rear
    if is_full():
        return -1
    # 꼬리 rear을 1 증가시키고 그 위치에 요소를 삽입한다.
    rear = rear + 1
    q[rear] = item

# 큐 삭제 연산 dequeue:
def dequeue():
    global front
    if is_empty():
        return -1
    # 머리 front 1 증가 시키고 그 위치에 요소를 반환
    front = front + 1
    return q[front]

# 보조 연산 ...
# is_full : 가득 차있는 상태
def is_full():
    return rear == N -1

# is_empty : 비어있는 상태
def is_empty():
    return front == rear

# q_peek : 꺼낼 요소를 미리 확인해볼 수 있는 peek
def q_peek():
    return q[front + 1]

# 큐를 구현하여 1, 2, 3 원소를 순서대로 삽입
# 큐에서 값을 3개를 꺼내 차례대로 출력한다

enqueue(1)
enqueue(2)
enqueue(3)

item = dequeue()
print(item)
item = dequeue()
print(item)
item = dequeue()
print(item)