n, T = map(int, input().split())
lst = set()
for _ in range(n):
    x, y = map(int, input().split())
    lst.add((x, y))

queue = [[0, 0, 0]]
peak = False
while queue:
    start_x, start_y, cnt = queue.pop(0)

    if start_y == T:
        peak = True
        print(cnt)
        break

    for i in range(-2, 3):
        for j in range(-2, 3):
            nx = start_x + i
            ny = start_y + j
            if (nx, ny) in lst:
                queue.append([nx, ny, cnt + 1])
                lst.remove((nx, ny))
if not peak:
    print(-1)
