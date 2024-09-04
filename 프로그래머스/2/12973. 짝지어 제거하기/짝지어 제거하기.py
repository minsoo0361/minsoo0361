def solution(s):
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):        
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer