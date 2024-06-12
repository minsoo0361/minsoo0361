N, M = map(int, (input().split()))
arr = [input() for _ in range(N)]
result = []
# 리스트를 8*8 로 쪼개기
for i in range(0, N-7):
    for j in range(0, M-7):
        count1 = 0
        count2 = 0
        # 8*8 보드를 하나씩 검사하기
        for x in range(i, i+8):
            for y in range(j, j+8):
                # 인덱스 합이 짝수인 경우 일정한 색 가지게 됨
                if (x+y) % 2 == 0:
                    # 0,0 이 검정색인 경우
                    if arr[x][y] != 'W':
                        count1 += 1
                    # 0,0 이 하얀색인 경우
                    if arr[x][y] != 'B':
                        count2 += 1
                # 인덱스 합이 홀수인 경우
                else:
                    if arr[x][y] != 'W':
                        count2 += 1
                    if arr[x][y] != 'B':
                        count1 += 1
        result.append(count1)
        result.append(count2)
print(min(result))




