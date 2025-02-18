N = int(input())
arr = list(map(int, input().split()))
# arr = [2, 1, 1, 0]
result = [0] * N
# result = [4, 2, 1, 3]

for i in range(1, N+1): # 1번부터 N번사람까지 배치
    # i는 1, 2, 3, 4
    people = arr[i-1]
    # i = 3
    # people = 1
    cnt = 0

    for j in range(N): 
        # j = 0 부터 3까지
        if result[j] == 0:
            # 빈 자리일 때만 카운트
            if cnt == people:
                result[j] = i                
                break
            cnt += 1
print(*result)