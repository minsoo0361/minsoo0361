def dfs(row):
    global answer
    if row >= N:
        answer += 1
        return      
    for i in range(N):
        if col[i] == True:
            continue
        if ld[row+i] == True:
            continue        
        if rd[row-i+N] == True:
            continue
        col[i] = True
        ld[row+i] = True        
        rd[row-i+N] = True
        dfs(row+1)
        col[i] = False
        ld[row+i] = False
        rd[row-i+N] = False

N = int(input())
col = [False] * N 
ld = [False] * (N * 2)
rd = [False] * (N * 2)
answer = 0 
dfs(0)
print(answer)
