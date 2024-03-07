from collections import deque

N, K = map(int, input().split())
dq = deque()
arr = []
for i in range(1, N+1):
    dq.append(i)
while len(dq)!= 0:
    dq.rotate(-K + 1)
    arr.append(dq.popleft())
print('<', end = '')
print(*arr, end = '', sep = ', ')
print('>')


