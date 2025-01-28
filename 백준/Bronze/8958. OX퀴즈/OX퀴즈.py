T = int(input())
for _ in range(T):
    arr = list(map(str, input()))    
    result = []
    cnt = 0
    for i in arr:
        if i == "O":
            cnt += 1
            result.append(cnt)
        else:
            cnt = 0
    print(sum(result))