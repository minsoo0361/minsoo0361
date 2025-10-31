def solution(s):
    arr = s.split(' ')
    new_arr = []
    n = len(arr)
    for i in range(n):
        new_arr.append(int(arr[i]))
    max_num = max(new_arr)
    min_num = min(new_arr)
    answer = f'{min_num} {max_num}'
    return answer