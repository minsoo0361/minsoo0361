N, M = map(int, input().split())
card = list(map(int, input().split()))
arr = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            arr.append(card[i]+card[j]+card[k])
arr.sort()
strange = []
if M not in arr:
    for i in range(len(arr)):
        if arr[i] < M:
            strange.append(arr[i])
    print(max(strange))
else:
    print(M)


