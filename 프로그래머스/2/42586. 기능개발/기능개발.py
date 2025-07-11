def solution(progresses, speeds):
    answer = [] 
    n = len(progresses)
    lst = []
    for i in range(n):
        bepo =  ((100 - progresses[i]) // speeds[i]) 
        if (100 - progresses[i]) % speeds[i] != 0:
            bepo += 1
        lst.append(bepo)
    
    i = 0
    while i < n:
        cnt = 1
        for j in range(i+1, len(lst)):
            if lst[i] >= lst[j]:
                cnt += 1
            else:
                break
        answer.append(cnt)
        i += cnt
        
    return answer