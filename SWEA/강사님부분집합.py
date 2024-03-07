A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def dfs(i, subset, total):
    # 기저조건 : i가 A의 길이만큼 진행을 하였다면 종료!
    if i == len(A):
        # 부분집합의 합이 10인 경우라면? 출력
        if total == 10:
            print(subset)
        return
    # 가지치기 : subset의 전체 합이 10을 넘어가는 경우
    if total > 10:
        return
    # 재귀호출


    # A집합 해당 i 번째 인덱스의 요소를 포함 o
    subset.append(A[i])  # 결정
    dfs(i + 1, subset, total + A[i])

    # A집합 해당 i 번째 인덱스의 요소를 포함하지 않음
    subset.pop()
    dfs(i + 1, subset, total)

