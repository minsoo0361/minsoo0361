def solution(want, number, discount):
    answer = 0
    # len(discount) = 14
    # 1 ~ 10
    # 2 ~ 11
    # 3 ~ 12
    # 4 ~ 13
    # 5 ~ 14
    for i in range(len(discount) - 9):
        dict = {}
        for t in discount[i:i+10]:
            cnt = 0
            if t in dict:
                dict[t] += 1
            else:
                dict[t] = 1
        
            for j in range(len(number)): #len(number) = 5
                
                if want[j] not in dict:
                    break
                else:
                    if dict[want[j]] >= number[j]:
                        cnt += 1
                        if cnt == len(number):
                            answer += 1
                            break 
            
    return answer