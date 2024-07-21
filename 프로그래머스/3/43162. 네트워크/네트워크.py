def solution(n, computers):    
    answer = 0
    visited = [False for _ in range(n)] # 방문 여부 저장 배열. 현재 [False, False, False]
    for com in range(n):    # com = 0, 1, 2
        if visited[com] == False:   # visited[0] == False,
            DFS(n, computers, com, visited)
            answer += 1
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True # 해당 노드의 방문을 True로 변경
    for i in range(n):  # 0, 1, 2
        if i != com and computers[i][com] == 1 and visited[i] == False:
            DFS(n, computers, i, visited)
    