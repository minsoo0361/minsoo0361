def solution(k, tangerine):
    answer = 0
    # 귤이 [1, 3, 2, 5, 4, 5, 2, 3]인 경우에 k = 4
    # 정렬시키면 [1, 2, 2, 3, 3, 4, 5, 5]
    # 2 2개, 3 2개 or 2 2개, 5 2개, 3 2개, 5 2개 뽑으면 되므로 답은 2
    # 딕셔너리로 표현하면 {1:1, 2:2, 3:2, 4:1, 5:2}
    dict = {}
    for t in tangerine:
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
    sorted_dict = sorted(dict.values(), reverse=True)
    cnt = 0 # 귤의 총 개수
    type_cnt = 0 #귤의 종류 개수
    for l in sorted_dict: # [2,2,2,1,1]
        cnt += l
        type_cnt += 1
        if cnt >= k:
            break
            
    return type_cnt