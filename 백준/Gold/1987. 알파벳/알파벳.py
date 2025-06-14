# DFS 방식
import sys
input = sys.stdin.readline

di = [-1,1,0,0]
dj = [0,0,-1,1]

def dfs(ci, cj, cnt):
    global result
    result = max(result, cnt)

    #4방향 탐색, 범위 내, 중복값 아닌 경우
    for dir in range(4):
        ni = ci + di[dir]
        nj = cj + dj[dir]
        if 0 <= ni < r and 0 <= nj < c and visited[ord(alpha_lst[ni][nj])] == 0:
            visited[ord(alpha_lst[ni][nj])] = 1
            dfs(ni, nj, cnt+1)
            visited[ord(alpha_lst[ni][nj])] = 0
    return result

r, c = map(int, input().split())
alpha_lst = list(input() for _ in range(r))
result = 1
visited = [0] * 128 #아스키 코드 개수만큼 생성

visited[ord(alpha_lst[0][0])] = 1 #방문 표시
dfs(0, 0, 1) #currnet i, current j, cnt

print(result)