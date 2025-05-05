a, b = map(int, input().split())
arr = [i for i in range(1, 101)]
answer = []
k = []
for i in range(1, len(arr)):
    answer.extend([i] * arr[i-1])
k = answer[a-1:b]
print(sum(k))