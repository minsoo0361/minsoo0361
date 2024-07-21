board1 = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]
board2 = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]
N, M = map(int, input().split())
arr = [input() for _ in range(N)]
answer = []
for i in range(N-7): # i = 0, 1, 2 ...N-1까지
    for j in range(M-7): # j = 0, 1, 2 ... M-1까지
        result1 = 0
        result2 = 0
        for k in range(i, i+8): # k= 8*8보드에서 0부터 7까지는 돌아야하는데, i가 5일경우, 5~12까지는 돌아야함
            for l in range(j, j+8):
                if arr[k][l] != board1[k-i][l-j]:
                    result1 += 1
                elif arr[k][l] != board2[k-i][l-j]:
                    result2 += 1    
        answer.append(result1)
        answer.append(result2)
print(min(answer))