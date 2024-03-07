from heapq import heappop, heappush

# 기본적으로 리스트 자료형을 사용하여 동작 수행...
hq = []   # 힙으로 사용할 리스트

# 우선순위큐에 값을 삽입하는 연산 enqueue -> heappush 함수
heappush(hq, 30)
heappush(hq, 10)
heappush(hq, 50)
heappush(hq, 100)
heappush(hq, 0)

# 우선순위큐에 삭제를 하는 연산 dequeue -> heappop 함수
item = heappop(hq)
print(item)

item = heappop(hq)
print(item)

item = heappop(hq)
print(item)

item = heappop(hq)
print(item)

item = heappop(hq)
print(item)


