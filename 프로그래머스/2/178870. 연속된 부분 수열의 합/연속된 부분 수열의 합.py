def solution(lst, k):
    n = len(lst)
    min_length = float('inf')
    best_start, best_end = -1, -1

    # 두 포인터 초기화
    start = 0
    current_sum = 0

    for end in range(n):
        current_sum += lst[end]

        # 현재의 부분합이 k보다 크면 start를 이동하여 부분합을 줄인다
        while current_sum > k and start <= end:
            current_sum -= lst[start]
            start += 1
        
        # 부분합이 k와 같으면 길이를 비교하고 최적의 부분 배열을 저장한다
        if current_sum == k:
            if (end - start) < min_length:
                min_length = end - start
                best_start, best_end = start, end

    if best_start == -1:
        return []  # 조건을 만족하는 부분 배열이 없는 경우

    return [best_start, best_end]