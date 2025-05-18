def solution(s):
    stack = []
    for x in s:
        if x == '(':
            stack.append(x)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return not stack
