N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse = True)
S = []
for i in range(N):
    S.append(A[i] * B[i])
print(sum(S))


