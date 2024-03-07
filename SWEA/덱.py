from collections import deque

q = deque()
q.append(1)
q.append(2)
print(q.popleft())
print(q.popleft())
#
# q = []
# for i in range(10000):
#     q.append(i)
# print('append')
# while q:
#     q.pop(0)
# print('end')