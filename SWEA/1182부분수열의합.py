N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
for i in range(1, 1<<N):
    total = 0
    for j in range (N):
        if i & 1 <<j:
            total += arr[j]
    if total == S:
        answer +=1
print(answer)