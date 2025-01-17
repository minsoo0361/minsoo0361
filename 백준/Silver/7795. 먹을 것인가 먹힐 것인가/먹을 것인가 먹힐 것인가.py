T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    B.sort()
    cnt = 0

    for a in A:
        start = 0
        end = len(B) - 1

        while start <= end:
            mid = (start + end) // 2
            if B[mid] < a: # A[i] > B[mid] A의 원소가 B보다 크다면
                start = mid + 1
            else:
                end = mid -1
        cnt += start

    print(cnt)