from collections import deque

def solution(elements):
    ans = set()
    dq = deque(elements) # [7,9,1,1,4]
    
    for _ in range(len(dq)): # 5번
        sum = 0
        for i in dq:  
            sum += i # [7, 16, 17, 18, 22]            
            ans.add(sum)
            
        dq.append(dq.popleft())        
    return len(ans)