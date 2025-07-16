cnt = 0
def dfs(numbers, target, idx, res):
    global cnt
    
    if idx == len(numbers):
        if res == target:
            cnt += 1
        return
    else:
        dfs(numbers, target, idx+1, res + numbers[idx])
        dfs(numbers, target, idx+1, res - numbers[idx])

def solution(numbers, target):
    dfs(numbers, target, 0 ,0)
    return cnt