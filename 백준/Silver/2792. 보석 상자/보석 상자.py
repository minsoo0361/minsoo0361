N, M = map(int, input().split())  # N은 학생 수, M은 보석 상자 수
arr = [int(input()) for _ in range(M)]

start = 1
end = max(arr)  # 가장 많은 보석이 든 박스를 기준으로 초기 설정

# 이진 탐색
result = end
while start <= end:
    mid = (start + end) // 2  # 현재 질투심
    total_boxes = 0          # 필요한 상자의 수 계산

    for jewels in arr:
        total_boxes += (jewels + mid - 1) // mid  # 올림 처리된 상자 수

    if total_boxes <= N:  # 상자를 N명에게 배분 가능하면 더 작은 질투심을 탐색
        result = mid
        end = mid - 1
    else:  # 상자가 부족하면 더 큰 질투심 탐색
        start = mid + 1

print(result)
