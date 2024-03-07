def f(i, N):   # i는 인덱스 값
    # 기저조건 : 순열이 완성된 경우
    if i == N:
        print(P)
        return
    for j in range(i, N):
        P[i], P[j] = P[j], P[i]   # P[i] <--> P[j] 교환, 결정
        f(i + 1, N)
        P[i], P[j] = P[j], P[i]   # P[i] <--> P[j] 교환, 결정

P = [1, 2, 3]
N = len(P)
f(0, N)
