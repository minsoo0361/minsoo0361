def solution(pri, location):
    answer = 0
    n = len(pri)
    queue = [i for i in range(n)] 
    lst = []
    
    while pri:
        if pri[0] == max(pri):
            lst.append(queue[0])
            pri.pop(0)
            queue.pop(0)
        else:
            queue.append(queue[0])
            queue.pop(0)
            pri.append(pri[0])
            pri.pop(0)
    for i in range(n):
        if lst[i] == location:
            answer = i + 1
    return answer