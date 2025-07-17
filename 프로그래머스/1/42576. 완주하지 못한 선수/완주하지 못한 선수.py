def solution(participant, completion):
    answer = ''
    dict = {}
    for name in participant:
        if name in dict:
            dict[name] += 1
        else:
            dict[name] = 1
    
    for check in completion:
        if check in dict:
            dict[check] -= 1
    for i in dict:
        if dict[i] == 1:
            answer = i
    return answer