# N- Queen 문제

# 완전 탐색(DFS)

# 내가 해당 (row, col)에 퀸을 배치할 수 있는지 체크
# 대각선에 대해서 서로 영역이 겹치지 않는지만 간단하게 체크



# 중첩함수 : 내부 함수를 만들어서 간단하게 정리
def n_queen_solve(N):

    def check(row, col):
        # 이전까지 놓아져 있는 퀸이 내가 놓으려고 하는
        for x in range(row):  # [0, row)
            y = board[x]
            # (row, col)의 위치와 대각선 영역이 서로 겹치는가
            if abs(x - row) == abs(y - col):
                return False  # 놓을 수가 없어요!
        return True

    def dfs(depth):
        nonlocal cnt, visited, board
        # 기저조건(종료조건) : depth가 queen의 갯수 만큼 카운트가 되었을 때
        # -> queen이 N개 놓여져 있을 때 중단하겠다
        if depth == N:
            cnt += 1
            return
        #     # TODO : 퀸이 올바르게 놓여져 있지를 대각선 체크!!
        #     # 좌하단, 우하단에 퀸이 서로 겹치는 영역있는지 확인!
        # for x1 in range(N):
        #     y1 = board[x1]
        #     for x2 in range(x1+1, N):
        #         y2 = board[x2]
        #         # 퀸의 위치를 비교...
        #         # x축과 y축에 대한 거리가 서로 같다면 = 대각선에 있는 것!
        #         if abs(x1-x2) == abs(y1-y2):
        #             return
        #
        #     cnt += 1 # 퀸이 올바르게 배치되어 있는 경우 카운트 +1
        #     return
        # 재귀적으로 말을 배치..! 반복문을 통해서 1부터 N번까지의 모든 위치에 말을 놓아보도록 시도!
        for col in range(N):
                # 해당 행에 말을 배치..! 현재 위치 : (depth, col)
                # TODO : 해당 위치에 배치를 할 수 있는지 체크!
                if not visited[col] and check(depth, col):
                    board[depth] = col
                    # visited 배열을 통해 동일한 행(col)에 대해서 다른 퀸이 들어가지 않도록 체크
                    visited[col] = True   # 결정
                    dfs(depth+1)
                    visited[col] = False   # 복구

    visited = [False] * N
    # 배치할 말의 ㄷ위치
    board = [-1] * N
    cnt = 0
    dfs(0)

    return cnt



# N-퀸을 놓을 수 있는 횟수를 카운트하여 출력
N = int(input())
# 카운트 변수 (글로벌)
answer = n_queen_solve(N)
print(answer)
