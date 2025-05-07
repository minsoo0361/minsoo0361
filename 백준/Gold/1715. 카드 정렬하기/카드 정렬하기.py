import heapq

N = int(input())

if N == 1:
    print(0)
    exit()

q= []
for _ in range(N):
    card = int(input())
    heapq.heappush(q, card)

result = 0

while 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)

    result += (a + b)
    if len(q) == 0:
        break

    heapq.heappush(q, a+b)
    
print(result)