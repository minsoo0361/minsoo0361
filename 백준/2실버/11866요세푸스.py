from collections import deque

n, k = map(int, input().split())
dq = deque()
arr = []
for i in range(1, n+1):
    dq.append(i)
while len(dq) != 0:
    dq.rotate(-k+1)
    arr.append(dq.popleft())
print(f'<', end = '')
print(*arr, sep = ', ', end = '')
print(f'>')