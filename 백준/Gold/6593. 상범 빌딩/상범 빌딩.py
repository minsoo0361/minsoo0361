from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

point = []

def bfs(start_z, start_x, start_y):
    global point
    
    queue = deque()
    queue.append((start_z, start_x, start_y, 0))
    visited[start_z][start_x][start_y] = True

    while queue:
        z, x, y, time = queue.popleft()
       
        if z == point[0] and x == point[1] and y == point[2]:
            return f"Escaped in {time} minute(s)."
       
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            # 유효성 검사: 범위 내인지, 벽이 아닌지, 방문하지 않았는지
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and \
               build[nz][nx][ny] != '#' and not visited[nz][nx][ny]:
                
                visited[nz][nx][ny] = True
                queue.append((nz, nx, ny, time + 1))
    
    return "Trapped!" # 'E'에 도달할 수 없는 경우

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break
    
    build = []
    start_s_pos = None # 'S' 지점의 좌표를 저장할 변수

    for i in range(L): # 층(level, z) 반복
        floor_rows = []
        for j in range(R): # 행(row, x) 반복
            row_chars = list(input().strip()) # 한 행을 문자로 리스트화
            for k in range(C): # 열(column, y) 반복
                if row_chars[k] == 'S':
                    start_s_pos = (i, j, k) # 'S' 좌표 (z, x, y)
                elif row_chars[k] == 'E':
                    point = [i, j, k] # 'E' 좌표 (z, x, y), 전역 point에 할당
            floor_rows.append(row_chars)
        build.append(floor_rows) 
        input()

    visited = [[[False] * C for _ in range(R)] for _ in range(L)]    

    if start_s_pos: # 'S' 지점이 유효한지 확인
        print(bfs(start_s_pos[0], start_s_pos[1], start_s_pos[2]))
    else:
        # 문제 조건상 S는 항상 존재한다고 가정
        print("Error: Start point 'S' not found.")