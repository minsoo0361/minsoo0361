def solution(number, k):
    answer = []
    
    for n in number:
        while answer and k > 0 and answer[-1] < n:
            answer.pop()
            k -= 1
        answer.append(n)
    while k > 0:
        answer.pop()
        k -= 1
    return "".join(answer)